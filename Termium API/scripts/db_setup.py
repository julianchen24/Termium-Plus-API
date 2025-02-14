from sqlmodel import SQLModel, create_engine
from app.models import Term  # Import Term since it defines table structure
import logging

def setup_database():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    try:
        DATABASE_URL = "sqlite:///./data/terms.db"
        engine = create_engine(DATABASE_URL)
        SQLModel.metadata.create_all(engine)
        logger.info("Database setup complete")
        
    except Exception as e:
        logger.error(f"Error during database setup: {str(e)}")
        raise

if __name__ == "__main__":
    setup_database()