from fastapi import APIRouter, Depends
from typing import List
from repositories.users import UserRepository
from models.user import User, UserIn
from .depends import get_user_repository

router = APIRouter()

@router.get("/", response_mode=List[User])
async def read_users(
	users: UserRepository = Depends(get_user_repository),
	limit: int = 100, 
	skip: int = 100):
	return await users.get_all(limit=limit, skip=0)

@router.post("/", response_mode=User)
async def create(user=UserIn, users: UserRepository = Depends(get_user_repository)):
	return await users.create(u=user)

@router.put("/", response_mode=User)
async def create(id: int, user: UserIn, users: UserRepository = Depends(get_user_repository)):
	return await users.update(id=id, u=user)