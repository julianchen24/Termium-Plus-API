from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, or_
from app.database import get_db
from app.models import Term
from app.schemas import TermsResponse
from fuzzywuzzy import fuzz
from typing import List

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Welcome to Terminium Plus API"}

@router.get("/term", response_model=TermsResponse)
async def get_term(term: str, lang: str, subject: str | None = None, term_threshold: int = Query(default=80, ge=0, le=100),subject_threshold: int = Query(default=70, ge=0, le=100),db: AsyncSession = Depends(get_db)):
    if lang not in ["en", "fr", "es", "pt"]:
        raise HTTPException(
            status_code=400,
            detail="Invalid language code. Supported codes are: en, fr, es, pt"
        )
    try:
        
        if lang == "en":
            term_field = Term.term_en
            subject_field = Term.subject_en
        elif lang == "fr":
            term_field = Term.terme_fr
            subject_field = Term.domaine_fr
        else:
            term_field = getattr(Term, f"terme_term_{lang}")
            subject_field = getattr(Term, f"dom_subj_{lang}")
        
        # 1.We split into 3 chunks to allow for a more flexible search
        # 2.After we split this, each of the three terms will return database entries similar to the three letter subword
        # 3.Once we split it, we use fuzzy ratio to compare each of the entries
        search_chunks = []
        for i in range(len(term) - 2):
            chunk = term[i:i+3]
            search_chunks.append(chunk)
        conditions = []
        for chunk in search_chunks:
            condition = term_field.ilike(f"%{chunk}")
            conditions.append(condition)
        query = select(Term).where(or_(*conditions)) 

        if subject:
            query = query.where(subject_field.ilike(f"%{subject}%"))
        result = await db.execute(query)
        candidates = result.scalars().all()

        filtered_terms = []

        for candidate in candidates:
            # Get term and subject values based on language
            if lang == "en":
                term_value = candidate.term_en
                subject_value = candidate.subject_en
            elif lang == "fr":
                term_value = candidate.terme_fr
                subject_value = candidate.domaine_fr
            else:
                term_value = getattr(candidate, f"terme_term_{lang}")
                subject_value = getattr(candidate, f"dom_subj_{lang}")
        
            if term_value:
                term_score = fuzz.ratio(term.lower(),term_value.lower())
                
            else:
                term_score = 0
            if subject_value and subject:
                subject_score = fuzz.ratio(subject.lower(),subject_value.lower())
            else:
                subject_score = 100
            
            if term_score >= term_threshold and subject_score >= subject_threshold:
                filtered_terms.append(candidate)

        
        return TermsResponse(count=len(filtered_terms), results=filtered_terms)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    


