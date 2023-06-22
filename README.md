# Learn FastAPI

## Setup

- Create a folder for your project
- CD into your project folder
- Create a virtual environment "python -m venv venv"
- Active your virtual environment "source venv/bin/activate"
- pip install fastapi
- pip install "uvicorn[standard]"

### First Steps

```python

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

#### Recap

- Import FastAPI
- Create an app instance
- Write path operation decorator(like @app.get("/"))
- Write a path operation function (like def root(): ... above)
- Run the development server (like uvicorn main:app --reload) --reload watch for changes on reload the server

### Path Parameters

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

```

> Notice that the value your function received (and returned) as python int, not as string "3". So with that type declaration, **FastAPI** gives you automatic request "parsing".

##### Pydantic

Al lthe data validation is performed under the hood by [Pydantic](https://docs.pydantic.dev/latest/),
so you get all the benefits from it. And you know you are in good hands.

You can use the same type declarations with str, flaot, bool and many other complex data types.

##### Order matters

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]


@app.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]

```

> The first one will always be used since the path matches first.

#### Predefined values

If you have a path operation that receives a path parameter, but you want the
valid path parameter values to be predefined, you can use a standard Python Enum.

##### Create an Enum class

Import Enum and create a sub-class that inherits from str and from Enum.

By inheriting from str the API docs will be able to know that the values must
of type string and will be able to render

```python
from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
```

##### Path parameters containing paths

##### OpanAPI support

OpenAPI doesn't support a way to declare a path parameter to contain a path inside, as that could lead to scenarios that are difficult to test and define.

Nevertheless, you can still do it in FastAPI, using one of the internal tools from Starlette.

And the docs would still work, although not adding any documentation telling that the parameter should contain a path.

##### Path convertor

Using an option directly from Starlette you can declare a path parameter containing a path using a URL like:

`/files/{file_path:path}`

In this case, the name of the parameter is file_path, and the last part, :path, tells it that the parameter should match any path.

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
```

#### Recap

With **FastAPI** by using short, intuitive and standard Python type declarations,
you get:

- Editor support: error checks, autocompletion, etc.
- Data "parsing"
- Data validation
- API annotation and automatic documentation
