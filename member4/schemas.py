from typing import Optional
from datetime import date
from pydantic import BaseModel


class DocumentResponse(BaseModel):
    id: int
    fir_number: Optional[str] = None
    case_number: Optional[str] = None
    officer_name: Optional[str] = None
    document_type: Optional[str] = None
    document_date: Optional[date] = None
    section: Optional[str] = None
    file_path: Optional[str] = None