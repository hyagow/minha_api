from typing import List
from minhaapi.models.user import User
from minhaapi.data.connection import database

class UserController:
  async def get_user(self) -> List[User]:
    query = "SELECT id, username, email FROM users"
    return await database.fetch(query)
  
  async def get_user_by_id(self, user_id: int) -> User:
    query = "SELECT id, username, email FROM users WHERE id = $1"
    return await database.fetch(query, user_id)
  
  async def create_user(self, user) -> User:
    query = "INSERT INTO users (username, email) VALUES ($1, $2) RETURNING id, username, email"
    return await database.fetchrow(query, user.username, user.email)
  
  async def update_user(self, user_id: int, user: User) -> User:
    query = "UPDATE users SET username = $1, email = $2 WHERE id = $3 RETURNING id, username, email"
    return await database.fetchrow(query, user.username, user.email, user_id)
  
  async def delete_user(self, user_id: int) -> None:
    query = "DELETE FROM users WHERE id = $1"
    await database.execute(query, user_id)