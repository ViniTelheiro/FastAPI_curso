from fastapi import APIRouter, Depends, HTTPException, Path
from starlette import status
from sqlalchemy.orm import Session
from database import SessionLocal
from typing import Annotated
from models import Todos, TodosRequest, Users
from .auth import get_current_user, bcrypt_context
from pydantic import BaseModel, Field

router = APIRouter(
    prefix='/users',
    tags=['users']
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]


class PasswordRequest(BaseModel):
    password: str = Field(min_length=3)





@router.get('/', status_code=status.HTTP_200_OK)
async def get_user(user:user_dependency, db:db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed.')
    
    user_data = db.query(Users).filter(Users.id == user.get('id')).first()
    show = {
        'id': user_data.id,
        'email': user_data.email,
        'username': user_data.username,
        'first_name': user_data.first_name,
        'last_name': user_data.last_name,
        'is_active': user_data.is_active,
        'role': user_data.role
    }
    return show

@router.put('/change_password/', status_code=status.HTTP_204_NO_CONTENT)
async def update_password(user: user_dependency, db:db_dependency, password:PasswordRequest):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed.')
    
    user_data = db.query(Users).filter(Users.id == user.get('id')).first()
    new_password = bcrypt_context.hash(password.password)
    if new_password == user_data.hashed_password:
        return "The new password is equal to the old password!"
    user_data.hashed_password = new_password
    db.add(user_data)
    db.commit()
    