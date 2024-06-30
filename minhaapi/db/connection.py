import asyncpg # type: ignore
from .settings import settings

class Database:
  def __init__(self):
    self.pool = None
  
  async def connect(self):
    self.pool = await asyncpg.create_pool(settings.database_url)

  async def disconnect(self):
    await self.pool.close()

  async def execute(self, query: str, *args):
    async with self.pool.acquire() as conn:
      return await conn.execute(query, *args)
    
  async def fetch(self, query: str, *args):
    async with self.pool.acquire() as conn:
      return await conn.fetch(query, *args)
    
  async def fetchrow(self, query: str, *args):
    async with self.pool.acquire() as conn:
      return await conn.fetchrow(query, *args)
    

db = Database()
