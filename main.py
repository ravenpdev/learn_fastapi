from fastapi import FastAPI

app = FastAPI()


# Path Operation
# Path here refers to the last part of the URL starting form the first /
# Operation here referes to one of the HTTP "methods" POST, GET, PUT, DELETE
@app.get("/")  # this is the path operation decorator
def root():  # this is the path operation function
    return {"message": "Hello World"}
