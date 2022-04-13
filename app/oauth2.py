from jose import JWTError, jwt
from datetime import datetime, timedelta
from . import keys

#secret key
#algorithm
#expiration time


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now() + timedelta(minutes=keys.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, keys.SECRET_KEY, algorithm=keys.ALGORITHM)

    return encoded_jwt

