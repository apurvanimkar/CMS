from fastapi import FastAPI, status,HTTPException,APIRouter,Depends
from schema import Login
from database import db
from passlib.context import CryptContext
from routers.Users_ import hashingP
import models
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from routers import Token 
router=APIRouter(tags=['Authentication'])


def check_password(hashed_password, plain_password):
    return hashingP.verify(plain_password, hashed_password)


@router.post('/login')
#def login(login:Login):
def login(login:OAuth2PasswordRequestForm= Depends()):
        user=db.query(models.User).filter(models.User.username==login.username).first() 
        if not user:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalid Credentials")
        
        if not check_password(user.password, login.password):
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Incorrect Password")
        

        access_token = Token.create_access_token(data={"sub": user.username,"id": user.id} )
        return {"access_token": access_token, "token_type": "bearer"}