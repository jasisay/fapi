from fastapi import APIRouter,HTTPException,Depends,status,Response
from sqlalchemy.orm import Session
from .. import database,schemas,models,util
from . import oauth
from fastapi.security.oauth2 import OAuth2PasswordRequestForm



router = APIRouter(tags=['Authentication'])

@router.post("/login",response_model=schemas.Token)
def login(user_credentials:OAuth2PasswordRequestForm = Depends(),db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Invalid credentials")
    if not util.verify(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Invalid credentials")
    access_token = oauth.create_access_token(data={"user_id":user.id})
    return {"access_token":access_token,"token_type":"bearer"}