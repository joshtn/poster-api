from app import schemas
from .database import client, session


def test_root(client):
    res = client.get("/")
    print(res.json().get("How to use api"))
    assert res.status_code == 200


def test_create_user(client):
    res = client.post("/users/", json={"email": "pytest1@gmail.com", "password": "test123"})
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "pytest1@gmail.com"
    assert res.status_code == 201

