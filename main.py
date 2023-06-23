from enum import Enum
from typing import Annotated
from pydantic import BaseModel
from fastapi import FastAPI, Path, Query

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str | None = None


fake_posts_db = [
    {"id": 1, "title": "Post 1"},
    {"id": 2, "title": "Post 2"},
    {"id": 3, "title": "Post 3"},
]


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/posts")
def get_posts(skip: int = 0, limit: int = 10):
    return fake_posts_db[skip : skip + limit]


@app.get("/posts/{id}")
def read_post(id: int, q: str | None = None, short: bool = False):
    post: dict[str, int | str] = {"post_id": id}

    if q:
        post.update({"q": q})
    if not short:
        post.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return post


@app.post("/posts")
def create_post(post: Post):
    print(post)
    return {"data": post}


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.get("/items")
def all_items(
    q: Annotated[
        str | None,
        Query(
            alias="item-query",
            min_length=5,
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            deprecated=True,
            include_in_schema=False,
        ),
    ] = None
):
    # def all_items(
    #     q: Annotated[
    #         list[str] | None,
    #         Query(
    #             title="Query String",
    #             description="Query string for the items to search in the database that have a good match",
    #         ),
    #     ] = None
    # ):
    results: dict[str, list[dict[str, str]] | list[str] | str] = {
        "items": [{"item_id": "Foo"}, {"item_id": "bar"}]
    }
    if q:
        results.update({"q": q})
    return results


@app.post("/items")
def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price * item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


# needy, a required str
# skip, an int with a default value of 0.
# limit, an optional int.
@app.get("/items/{item_id}")
def read_item(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    q2: Annotated[int, Query(ge=1, le=10)],
    q: Annotated[str | None, Query(alias="item-query")] = None,
):
    results: dict[str, str | int] = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


# def read_item(item_id: int, needy: str, skip: int = 0, limit: int | None = None):
#     item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
#     return item


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int,
    item_id: str,
    q: str | None = None,
    short: bool = False,
):
    item = {"item_id": item_id, "owner_id": user_id}

    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )

    return item


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name is ModelName.lenet:
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
