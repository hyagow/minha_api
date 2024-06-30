from typing import List
from minhaapi.models.item import Item
from minhaapi.db.connection import db

class ItemController:
  async def get_items(self) -> List[Item]:
    query = "SELECT id, name, description FROM items"
    return await db.fetch(query)
  
  async def get_item_by_id(self, item_id: int) -> Item:
    query = "SELECT id, name, description FROM items WHERE id = $1"
    return await db.fetchrow(query, item_id)
  
  async def create_item(self, item) -> Item:
    query = "INSERT INTO items (name, description) VALUES ($1, $2) RETURNING id, name, description"
    return await db.fetchrow(query, item.name, item.description)
  
  async def update_item(self, item_id: int, item: Item) -> Item:
    query = "UPDATE items SET name = $1, description = $2 WHERE id = $3 RETURNING id, name, description"
    return await db.fetchrow(query, item.name, item.description, item_id)
  
  async def delete_item(self, item_id: int) -> None:
    query = "DELETE FROM items WHERE id = $1"
    await db.execute(query, item_id)
