from fastapi import FastAPI
from fastapi.param_functions import Body

app = FastAPI()

@app.get("/") #decorator, tells what path url
def root():
    return {"message": "Goat first api!!"}


@app.get("/posts")
def get_posts():
    return {"data": "this is posts"}

@app.post("/createposts")
def create_posts(payload: dict = Body(...)):
    print(payload)
    return {"new_post": f"title {payload['title']} content: {payload['content']}"}
