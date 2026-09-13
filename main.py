from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
from dotenv import load_dotenv
from typing import Optional
import os

load_dotenv()

app = FastAPI()

# Database connection
connection_url = URL.create(
    "postgresql",
    username="postgres",
    password=os.getenv("DATABASE_PASSWORD"),
    host="localhost",
    port=5432,
    database="sih_document_db"
)

engine = create_engine(connection_url)

# CORS for existing Vercel frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "SIH Document Search API is working!"}


@app.get("/documents/search")
def search_documents(
    fir_number: Optional[str] = None,
    case_number: Optional[str] = None,
    officer_name: Optional[str] = None,
    document_type: Optional[str] = None,
    section: Optional[str] = None,
    document_date: Optional[str] = None
):
    try:
        query = text("""
            SELECT
                id,
                fir_number,
                case_number,
                officer_name,
                document_type,
                document_date,
                section,
                file_path
            FROM documents
            WHERE
                (:fir_number IS NULL OR fir_number ILIKE :fir_number)
                AND (:case_number IS NULL OR case_number ILIKE :case_number)
                AND (:officer_name IS NULL OR officer_name ILIKE :officer_name)
                AND (:document_type IS NULL OR document_type ILIKE :document_type)
                AND (:section IS NULL OR section ILIKE :section)
                AND (:document_date IS NULL OR document_date = CAST(:document_date AS DATE))
        """)

        with engine.connect() as conn:
            result = conn.execute(
                query,
                {
                    "fir_number": f"%{fir_number}%" if fir_number else None,
                    "case_number": f"%{case_number}%" if case_number else None,
                    "officer_name": f"%{officer_name}%" if officer_name else None,
                    "document_type": f"%{document_type}%" if document_type else None,
                    "section": f"%{section}%" if section else None,
                    "document_date": document_date
                }
            )

            documents = [dict(row._mapping) for row in result]

        return {"results": documents}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))