import sys
import os
from pathlib import Path


current_dir = Path(__file__).resolve().parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir))

from sqlalchemy.dialects.sqlite import dialect as sqlite_dialect
from sqlmodel import SQLModel, create_engine
from sqlalchemy import inspect
import logging

def setup_database():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    try:

        DATABASE_URL = "sqlite:///./data/terms.db"
        engine = create_engine(
            DATABASE_URL, 
            echo=True,
            connect_args={"check_same_thread": False},
            poolclass=None  
        )

        logger.info(f"Using dialect: {engine.dialect}")

        Path('./data').mkdir(exist_ok=True)

        logger.info("Dropping existing tables...")
        SQLModel.metadata.drop_all(engine)
        
        logger.info("Creating fresh tables...")
        SQLModel.metadata.create_all(engine)

        inspector = inspect(engine)
        tables = inspector.get_table_names()
        logger.info(f"Created tables: {tables}")
        
        for table in tables:
            columns = inspector.get_columns(table)
            logger.info(f"Columns in {table}: {[col['name'] for col in columns]}")
            
    except Exception as e:
        logger.error(f"Error during database setup: {str(e)}")
        raise

if __name__ == "__main__":
    setup_database()