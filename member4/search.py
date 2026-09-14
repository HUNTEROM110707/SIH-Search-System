from typing import Optional
from sqlalchemy import text
from .database import engine


def search_documents(
    fir_number: Optional[str] = None,
    case_number: Optional[str] = None,
    officer_name: Optional[str] = None,
    document_type: Optional[str] = None,
    section: Optional[str] = None,
    document_date: Optional[str] = None
):
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

        return [dict(row._mapping) for row in result]