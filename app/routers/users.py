from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import UserCreate, UserOut
from app.models.users import User
from app.security import hash_password
from sqlalchemy.orm import Session
from app.database import Base, get_db
from app.security import get_current_user



router = APIRouter()

@router.post("/users/" ,response_model=UserOut, status_code=201)
async def create_user(user: UserCreate, db:Session = Depends(get_db)):

    #Si l'utilisateur existe ou non
    utilisateur_existant = db.query(User).filter(User.email == user.email).first()
    if utilisateur_existant:
        raise HTTPException(status_code=400,detail="Email déja utilisé")

    hashed_password = hash_password(user.password)
    nouvel_utilisateur = User(email=user.email, hashed_password=hashed_password)
    db.add(nouvel_utilisateur)
    db.commit()
    db.refresh(nouvel_utilisateur)
    return nouvel_utilisateur


@router.get("/users/me", response_model=UserOut)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user