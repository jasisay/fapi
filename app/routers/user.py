from fastapi import HTTPException,status,Depends,APIRouter
from ..  import models ,schemas
from ..util import hash
from sqlalchemy.orm import Session
from ..database import get_db
from . import oauth


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)




@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.UserOut)
def create_user(user:schemas.UserCreate,db:Session = Depends(get_db),userId:int = Depends(oauth.get_current_user)):
    hashed_password = hash(user.password)
    user.password = hashed_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



@router.get("/{id}",response_model=schemas.UserOut)
def get_user(id:int,db:Session = Depends(get_db),user_id:int = Depends(oauth.get_current_user)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The user with id:{id} was not found.")
    return user

