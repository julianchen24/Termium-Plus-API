# venv\Scripts\Activate.ps1
# Run these if database has not been initialized yet
# python scripts/db_setup.py
# python scripts/import_data.py

# To run tests, cd into Termium API/tests and run pytest

# uvicorn app.main:app --reload

# To build:
# docker build -t terminium-api .
# docker run -p 8000:8000 terminium-api
# http://localhosSt:8000


from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
import logging
import os
from pathlib import Path

static_dir = Path("app/static")
static_dir.mkdir(exist_ok=True, parents=True)

app = FastAPI(
    title="Terminium Plus API",
    description="API for querying the Terminium Plus terminology database",
    version="1.0.0"
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.mount("/data", StaticFiles(directory="app/static/data"), name="data")

@app.on_event("startup")
async def startup_event():
    logging.info("Starting up FastAPI application")

@app.get("/", response_class=HTMLResponse)
async def home():
    """Redirect to the static HTML page"""
    return RedirectResponse(url="/static/index.html")



from app.api.endpoints import router
app.include_router(router)


