# schemas.py
from pydantic import BaseModel, EmailStr
from datetime import date

class User(BaseModel):
    name: str
    age: int
    email: EmailStr
    gender: str
    mobile_number: int
    birthday: str  # Represent birthday as a date
    city: str
    state: str
    country: str
    address1: str
    address2: str = None
