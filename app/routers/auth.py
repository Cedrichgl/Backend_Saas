from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.users import User
from jose import JWTError
from app.schemas.user import UserCreate, UserOut, TokenOut
from app.security import create_access_token, verify_password
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login", response_model=TokenOut)
def login(credentials:OAuth2PasswordRequestForm = Depends(), db:Session = Depends(get_db)):
    #cherche l'utilisateur par email
    user = db.query(User).filter(User.email == credentials.username).first()
    if not user or not verify_password(credentials.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Incorrect email or password")

    token = create_access_token(data={"sub": str(user.id)})

    return {"access_token": token, "token_type": "bearer"}


