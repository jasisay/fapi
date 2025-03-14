from jose import jwt,JWTError
from datetime import datetime,timedelta
from .. import schemas,database,models
from fastapi import Depends,status,HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from ..config import settings


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = settings.SECRET_KEY
ALGORYTHM = settings.ALGORITHM
Access_token_expiration_minutes = settings.ACCESS_TOKEN_EXPIRE_MINUTES


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=Access_token_expiration_minutes)
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORYTHM)
    return encoded_jwt


def verify_access_token(token:str,credential_exception):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORYTHM])
        id:str = payload.get("user_id")
        if id is None:
            raise credential_exception
        token_data = schemas.TokenData(id=id)
    except JWTError:
        raise credential_exception
    return token_data
    

def get_current_user(token:str = Depends(oauth2_scheme),db:Session = Depends(database.get_db)):
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"Invalid credentials",headers={"WWW.Authenticate":"Bearer"})
    token = verify_access_token(token,credential_exception)
    user = db.query(models.User).filter(models.User.id == token.id).first()
    return user