from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database import get_db
from app.models import Term
from app.schemas import TermsResponse

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Welcome to Terminium Plus API"}

@router.get("/term", response_model=TermsResponse)
async def get_term(term: str, lang: str, subject: str | None = None, db: AsyncSession = Depends(get_db)):
    if lang not in ["en", "fr", "es", "pt"]:
        raise HTTPException(
            status_code=400,
            detail="Invalid language code. Supported codes are: en, fr, es, pt"
        )
    try:
        # Build query
        if lang == "en":
            term_field = Term.term_en
            subject_field = Term.subject_en
        elif lang == "fr":
            term_field = Term.terme_fr
            subject_field = Term.domaine_fr
        else:
            term_field = getattr(Term, f"terme_term_{lang}")
            subject_field = getattr(Term, f"dom_subj_{lang}")
        
        query = select(Term).where(term_field.ilike(f"%{term}%"))
        if subject:
            query = query.where(subject_field.ilike(f"%{subject}%"))
        result = await db.execute(query)
        terms = result.scalars().all()
        
        return TermsResponse(count=len(terms), results=terms)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    


