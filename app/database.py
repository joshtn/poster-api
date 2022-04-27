from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .keys import SQLALC_DB_URL
import psycopg2
from psycopg2.extras import RealDictCursor
import time

SQLALCHEMY_DATABASE_URL = SQLALC_DB_URL

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# not using this raw sql. Now using sqlalchemy
# while True:

#     try:
#         conn = psycopg2.connect(host=keys.HOST, database=keys.DB, user=keys.USER, password=keys.PASSW, cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was successfull!")
#         break
#     except Exception as error:
#         print("Connecting to database failed")
#         print("Error: ", error)
#         time.sleep(2)


# used this before 
# my_posts = [{"title": "post 1", "content": "content 1", "id": 1},{"title": "best pizza", "content": "kebab", "id": 2}]

# def find_post(id):
#     for p in my_posts:
#         if p["id"] == id:
#             return p


# def find_index_post(id):
#     for i, p  in enumerate(my_posts):
#         if p["id"] == id:
#             return i


