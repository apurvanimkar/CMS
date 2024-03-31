
from fastapi import FastAPI,status,HTTPException
from routers import Users_ ,Post_,Category_,Authentication,Comments_,Reset_Password,Admin,media


app=FastAPI()
app.include_router(Users_.router)
app.include_router(Post_.router)
app.include_router(Category_.router)
app.include_router(Authentication.router)
app.include_router(Comments_.router)
app.include_router(Reset_Password.router)
app.include_router(Admin.router)
app.include_router(media.router)
































# db=SessionLocal()

# @app.get('/media',response_model=List[schema.Media_Library],status_code=200)
# def get_all_media():
#     medias=db.query(models.Media_Library).all()
#     return medias
        
# @app.get('/media/{media_id}',response_model=schema.Media_Library)
# def get_an_media(media_id:int):
#     media=db.query(models.Media_Library).filter(models.Media_Library.id==media_id).first()
#     return media
            
# @app.post('/media',response_model=schema.Media_Library,status_code=status.HTTP_201_CREATED)
# def create_an_user(media:Media_Library):
#             new_media=models.Media_Library(
#             id=media.id,
#             user=media.user,
#             link_to_media=media.link_to_media

                  
#  )
#             db_media=db.query(models.Media_Library).filter(models.Media_Library.id==new_media.id).first()
#             if db_media is not None:
#                 raise HTTPException(status_code=400,details="you have already account")
#             db.add(new_media)
#             db.commit()
#             return new_media
        
# @app.put('/media/{media_id}',response_model=schema.Media_Library,status_code=status.HTTP_200_OK)
# def update_an_media(media_id:int,media:Media_Library):
#             media_to_update=db.query(models.Media_Library).filter(models.Media_Library.id==media_id).first()
    
#             media_to_update.id=media.id
#             media_to_update.user=media.user
#             media_to_update.link_to_media=media.link_to_media
           
#             db.commit()
#             return media_to_update

# @app.delete('/media/{media_id}')
# def delete_media(media_id:int):
#     media_to_delete=db.query(models.Media_Library).filter(models.Media_Library.id==media_id).first()

#     if media_to_delete is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User Not Found")
    
#     db.delete(media_to_delete)
#     db.commit()
#     db.refresh(media_to_delete)
    
#     return media_to_delete
# #-----------------------------------------------------------------

        
