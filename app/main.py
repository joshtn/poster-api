from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models
from .database import engine, get_db
from .routers import post, user, auth, vote
from .config import settings

# this cmd tells sql alchemy to run create statement to gen tables
# now using alembic so dont need this cmd.
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return {"data": posts}


@app.get("/")
def root():
    return {"message": "Goat first api!!"}

