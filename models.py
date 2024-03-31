from database import Base
from sqlalchemy import String,Boolean,Integer,Column,Text,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils import URLType

class User(Base):
        
        __tablename__='users'
        id=Column(Integer,primary_key=True,index=True)
        name=Column(String(255),nullable=False)
        #username=Column(Text)
        username=Column(String(255),nullable=False)
        Mobile_num=Column(Integer,nullable=False)
        email_id=Column(Text)
        password=Column(Text,nullable=False)
        role=Column(String,default="author")
        profile_photo=Column(Integer,nullable=False)
        bio=Column(String(255),nullable=False)

        posts = relationship("Post", back_populates="creator")
        media_user= relationship("Media_Library", back_populates="user_media")
       
    
class Post(Base):
    
         __tablename__='PostDetails'
         post_id=Column(Integer,primary_key=True,index=True)
         post_title=Column(String(255),nullable=False)
         post_description=Column(String(255),nullable=False)
         posted_on=Column(String(255),nullable=True)
         is_featured=Column(Boolean,default=False)
         is_published=Column(Boolean,default=True)
         
         posted_by_user=Column(Integer,ForeignKey('users.id'))
         creator = relationship("User", back_populates="posts")

         post_category = Column(Integer,ForeignKey("categoryt.id"))
         category_id= relationship("Category", back_populates="posts")

        
         comment_id_= relationship("Comments", back_populates="c_posts")
         
#for class category
class Category(Base):

         __tablename__='categoryt'
         id=Column(Integer,primary_key=True,unique=True)
         category_name=Column(String(255),nullable=False)

         posts = relationship("Post", back_populates="category_id")

         
#for class Comments
class Comments(Base):
        __tablename__='Comments'
        comment_id=Column(Integer,primary_key=True,unique=True)
        post_id=Column(Integer,ForeignKey("PostDetails.post_id"))
        comment_description=Column(String(255),nullable=False)
        comment_by=Column(String(255),nullable=False)

        c_posts = relationship("Post", back_populates="comment_id_")



class Media_Library(Base):
    
        __tablename__='Media_Libraries'
        id=Column(Integer,primary_key=True,index=True)
        user = Column(Integer, ForeignKey("users.id"))
        url_link = Column(URLType)       
        
        user_media = relationship("User", back_populates="media_user")
        