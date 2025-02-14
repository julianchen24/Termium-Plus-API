import pandas as pd
from sqlalchemy import create_engine
import logging

def import_csv(csv_path: str):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    try:
        # Create engine
        DATABASE_URL = "sqlite:///./data/terms.db"
        engine = create_engine(DATABASE_URL)
        
        # Read CSV file
        logger.info(f"Reading CSV file: {csv_path}")
        df = pd.read_csv(csv_path)
        logger.info(f"Found {len(df)} rows in CSV")
        
        # Preview data structure
        logger.info("CSV columns:")
        logger.info(df.columns.tolist())
        
        # Import to database
        logger.info("Importing data to database...")
        df.to_sql('term', engine, if_exists='replace', index=False)
        
        logger.info("Import completed successfully")
        
    except Exception as e:
        logger.error(f"Error during import: {str(e)}")
        raise
    
if __name__ == "__main__":
    csv_file = "./data/Arts,_loisirs_et_sports_Arts,_Recreation_and_Sports_LJ.csv"
    import_csv(csv_file)