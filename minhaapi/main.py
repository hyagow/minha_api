# type: ignore
from fastapi import FastAPI
from minhaapi.data.connection import database
from minhaapi.data.settings import settings
# from data.connection import database
# from data.settings import settings
from minhaapi.views import item, user

app = FastAPI()

@app.on_event("startup")
async def startup():
  await database.connect()
  print(f'Connected to database: {settings.database_url}')

@app.on_event("shutdown")
async def shutdown():
  await database.disconnect()


app.include_router(item.router, prefix="/api")
app.include_router(user.router, prefix="/api")