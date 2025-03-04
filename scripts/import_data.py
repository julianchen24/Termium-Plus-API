import pandas as pd
from sqlalchemy import create_engine
import logging
from pathlib import Path

def import_csv(csv_path: str):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    try:
        # Read CSV and convert columns to lowercase
        df = pd.read_csv(csv_path)
        df.columns = df.columns.str.lower()
        
        # Add id column
        df['id'] = range(1, len(df) + 1)
        
        # Create database directory if it doesn't exist
        Path('./data').mkdir(exist_ok=True)
        
        # Import to database
        DATABASE_URL = "sqlite:///./data/terms.db"
        engine = create_engine(DATABASE_URL)
        df.to_sql('term', engine, if_exists='replace', index=False)
        logger.info("Data imported successfully")
        
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        raise

if __name__ == "__main__":
    csv_file = "./data/combined.csv"
    import_csv(csv_file)