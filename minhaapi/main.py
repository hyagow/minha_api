# type: ignore
from fastapi import FastAPI
from minhaapi.db.connection import db
from minhaapi.db.settings import settings
from minhaapi.views import item, user

app = FastAPI()

@app.on_event("startup")
async def startup():
  await db.connect()
  print(f'Connected to database: {settings.database_url}')

@app.on_event("shutdown")
async def shutdown():
  await db.disconnect()


app.include_router(item.router, prefix="/api")
app.include_router(user.router, prefix="/api")

if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app, localhost="127.0.0.1", port=8000)