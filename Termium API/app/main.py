# venv\Scripts\Activate.ps1


from fastapi import FastAPI
from app.api.endpoints import router
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

app = FastAPI(
    title="Terminium Plus API",
    description="API for querying the Terminium Plus terminology database",
    version="1.0.0"
)

app.include_router(router)

@app.on_event("startup")
async def startup_event():
    logging.info("Starting up FastAPI application")