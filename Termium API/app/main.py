# venv\Scripts\Activate.ps1
# Run these if database has not been initialized yet
# python scripts/db_setup.py
# python scripts/import_data.py

# To run tests, cd into Termium API/tests and run pytest

# uvicorn app.main:app --reload

from fastapi import FastAPI
from app.api.endpoints import router
import logging

app = FastAPI(
    title="Terminium Plus API",
    description="API for querying the Terminium Plus terminology database",
    version="1.0.0"
)

app.include_router(router)

@app.on_event("startup")
async def startup_event():
    logging.info("Starting up FastAPI application")