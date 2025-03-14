from pydantic import BaseModel,EmailStr,conint
from datetime import datetime
from typing import Optional




class PostBase(BaseModel):
    title:str
    content:str
    published:bool = True
    likes : int = 0
    dislikes : int = 0
 
    
 

class CreatePost(PostBase):
    pass
    

class UpdatePost(PostBase):
    pass


class UserCreate(BaseModel):
    email :EmailStr
    password:str 


class UserOut(BaseModel):
    id: int
    email : EmailStr
    created_at :datetime



class UserLogin(BaseModel):
    email: EmailStr
    password:str




class Post(BaseModel):
    title:str
    content:str
    published:bool 
    owner_id:int
    Likes : int
    DisLikes : int
    owner:UserOut

    class Config:
        form_attributes = True
 


class Token(BaseModel):
    access_token:str
    token_type:str


class TokenData(BaseModel):
    id: Optional[int]
    
    
class Vote(BaseModel): 
    post_id : int
    dir : int
    
 