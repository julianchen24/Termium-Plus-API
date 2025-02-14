from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Optional
from app.database import get_db
from app.models import Term
from app.schemas import TermsResponse
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

@router.get("/term", response_model=TermsResponse)
async def get_term(
    term: str,
    lang: str,
    db: AsyncSession = Depends(get_db)
):
    logger.info(f"Searching for term: {term} in language: {lang}")
    
    if lang not in ["en", "fr", "es", "pt"]:
        logger.warning(f"Invalid language code provided: {lang}")
        raise HTTPException(
            status_code=400,
            detail="Invalid language code. Supported codes are: en, fr, es, pt"
        )
    
    # Build query based on language
    lang_field = f"term_{lang}" if lang == "en" else f"terme_term_{lang}"
    query = select(Term).where(getattr(Term, lang_field).ilike(f"%{term}%"))
    
    try:
        result = await db.execute(query)
        terms = result.scalars().all()
        
        if not terms:
            logger.info(f"No matches found for term: {term}")
            raise HTTPException(
                status_code=404,
                detail="No matches found for the specified term"
            )
        
        logger.info(f"Found {len(terms)} matches for term: {term}")
        return TermsResponse(count=len(terms), results=terms)
        
    except Exception as e:
        logger.error(f"Error processing query: {str(e)}")
        raise