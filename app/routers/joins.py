from fastapi import Depends,HTTPException,APIRouter,status
from sqlalchemy.orm import Session
from typing import List
from sqlalchemy import text,func
from ..database import engine,get_db
from .. import models


router = APIRouter(
    prefix="/joins",
    tags=["Joins"]
)


def get_votes(post_id:int,db: Session = Depends(get_db)):
    votes = db.query(models.Post).join(models.Vote).filter(models.Vote.post_id == post_id).all()
    return votes

@router.get("/{post_id}")
def post_vote(post_id:int,db:Session = Depends(get_db)):
    likes = get_votes(post_id,db)
    for i in likes:
        print(str(i.id))
    user_id = ''
    with engine.connect() as conn:
        vote_id = conn.execute(text(f"select user_id from votes where post_id in ({post_id})"))
        for row in vote_id:
            user_id += str(row[0])
            user_id += ','
    
    
    
    return user_id




