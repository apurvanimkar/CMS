from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel
from typing import Optional,List,Text

#--------------------------USER SCHEMAS---------------
class User(BaseModel): #serializer
    id:int
    name:str
    username:str
    Mobile_num:int
    email_id:str
    profile_photo:int
    bio:str
    #password:str
    #role:str
   
    
    class Config:
        orm_mode=True

class NewUserUpdate(BaseModel): #serializer
   
    name:str
    username:str
    email_id:str
    profile_photo:int
   
    #password:str
    #role:str
   
    
    class Config:
        orm_mode=True
#---------------------------
class RoleAssign(BaseModel):
      
      role:str

      class Config:
        orm_mode=True

class RoleR(BaseModel):
    name:str
    username:str
    Mobile_num:int
    email_id:str
    #password:str
    role:str
    profile_photo:int
    bio:str

    class Config:
        orm_mode=True


#---------------------------
class ShowUser(BaseModel):
    id:int
    username:str
    email_id:str
    posts:List
  
    class Config:
        orm_mode=True


class ShowUserR(BaseModel):
    id:int
    username:str
    email_id:str
    
     
    class Config:
        orm_mode=True
 #-----------------------------
class CreateUser(BaseModel):
    name: str
    username: str
    Mobile_num:int
    email_id: str
    password: str
    profile_photo: Optional[int] = None
    bio: Optional[str] = None
    class Config:
        orm_mode = True

 #-----------------------------
class UpdateUser(BaseModel):
    #name: str
    username: str
    Mobile_num:int
    email_id: str
    #password: str
    
    class Config:
        orm_mode = True

#-----------------------------POST SCHEMAS-------------------------
class Post(BaseModel): #serializer
     post_id:int
     post_title:str
     post_description:str
     posted_on:str
     is_published:bool
     #is_featured:bool
     post_category:str
     #media_id:int

     class Config:
         orm_mode=True

class ShowCategory(BaseModel):
    
    id:int
    category_name:str
    class Config:
         orm_mode=True

class ShowComment_by(BaseModel):
    post_id:int 
    post_title:str
    posted_on:str
    
    class Config:
         orm_mode=True 
           

class ShowComments(BaseModel): 
    post_id:int
    comment_id:int
    comment_description:str
    c_posts:ShowComment_by
    class Config:
         orm_mode=True


    
class Posted_by(BaseModel):
    
    comment_description:str
    comment_by:str
    class Config:
          orm_mode=True


class ShowPost(BaseModel): #serializer
    post_id:int
    posted_by_user:int 
    post_title:str
    post_description:str
    posted_on:str
    is_published:bool
    creator:ShowUserR
    category_id:ShowCategory
    comment_id_:List[Posted_by]
    #comment_id_:ShowComments
    class Config:
         orm_mode = True

class createpost(BaseModel): #serializer
    post_title:str
    post_description:str
    posted_on:str
    post_category:int
    is_published:bool
    posted_by_user:int
    

    class Config:
         orm_mode = True

class PostUpdate(BaseModel): #serializer
    post_title:str
    post_description:str
    posted_on:str
    is_published:bool

    class Config:
        orm_mode=True
#--------------------------------CATEGORY-----------------------------
class Category(BaseModel):
    id:int
    category_name:str
    posts:List
    
    class Config:
        orm_mode=True

class CreateCategory(BaseModel):
    
    category_name:str

    class Config:
        orm_mode=True


 #-------------------------------
class featureUpdate(BaseModel):
     
     is_featured:bool

     class Config:
         orm_mode=True

class featureRes(BaseModel): #serializer
     post_id:int
     post_title:str
     post_description:str
     posted_by_user:int
     posted_on:str
     is_featured:bool
     class Config:
         orm_mode=True

class All_feature_Update(BaseModel):
     
     is_featured:bool

     class Config:
         orm_mode=True

#-------------------------------
class Login(BaseModel):  #serializer
   
    username: str 
    password: str 
    
    class Config:
       orm_mode=True

#-------------------------------
class Comments(BaseModel):  #serializer
    comment_id: int 
    post_id: int
    comment_description:str
    comment_by: str
    c_posts:List

    class Config:
        orm_mode=True
#-------------------------------
class create_comment(BaseModel):  #serializer
    
    post_id: int
    comment_description:str
    comment_by: str

    class Config:
        orm_mode=True
#-------------------------------

class Token(BaseModel):
    access_token:str
    token_type:str

    class Config:
        orm_mode=True
#-------------------------------

class TokenData(BaseModel):
    email_id:Optional[str]=None

#-------------------------------
class ResetPassword(BaseModel):
    email_id:str

    class Config:
        orm_mode=True

class Update_pass(BaseModel):
    
    password:str
     
    class Config:
        orm_mode = True

#========================
class Media_library(BaseModel):
    
    #id:str
    url_link:str
     
    class Config:
        orm_mode = True
#========================
class show_media(BaseModel):
    
    user_media:List
     
    class Config:
        orm_mode = True