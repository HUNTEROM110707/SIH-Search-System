from typing import Optional
from datetime import date


class Document:
    id: int
    fir_number: Optional[str]
    case_number: Optional[str]
    officer_name: Optional[str]
    document_type: Optional[str]
    document_date: Optional[date]
    section: Optional[str]
    file_path: Optional[str]