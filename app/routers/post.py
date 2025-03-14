from fastapi import HTTPException,status,Depends,APIRouter
from ..  import models ,schemas
from ..util import hash
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List
from . import oauth
from typing import Optional
from sqlalchemy import func


router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)


@router.get('/{id}',response_model=schemas.Post)
def get_post(id:int,db: Session = Depends(get_db),current_user:int = Depends(oauth.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail = f"The post with id:{id} does not exist.")
    return post


@router.get("/",response_model=List[schemas.Post])
#@router.get("/")
def get_all_posts(db:Session = Depends(get_db),limit:int = 10,skip:int = 0,search:Optional[str] =""):

    posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    #results = db.query(models.Post,func.count(models.Vote.post_id).label("votes")).outerjoin(models.Vote,models.Vote.post_id == models.Post.id).group_by(models.Post.id).all()
    return posts

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
def create_post(post:schemas.CreatePost,db:Session = Depends(get_db),current_user:int = Depends(oauth.get_current_user)):
    #cursor.execute("SELECT * FROM posts WHERE id = %s",(str(id)))
    #post = cursor.fetchone()
    new_post = models.Post(owner_id = current_user.id,**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
    

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db:Session = Depends(get_db),current_user:int = Depends(oauth.get_current_user)):
  #  cursor.execute("DELETE FROM posts WHERE id = %s returning * ",(str(id)))
   # delete_post = cursor.fetchone()
    #conn.commit()
    

    delete_post = db.query(models.Post).filter(models.Post.id == id)
    if not delete_post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id:{id} was not found.")
    if delete_post.first().owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"You are forbidden to carry out this action.")
    delete_post.delete(synchronize_session=False)
    db.commit()
    return None

@router.put("/{id}",response_model=schemas.Post)
def update_post(post:schemas.UpdatePost,id:int,db:Session = Depends(get_db),current_user:int = Depends(oauth.get_current_user)):
    #cursor.execute("UPDATE posts SET title = %s, content = %s, published = %s WHERE id =%s  returning *",(post.title,post.content,post.published,str(post.id)))
    #new_post = cursor.fetchone()
    #conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id == id )
    new_post = post_query.first()
    if not new_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id:{id} was not found.")
    updated_post = post_query.update(post.dict(),synchronize_session=False)
    if new_post.owner_id != current_user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"The current action is forbidden")
    db.commit()
    return post_query.first()

