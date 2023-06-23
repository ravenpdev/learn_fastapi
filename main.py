from enum import Enum
from typing import Annotated
from pydantic import BaseModel
from fastapi import Body, FastAPI, Path, Query

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


# @app.put("/items/{item_id}")
# def update_item(
#     item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
#     q: str | None = None,
#     item: Item | None = None,
# ):
#     results: dict[str, object] = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     if item:
#         results.update({"item": item})
#     return results


# @app.put("/items/{item_id}")
# def update_item(
#     item_id: int,
#     item: Item,
#     user: User,
#     importance: Annotated[int, Body()],
# ):
#     results = {
#         "item_id": item_id,
#         "item": item,
#         "user": user,
#         "importance": importance,
#     }
#     return results


# Embed a single body parameter
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results
