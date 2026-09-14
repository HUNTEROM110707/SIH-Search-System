from fastapi import APIRouter, HTTPException
from typing import Optional

from .search import search_documents

router = APIRouter()


@router.get("/documents/search")
def search(
    fir_number: Optional[str] = None,
    case_number: Optional[str] = None,
    officer_name: Optional[str] = None,
    document_type: Optional[str] = None,
    section: Optional[str] = None,
    document_date: Optional[str] = None
):
    try:
        documents = search_documents(
            fir_number=fir_number,
            case_number=case_number,
            officer_name=officer_name,
            document_type=document_type,
            section=section,
            document_date=document_date
        )

        return {"results": documents}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))