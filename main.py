from typing import Any
from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse, RedirectResponse
from pydantic import BaseModel, EmailStr

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


# return type annotation
# @app.post("/items")
# async def create_item(item: Item) -> Item:
#     return item


# return type annotation
# @app.get("/items")
# async def read_items() -> list[Item]:
#     return [
#         Item(name="Portal Gun", price=42.0),
#         Item(name="Plumbus", price=32.0),
#     ]


# response_model parameter
@app.post("/items", response_model=Item, response_model_exclude_unset=True)
async def create_item(item: Item) -> Any:
    return item


@app.get("/items", response_model=list[Item], response_model_exclude_unset=True)
async def read_items() -> Any:
    return [
        Item(name="Portal Gun", price=42.0),
        Item(name="Plumbus", price=32.0),
    ]


# Return the same input data
# class UserIn(BaseModel):
#     username: str
#     password: str
#     email: EmailStr
#     full_name: str | None = None
#
#
# class UserOut(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: str | None = None


# Don't do this in production!
# @app.post("/user", response_model=UserOut)
# async def create_user(user: UserIn) -> Any:
#     return user


class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserIn(BaseUser):
    password: str


@app.get("/user")
async def create_user(user: UserIn) -> BaseUser:
    return user


# RedirectREponse and JSONResposne are subclasses of Response
@app.get("/portal")
async def get_portal(teleport: bool = False) -> Response:
    if teleport:
        return RedirectResponse(url="https://www.locahost:8000/")
    return JSONResponse(content={"message": "Here's your interdimensional portal"})
