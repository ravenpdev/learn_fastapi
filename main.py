from enum import Enum
from typing import Annotated
from pydantic import BaseModel, Field
from fastapi import Body, FastAPI, Path, Query

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None,
        title="The Description of the item",
        max_length=300,
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: float | None = None


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    result = {"item_id": item_id, "item": item}
    return result
