from pydantic import BaseModel # type: ignore

class Item(BaseModel):
  id: int
  name: str
  description: str
