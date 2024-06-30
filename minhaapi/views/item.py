# type: ignore
from typing import List
from fastapi import APIRouter, HTTPException
from minhaapi.controllers.item_controller import ItemController
from minhaapi.models.item import Item

router = APIRouter()
controller = ItemController()

@router.get("/items/", response_model=List[Item])
async def read_items():
  return await controller.get_items()

@router.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
  item = await controller.get_item_by_id(item_id)
  if item is None:
    raise HTTPException(status_code=404, detail="Item not found")
  
@router.post("/items/", response_model=Item)
async def create_item(item: Item):
  return await controller.create_item(item)

@router.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
  return await controller.update_item(item_id, item)

@router.delete("/items/{item_id}")
async def delete_item(item_id: int):
  await controller.delete_item(item_id)
  return {"message": "Item deleted successfully"}
