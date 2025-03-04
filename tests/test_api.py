import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
import logging
import asyncio
from pathlib import Path
from app.main import app
from app.database import get_db
from app.models import Term

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

TEST_DATABASE_URL = "sqlite+aiosqlite:///test.db" 
engine = create_async_engine(
    TEST_DATABASE_URL,
    echo=True
)

TestingSessionLocal = sessionmaker(
    engine,
    class_=AsyncSession,  
    expire_on_commit=False
)

test_terms = [
    {
        "id": 1,
        "subject_en": "Sports",
        "term_en": "Boxing",
        "terme_term_fr": "Boxe",
        "terme_term_es": "Boxeo",
        "terme_term_pt": "Boxe"
    }
]


async def init_test_db():
    try:
        async with engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.drop_all)
            await conn.run_sync(SQLModel.metadata.create_all)
        logger.info("Test database initialized successfully")
    except Exception as e:
        logger.error(f"Error initializing test database: {e}")
        raise

async def get_test_db():
    try:
        async with TestingSessionLocal() as session:
            logger.info("Test database session created")
            yield session
            await session.commit()
    except Exception as e:
        logger.error(f"Database session error: {e}")
        await session.rollback()
        raise

app.dependency_overrides[get_db] = get_test_db

@pytest.fixture(scope="session")
def event_loop():
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(autouse=True)
async def setup_db():
    try:
        await init_test_db()
        async with TestingSessionLocal() as session:
            for term_data in test_terms:
                term = Term(**term_data)
                session.add(term)
            await session.commit()
            logger.info("Test data loaded successfully")
    except Exception as e:
        logger.error(f"Error in setup_db: {e}")
        raise

@pytest.fixture
def client():
    return TestClient(app)

def test_root_endpoint(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Terminium Plus API"}

@pytest.mark.asyncio
async def test_term_search_valid(client):
    try:
        response = client.get("/term?term=Box&lang=en")
        assert response.status_code == 200
        
    except Exception as e:
        logger.error(f"Error in test_term_search_valid: {e}")
        if hasattr(response, 'text'):
            logger.error(f"Response text: {response.text}")
        raise

def test_term_search_invalid_language(client):
    response = client.get("/term?term=Box&lang=invalid")
    assert response.status_code == 400
    assert "Invalid language code" in response.json()["detail"]