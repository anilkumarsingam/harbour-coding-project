from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from app.api.models import Schedule, ScheduleUpdate
from app.api.utils import find_overlap

schedules = APIRouter()

@schedules.post("/", response_description="Create a new schedule", status_code=status.HTTP_201_CREATED, response_model=Schedule)
async def create_schedule(request: Request, schedule: Schedule = Body(...)):
    schedule = jsonable_encoder(schedule)
    new_schedule = request.app.database["schedules"].insert_one(schedule)
    created_schedule = request.app.database["schedules"].find_one(
        {"_id": new_schedule.inserted_id}
    )

    return created_schedule


@schedules.get("/", response_description="List all schedules of owner", response_model=List[Schedule])
async def list_schedules(request: Request, owner_id: int = None):
    query = { "owner_id": owner_id }
    schedules = list(request.app.database["schedules"].find(query, limit=100))
    return schedules


@schedules.get("/{id}", response_description="Get a single schedule by id", response_model=Schedule)
async def find_schedule(id: str, request: Request):
    if (schedule := request.app.database["schedules"].find_one({"_id": id})) is not None:
        return schedule

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Schedule with ID {id} not found")


@schedules.put("/{id}", response_description="Update a schedule", response_model=Schedule)
async def update_schedule(id: str, request: Request, schedule: ScheduleUpdate = Body(...)):
    schedule = {k: v for k, v in schedule.dict().items() if v is not None}

    if len(schedule) >= 1:
        update_result = request.app.database["schedules"].update_one(
            {"_id": id}, {"$set": schedule}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Schedule with ID {id} not found")

    if (
        existing_schedule := request.app.database["schedules"].find_one({"_id": id})
    ) is not None:
        return existing_schedule

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Schedule with ID {id} not found")


@schedules.delete("/{id}", response_description="Delete a schedule")
async def delete_schedule(id: str, request: Request, response: Response):
    delete_result = request.app.database["schedules"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Schedule with ID {id} not found")


@schedules.get("/overlap/", response_description="Overlap betweeen schedules")
async def get_schedules_overlap(request: Request, owner_schedule_id: str = None, guest_schedule_id: str = None):
    owner_schedule = request.app.database["schedules"].find_one({"_id": owner_schedule_id})
    guest_schedule = request.app.database["schedules"].find_one({"_id": guest_schedule_id})

    if owner_schedule is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Schedule with ID {owner_schedule_id} not found")

    if guest_schedule is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Schedule with ID {guest_schedule_id} not found")

    overlap_rules = []
    for owner_rule in owner_schedule["rules"]:
        for guest_rule in guest_schedule["rules"]:
            if owner_rule["day"] == guest_rule["day"]:
                overlap_rules.append({
                    "day" : owner_rule["day"],
                    "intervals" : find_overlap(owner_rule["intervals"], guest_rule["intervals"])

                }) 

    overlap = {
        "rules" : overlap_rules,
        "timezone" : owner_schedule["timezone"]
    }

    return overlap
