from fastapi import status, HTTPException, APIRouter,Depends
from routers.Users_ import hashingP
from routers.Token import create_access_token,SECRET_KEY,ALGORITHM
from jose import jwt
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jwt import ExpiredSignatureError,InvalidSignatureError,exceptions
from database import db 
import models,schema
from schema import * 
from routers import Token 
from routers import Reset_Password ,oauth2

router=APIRouter(tags=['Reset_Password'])


@router.post('/Password',status_code=status.HTTP_201_CREATED)
def create_an_user(user:ResetPassword,current_user:schema.User=Depends(oauth2.get_current_user)):    
        db_user=db.query(models.User).filter(models.User.email_id==user.email_id).first()
      
        if not db_user:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"You are not a valid user")
       
        Token_reset = create_access_token(data={"email":db_user.email_id})
        
        # Set up the sender's email address and password
        sender_email = "apurva.nimkar.stpl.2023@gmail.com"
        sender_password = "viobicmmoieiqbqk"  
       
        # Set up the recipient's email address
        recipient_email = db_user.email_id

        # Create a message object
        message = MIMEMultipart()

        # Set the email subject
        message["Subject"] = "Mail for reset password"

        # Set the sender's email address
        message["From"] = sender_email

        # Set the recipient's email address
        message["To"] = recipient_email

        # Add a message body
        body = f"Token for password reset {Token_reset}" 
        message.attach(MIMEText(body, "plain"))

        # Create an SMTP object
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        smtp_connection = smtplib.SMTP(smtp_server, smtp_port)

        # Start the TLS encryption
        smtp_connection.starttls()

        # Login to the email server
        smtp_connection.login(sender_email, sender_password)

        # Send the email
        smtp_connection.sendmail(sender_email, recipient_email, message.as_string())

        # Close the SMTP connection
        smtp_connection.quit()    
        
        return 'please check mail for Token'

def token_verify(token:str,email:str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        emailid:str = payload.get("email")
        if emailid != email:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
   
    except exceptions.ExpiredSignatureError:
        raise HTTPException(status_code=400, detail="Signature has expired")


      
    
@router.post("/Update_password/{email_id}/{token_reset}")
def reset_password(email_id: str, token_reset: str, update: Update_pass):
    try:
        user = db.query(models.User).filter(models.User.email_id == email_id).first()
        token_verify(token_reset, email_id)    
        new_password = hashingP.hash(update.password)
        user.password = new_password
        db.commit()
        return {"message": "Password reset successfully"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=f"Invalid Token Or EMail: {str(e)}")
    
    
