from enum import Enum
from fastapi import Body, FastAPI

app = FastAPI()

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
def create_post(payload: dict = Body(...)):
    print(payload)
    return {"data": {"id": 1, "title": "post 1"}}


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


# needy, a required str
# skip, an int with a default value of 0.
# limit, an optional int.
@app.get("/items/{item_id}")
def read_item(item_id: int, needy: str, skip: int = 0, limit: int | None = None):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
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
