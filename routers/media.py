# from fastapi import FastAPI, status,HTTPException , APIRouter,Depends
# import  models ,schema 
# from schema import *
# from database import SessionLocal
# from database import db
# from typing import Optional,List 
# from passlib.context import CryptContext
# from routers import media ,oauth2


# router=APIRouter(tags=['Media_Library'])

from fastapi import APIRouter, File, UploadFile,status,Depends,HTTPException
import schema ,models
from schema import *
from database import db
from fastapi.responses import FileResponse
from routers import media ,oauth2
import os
import shutil
from routers import oauth2
import sqlalchemy
from sqlalchemy.exc import InvalidRequestError


router=APIRouter(tags=['Media Library'])


@router.post("/media_libraries",status_code=status.HTTP_201_CREATED)
async def upload_media(file: UploadFile = File(...),current_user:User = Depends(oauth2.get_current_user)):
    media_folder = "C:/Subhchintak/Projects/Content management/routers/media_folder"
    file_path = os.path.join(media_folder, file.filename)
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())
        new_media=models.Media_Library(
            #user=id,
            url_link=file.filename) 
        db.add(new_media)
        db.commit()
        db.refresh(new_media)
        return new_media

@router.get('/medias',status_code=status.HTTP_200_OK,response_model=List[Media_library])


def get_all_medias(current_user:schema.User=Depends(oauth2.get_current_user)):
   posts=db.query(models.Media_Library).all()           
   return posts
 
        
#get an media by Id 
@router.get('/media/{id}',response_model=Media_library)
def get_an_media_by_id(id:int,current_user:schema.User=Depends(oauth2.get_current_user)):
    post =db.query(models.Media_Library).filter(models.Media_Library.id == id).first()
    return post

# @router.delete('/media/{id}')
# def delete_an_media(id: int, current_user=Depends(oauth2.get_current_user)):
#     media_to_delete = db.query(models.Media_Library).filter(models.Media_Library.id == id).first()
#     if media_to_delete is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="u cannot delete others medias")
#     try:
#         db.query(models.Media_Library).filter(models.Media_Library.id == id).delete()
        
#         db.delete(media_to_delete)
#         db.commit()
#         db.refresh(media_to_delete)
#     except sqlalchemy.exc.InvalidRequestError:
#      raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail="media delete successfully")