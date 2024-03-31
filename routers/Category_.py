from fastapi import FastAPI, status,HTTPException ,APIRouter,Depends
import models,schema 
from schema import *
from database import SessionLocal
from database import db
from typing import Optional,List 
from passlib.context import CryptContext
from routers import Category_ ,oauth2

router=APIRouter(tags=['Category'])
@router.get('/category',response_model=List[Category],status_code=200)
def get_all_category(current_user:schema.User=Depends(oauth2.get_current_user)):
    categories=db.query(models.Category).all()
    return categories

#get specific item

@router.get('/category/{id}',response_model=Category)
def get_an_category(id:int,current_user:schema.User=Depends(oauth2.get_current_user)):
     category=db.query(models.Category).filter(models.Category.id==id).first()
     return category

#get searching item

@router.get('/search/{id}',response_model=Category)
def get_an_category(id:int,current_user:schema.User=Depends(oauth2.get_current_user)):
     category=db.query(models.Category).filter(models.Category.id==id).first()
     return category

# #add items to database
@router.post('/category',response_model=Category,status_code=status.HTTP_200_OK)
def create_an_category(category:CreateCategory,current_user:schema.User=Depends(oauth2.get_current_user)):
       new_category=models.Category(
       
       category_name=category.category_name   
  )
       
       db.add(new_category)
       db.commit()
       return new_category


@router.put('/category/{id}',response_model=Category,status_code=status.HTTP_200_OK)
def update_an_category(id:int,c:CreateCategory,current_user:schema.User=Depends(oauth2.get_current_user)):
             c_to_update = db.query(models.Category).filter(models.Category.id == id).first()
             c_to_update.category_name = c.category_name,
             
             db.commit()
             db.refresh(c_to_update)
             return c_to_update
