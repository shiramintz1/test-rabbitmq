from pydantic import BaseModel
from datetime import date
from typing import Optional

class User(BaseModel):
    full_name: str
    password: str
    mail: str

class Production(BaseModel):
    production_name: str
    production_date: Optional[date]
    sensor_source: Optional[str]
    production_status: Optional[str]
    storage_location: Optional[str]
    number_of_images: Optional[int]
