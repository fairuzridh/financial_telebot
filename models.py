from pydantic import BaseModel
from datetime import datetime

class Transaction(BaseModel):
    id: int
    tele_id: int
    created_date: datetime
    category: str
    description: str
    nominal: float
    instrument: str
    note: str = None