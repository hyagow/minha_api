from pydantic import BaseModel # type: ignore

class User(BaseModel):
  id: int
  username: str
  email: str

  class Config:
    orm_model = True