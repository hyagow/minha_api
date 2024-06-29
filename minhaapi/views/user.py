# type: ignore
from fastapi import APIRouter, HTTPException
from typing import List
from minhaapi.models.user import User
from minhaapi.controllers.user_controller import UserController

router = APIRouter()
controller = UserController()

@router.get("/users/", response_model=List[User])
async def read_users():
  return await controller.get_users()

@router.get("/users/{user_id}", response_model=User)
async def read_user_by_id(user_id: int):
  user = await controller.get_user_by_id(user_id)
  if user is None:
    raise HTTPException(status_code=404, detail="User not found")
  
@router.post("/users/", response_model=User)
async def create_user(user: User):
  return await controller.create_user(user)

@router.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, user: User):
  return controller.update_user(user_id, user)

@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
  await controller.delete_user(user_id)
  return {"message": "User deleted successfully"}