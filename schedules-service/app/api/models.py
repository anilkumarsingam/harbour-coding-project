import uuid
from typing import Optional, List
from pydantic import BaseModel, Field

class Interval(BaseModel):
    start: str = Field(...)
    end: str = Field(...)

class Rule(BaseModel):
    day: str = Field(...)
    intervals : List[Interval] = Field(...)

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
                                                "start":"11:00",
                                                "end":"19:00"
                                        },
                                        {
                                                "start":"20:00",
                                                "end":"21:00"
                                        }
                                ],
                                "day":"MONDAY"
                        },
                        {
                                "type":"day",
                                "intervals":[
                                        {
                                                "start":"09:00",
                                                "end":"17:00"
                                        }
                                ],
                                "day":"FRIDAY"
                        }
                ],
                "timezone": "Asia/Kolkata"
            }
        }

