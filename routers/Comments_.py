from fastapi import FastAPI, status,HTTPException , APIRouter,Depends
import  models,schema
from schema import *
from database import SessionLocal
from database import db
from typing import Optional,List 
from passlib.context import CryptContext
from routers import Comments_ ,oauth2


router=APIRouter(tags=['Comments'])
@router.get('/comments',response_model=List[ShowComments],status_code=200)
def get_all_comment(current_user:schema.User=Depends(oauth2.get_current_user)):
    comments=db.query(models.Comments).all()
    return comments
        
@router.get('/comment/{comment_id}',response_model=ShowComments)
def get_an_comment(comment_id:int,current_user:schema.User=Depends(oauth2.get_current_user)):
    comment=db.query(models.Comments).filter(models.Comments.comment_id==comment_id).first()
    return comment
            
@router.post('/comment',response_model=ShowComments,status_code=status.HTTP_201_CREATED)
def create_an_comment(comment:create_comment,current_user=Depends(oauth2.get_current_user)):
            new_comment=models.Comments(    
            post_id= comment.post_id,
            comment_description= comment.comment_description,
            comment_by = current_user.get("sub")
            )         
            db.add(new_comment)
            db.commit()
            return new_comment


# #for deleting commen
# @router.delete('/comment/{comment_id}')
# def delete_comment(comment_id:int,current_user:schema.User=Depends(oauth2.get_current_user)):
#     comment_to_delete=db.query(models.Comments).filter(models.Comments.comment_id == comment_id, models.Comments.comment_id == current_user.get("sub")).first()
    
#     if not comment_to_delete:
#                  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Not deleted")
    
#     db.delete(comment_to_delete)
#     db.commit()
#     db.refresh(comment_to_delete)

#     return comment_to_delete

#for deleting comments 
@router.delete('/comment/{comment_id}')
def delete_comment(comment_id:int,current_user:schema.User=Depends(oauth2.get_current_user)):
    comment_to_delete=db.query(models.Comments).filter(models.Comments.comment_id == comment_id, models.Comments.comment_by == current_user.get("sub")).first()
    # comment_to_delete=db.query(models.Comment).filter(models.Comment.comment_id==comment_id).first()
    if not comment_to_delete:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not your comment, so you can't delete it")
   
    db.delete(comment_to_delete)
    db.commit()

    db.refresh(comment_to_delete)