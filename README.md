# Terminium Plus API
A FastAPI-based REST API for querying multilingual terminology data based on [TERMIUM Plus®](https://open.canada.ca/data/en/dataset/94fc74d6-9b9a-4c2e-9c6c-45a5092453aa), the Government of Canada's terminology and linguistic data bank.

## Overview

This project provides an API service that allows users to search and retrieve specialized terminology across four languages—English, French, Spanish, and Portuguese—with support for fuzzy matching and subject/domain filtering.

It is particularly valuable for professionals dealing with complex legal, governmental, and industry-specific terminology, including:

- **Translators** ensuring precise term usage  
- **Policymakers and legal experts** handling legislative texts and official documents  
- **Regulatory bodies** working with trade agreements, compliance, and legal frameworks  
- **Researchers and domain specialists** requiring authoritative terminology references  

Unlike general dictionaries or translation tools, this database contains a vast collection of terms that exist nowhere else. Derived from **TERMIUM Plus®**, the Government of Canada’s official terminology and linguistic data bank, it includes millions of terms covering:

- **Government agency names**  
- **Corporate and organizational names**  
- **Legal concepts and industry regulations**  
- **Crop types, import/export rules, and trade-specific terminology**  
- **Specialized jargon across multiple domains**  

These terms are essential for **accurate communication** in **international trade, legal documentation, policy development, and technical translations**.

## Download CSV Dataset

To run this API with the necessary terminology data, download the compiled dataset from the latest GitHub release:

📥 **[Download CSV Dataset](https://github.com/julianchen24/Termium-Plus-API/releases/download/v1.0/combined.csv)**  

🔗 **[GitHub Release Page](https://github.com/julianchen24/Termium-Plus-API/releases/tag/v1.0)**

After downloading, place the `combined.csv` file into the `data/` directory before initializing the database.

## Features

- **Multilingual Support**: Search for terms in English, French, Spanish, and Portuguese
- **Fuzzy Search**: Find matches even with slight spelling variations using configurable similarity thresholds
- **Subject Filtering**: Filter terminology by domain/subject area
- **Comprehensive Data**: Access terms with their translations, abbreviations, synonyms, and contextual information
- **Fast Performance**: Efficient database queries with proper indexing
- **Docker Support**: Easy deployment using Docker containers
- **Interactive Documentation**: Auto-generated Swagger UI for API exploration

## API Endpoints

### Root Endpoint
```
GET /
```
Returns a welcome message or redirects to the landing page.

### Term Search
```
GET /term?term={search_term}&lang={language_code}
```

#### Parameters:
- `term` (string, required): The term to search for
- `lang` (string, required): Language code for the term being searched (en, fr, es, pt)
- `subject` (string, optional): Domain or subject area that provides context for the terminology
- `term_threshold` (integer, optional, default: 80): Similarity threshold for term matching (0-100)
- `subject_threshold` (integer, optional, default: 70): Similarity threshold for subject matching (0-100)

#### Example Requests:
```
GET /term?term=Boxing&lang=en
GET /term?term=Boxe&lang=fr&subject=Sports
GET /term?term=Boxng&lang=en  # Fuzzy search with typo
```

#### Response Format:
```json
{
  "count": 1,
  "results": [
    {
      "id": 1,
      "subject_en": "Sports",
      "term_en": "Boxing",
      "term_en_parameter": null,
      "abbreviation_en": null,
      "terme_fr": "Boxe",
      ...
    }
  ]
}
```

## Installation & Usage

### Prerequisites
- Python 3.8+
- Docker (optional, for containerized deployment)
- The terminology CSV data file (not included in repository)

### Docker Installation

```bash
# Clone the repository
git clone https://github.com/julianchen24/Termium-Plus-API.git
cd Termium-Plus-API

# Download the CSV file and place it in the data directory
# For Windows: copy combined.csv data/
# For Mac/Linux: cp combined.csv data/

# Build and run with Docker
docker build -t terminium-api .
docker run -p 8000:8000 terminium-api
```

### Manual Installation

```bash
# Clone the repository
git clone https://github.com/julianchen24/Termium-Plus-API.git
cd Termium-Plus-API

# Create and activate virtual environment
python -m venv venv
venv\Scripts\Activate.ps1  # Windows
source venv/bin/activate   # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Download the CSV file and place it in the data directory
# For Windows: copy combined.csv data/
# For Mac/Linux: cp combined.csv data/

# Initialize the database
python scripts/db_setup.py
python scripts/import_data.py

# Run the API
uvicorn app.main:app --reload
```

Once running, access:
- API landing page: http://localhost:8000
- Interactive API docs: http://localhost:8000/docs
- ReDoc documentation: http://localhost:8000/redoc

## Technical Implementation

This project is built with:

- **FastAPI**: A modern, fast web framework for building APIs with Python
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) library
- **SQLite**: Lightweight disk-based database for storing terminology data
- **Fuzzywuzzy**: Library for fuzzy string matching and similarity calculations
- **Docker**: For containerized deployment

## About TERMIUM Plus®

TERMIUM Plus® is the Government of Canada's terminology and linguistic data bank, one of the largest collections of terms and phrases in the world. It contains millions of terms in English, French, Spanish and Portuguese covering a wide range of fields including science, technology, medicine, law, arts, humanities, and more.

This API implementation provides a programmatic way to access and search a subset of terminology data in a format suitable for integration with other applications.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- The Translation Bureau of the Government of Canada for creating and maintaining TERMIUM Plus®

## Contact

Created by Julian Chen - feel free to contact me!

## Contributing
All contributions are welcome.

---

*Note: This project is not officially affiliated with or endorsed by the Government of Canada or the TERMIUM Plus® service.*
