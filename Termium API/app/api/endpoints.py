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
async def get_term(term: str, lang: str, db: AsyncSession = Depends(get_db)):
    if lang not in ["en", "fr", "es", "pt"]:
        raise HTTPException(
            status_code=400,
            detail="Invalid language code. Supported codes are: en, fr, es, pt"
        )
    
    try:
        # Build query
        if lang == "en":
            field = Term.term_en
        else:
            field = getattr(Term, f"terme_term_{lang}")
        
        query = select(Term).where(field.ilike(f"%{term}%"))
        result = await db.execute(query)
        terms = result.scalars().all()
        
        return TermsResponse(count=len(terms), results=terms)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))