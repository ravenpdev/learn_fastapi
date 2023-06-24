from typing import Annotated
from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items")
async def read_items(
    accept: Annotated[str | None, Header()] = None,
    user_agent: Annotated[str | None, Header()] = None,
):
    return {"Accept": accept, "User-Agent": user_agent}
