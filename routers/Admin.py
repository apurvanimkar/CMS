import sys
sys.path.append("..")
from typing import List
from fastapi import APIRouter,status,HTTPException,Depends
from database import db
from schema import*
import models,schema
from routers import Admin ,oauth2
router=APIRouter(tags=['Admin'])

#API for Admin

@router.put('/role/{username}',response_model=RoleR,status_code=status.HTTP_200_OK)
def update_an_user(username:str,user:RoleAssign,current_user:schema.User=Depends(oauth2.get_current_user)):
            user_to_update=db.query(models.User).filter(models.User.username==username).first()

            user_to_update.role=user.role
            db.commit()
            return user_to_update


@router.put('/feature/{post_id}',response_model=featureRes,status_code=status.HTTP_200_OK) #admin side apdation of feature of post
def update_an_user(post_id:int,post:featureUpdate,current_user:schema.User=Depends(oauth2.get_current_user)):
            post_to_update=db.query(models.Post).filter(models.Post.post_id==post_id).first() 
    
            post_to_update.is_featured = post.is_featured
            
            db.commit()
            return post_to_update


# return user_to_update
@router.get('/featured_post',response_model=List[featureRes],status_code=status.HTTP_202_ACCEPTED)
def add_to_homepage(current_user:schema.User=Depends(oauth2.get_current_user)):
           _featured_post=db.query(models.Post).filter(models.Post.is_featured==True).all()
           return _featured_post