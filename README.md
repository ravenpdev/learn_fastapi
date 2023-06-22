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
