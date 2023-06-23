from enum import Enum
from typing import Annotated
from pydantic import BaseModel, HttpUrl
from fastapi import FastAPI, Path, Query

app = FastAPI()


class Image(BaseModel):
    # url: str
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    image: Image | None = None
    images: list[Image] | None = None


class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item]


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results


@app.post("/offers")
def create_offer(offer: Offer):
    return offer


@app.post("/images/multiple")
def create_multiple_images(images: list[Image]):
    # editor support
    # couldn't get this kind of editor support if you were working directly
    # with dict instead of pydantic models.
    for image in images:
        print(image.url)
    return images


@app.post("/index-weights")
def create_index_weights(weights: dict[int, float]):
    return weights
