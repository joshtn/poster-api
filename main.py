from fastapi import FastAPI
from fastapi.param_functions import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.get("/") #decorator, tells what path url
def root():
    return {"message": "Goat first api!!"}


@app.get("/posts")
def get_posts():
    return {"data": "this is posts"}


@app.post("/createposts")
def create_posts(post: Post):
    print(post)
    print(post.dict())
    return {"data": post}
