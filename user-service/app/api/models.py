from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
import uuid

class UserIn(BaseModel):
    name: str = Field(...)
    email: EmailStr = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "name": "testName",
                "email": "test@test.com",
            }
        }



class UserOut(UserIn):
    id: int 


class UserUpdate(UserIn):
    name: Optional[str] = None
    email: Optional[EmailStr] = None

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "name": "testName",
                "email": "test@test.com",
            }
        }

