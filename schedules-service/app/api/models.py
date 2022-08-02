import uuid
from typing import Optional, List
from pydantic import BaseModel, Field

'''class Interval(BaseModel):
    start: str = Field(...)
    end: str = Field(...)'''

class Rule(BaseModel):
    day: str = Field(...)
    intervals : List[List[str]] = Field(...)

class Schedule(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    owner_id: int = Field(...)
    rules: Optional[List[Rule]] = Field(...)
    timezone: Optional[str] = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "name": "testName1",
                "owner_id": "1",
                "rules":[],
                "timezone": "Asia/Kolkata"
            }
        }


class ScheduleUpdate(BaseModel):
    name: str = Field(...)
    owner_id: int = Field(...)
    rules: Optional[List[Rule]] = Field(...)
    timezone: Optional[str] = Field(...)
    
    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "name": "testName1",
                "owner_id": "1",
                "rules":[
                                            {
                                "type":"day",
                                "intervals":[
                                        {
                                                "1100",
                                                "1900"
                                        },
                                        {
                                                "2000",
                                                "2100"
                                        }
                                ],
                                "day":"MONDAY"
                        },
                        {
                                "type":"day",
                                "intervals":[
                                        {
                                                "0900",
                                                "1700"
                                        }
                                ],
                                "day":"FRIDAY"
                        }
                ],
                "timezone": "Asia/Kolkata"
            }
        }

