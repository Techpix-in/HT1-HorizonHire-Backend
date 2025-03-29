import os
from dotenv import load_dotenv
import redis.asyncio as redis
import json

load_dotenv()

class Redis:
    def __init__(self):
        """Initialize Redis connection"""
        self.REDIS_CONNECTION_URL = os.getenv('REDIS_CONNECTION_URL')
        self.connection = None

    async def create_connection(self):
        self.connection = redis.from_url(self.REDIS_CONNECTION_URL, db=0)


    async def set(self, key, value):
        if not self.connection:
            await self.create_connection()
        await self.connection.set(key, json.dumps(value))

    async def get(self, key):
        if not self.connection:
            await self.create_connection()
        data = await self.connection.get(key)
        return json.loads(data) if data else None


# async def test_redis():
#     redis_instance = Redis()
#     connection = await redis_instance.create_connection()
#     await connection.set('foo', 'bar')
#     result = await connection.get('foo')
#     print(result)  # Should print 'bar'

# import asyncio
# asyncio.run(test_redis())
