from fastapi import FastAPI, status,HTTPException , APIRouter,Depends
import  models ,schema 
from schema import *
from database import SessionLocal
from database import db
from typing import Optional,List 
from passlib.context import CryptContext
from routers import Post_ ,oauth2

router=APIRouter(tags=['post'])
@router.get('/posts',response_model=List[ShowPost],status_code=200)
def get_all_post(current_user:schema.User=Depends(oauth2.get_current_user)):
    posts=db.query(models.Post).all()
    return posts
        
@router.get('/post/{post_id}',response_model=ShowPost)
def get_an_post(post_id:int,current_user:schema.User=Depends(oauth2.get_current_user)):
      posts=db.query(models.Post).filter(models.Post.post_id==post_id).first()
      return posts
            
@router.post('/post',response_model=ShowPost,status_code=status.HTTP_201_CREATED)
def create_an_post(p:createpost,current_user=Depends(oauth2.get_current_user)):             
             new_Post=models.Post(
            
             post_title = p.post_title,
             post_description = p.post_description,
             posted_on = p.posted_on,
             post_category=p.post_category,
             posted_by_user=current_user.get("id"),
             is_published=p.is_published
             
  )
            
             db.add(new_Post)
             db.commit()
             return new_Post
        
# @router.put('/post/{post_id}',response_model=Post,status_code=status.HTTP_200_OK)
# def update_an_post(post_id:int,post:PostUpdate,current_user:schema.User=Depends(oauth2.get_current_user)):
#              post_to_update = db.query(models.Post).filter(models.Post.post_id == current_user.get("sub")).first()
#              post_to_update.post_title = post.post_title,
#              post_to_update.post_description = post.post_description,
#              post_to_update.posted_on = post.posted_on,
#              post_to_update.is_published=post.is_published
#              db.commit()
#              db.refresh(post_to_update)
#              return post_to_update


@router.put('/post/{post_id}',response_model=Post,status_code=status.HTTP_200_OK)
def update_an_post(post_id:int,post:Post,current_user:schema.User=Depends(oauth2.get_current_user)):    
            post_to_update=db.query(models.Post).filter(models.Post.post_id == post_id, models.Post.posted_by_user == current_user.get("id")).first()  
            if not post_to_update:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not accessible for other's post")
            post_to_update.post_title = post.post_title,
            post_to_update.post_description = post.post_description,
            post_to_update.posted_on = post.posted_on,
            post_to_update.is_published=post.is_published
            
            db.commit()
            return post_to_update

@router.delete('/post/{post_id}')
def delete_user(post_id:int,current_user:schema.User=Depends(oauth2.get_current_user)):
     post_to_delete=db.query(models.Post).filter(models.Post.post_id == post_id, models.Post.posted_by_user == current_user.get("id")).first()

     if post_to_delete is None:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User Not Found")
    
     db.delete(post_to_delete)
     db.commit()
     db.refresh(post_to_delete)
    
     return post_to_delete
