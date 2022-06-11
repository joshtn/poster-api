from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app import schemas
from app.config import settings
from app.database import get_db
from app.database import Base


SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


client = TestClient(app)


def test_root():
    res = client.get("/")
    print(res.json().get("How to use api"))
    assert res.status_code == 200


def test_create_user():
    res = client.post("/users/", json={"email": "pytest1@gmail.com", "password": "test123"})
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "pytest1@gmail.com"
    assert res.status_code == 201

