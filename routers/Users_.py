from fastapi import FastAPI, status,HTTPException , APIRouter,Depends
import models,schema 
from schema import *
from database import SessionLocal
from database import db
from typing import Optional,List 
from passlib.context import CryptContext
from routers import Users_,oauth2


router=APIRouter(tags=['Users'])
@router.get('/users',response_model=List[ShowUser],status_code=200)
def get_all_users(current_user:schema.User=Depends(oauth2.get_current_user)):
    users=db.query(models.User).all()
    return users
        
@router.get('/user/{username}',response_model=ShowUser)
def get_an_user(username:str,current_user:schema.User=Depends(oauth2.get_current_user)):
    user=db.query(models.User).filter(models.User.username==username).first()
    return user


hashingP= CryptContext(schemes=["bcrypt"], deprecated="auto")
@router.post('/user',response_model=ShowUser,status_code=status.HTTP_201_CREATED)
def create_an_user(user:CreateUser):
            C_hash=hashingP.hash(user.password)
            new_user=models.User(
            name=user.name,
            username=user.username,
            Mobile_num=user.Mobile_num,
            email_id=user.email_id,
            password=C_hash,
            profile_photo=user.profile_photo,
            bio=user.bio      
 )
            
            db.add(new_user)
            db.commit()
            return new_user
        
@router.put('/user',response_model=User,status_code=status.HTTP_200_OK)
def update_an_user(user:UpdateUser,current_user:schema.User=Depends(oauth2.get_current_user)):
            user_to_update=db.query(models.User).filter(models.User.username==current_user.get("sub")).first()
           # user_to_update.name=user.name,
            user_to_update.username=user.username,
            user_to_update.Mobile_num=user.Mobile_num,
            user_to_update.email_id=user.email_id
           
            db.commit()
            return user_to_update


# @router.put('/user/{username}',response_model=User,status_code=status.HTTP_200_OK)
# def update_an_user(username:str,user:UpdateUser,current_user:schema.User=Depends(oauth2.get_current_user)):
#             user_to_update=db.query(models.User).filter(models.User.username==username).first()
#             user_to_update.username=user.username,
#             user_to_update.Mobile_num=user.Mobile_num,
#             user_to_update.email_id=user.email_id
            
#             db.commit()
#             return user_to_update

@router.delete('/user')
def delete_user(User=Depends(oauth2.get_current_user)):
    user_to_delete=db.query(models.User).filter(models.User.username==User.get("sub")).first()

    if user_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User Not Found")
    
    db.delete(user_to_delete)
    db.commit()
    db.refresh(user_to_delete)
    
    return user_to_delete

