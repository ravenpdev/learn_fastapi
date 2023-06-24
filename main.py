from typing import Annotated
from fastapi import Body, FastAPI
from uuid import UUID
from datetime import datetime, time, timedelta

app = FastAPI()


@app.put("/items/{item_id}")
async def read_items(
    item_id: UUID,
    start_datetime: Annotated[datetime | None, Body()] = None,
    end_datetime: Annotated[datetime | None, Body()] = None,
    repeat_at: Annotated[time | None, Body()] = None,
    process_after: Annotated[timedelta | None, Body()] = None,
):
    start_process: datetime | None = None
    duration: timedelta | None = None

    if (
        start_datetime is not None
        and process_after is not None
        and end_datetime is not None
    ):
        start_process = start_datetime + process_after
        duration = end_datetime - start_process

    # datetime1: datetime = datetime(year=2023, month=11, day=29)
    # timedelta1: timedelta = timedelta(days=1)
    # print(datetime1 + timedelta1)

    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration,
    }
