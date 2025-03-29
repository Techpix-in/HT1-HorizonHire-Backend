# from config import Redis

class Cache:
    def __init__(self, redis_client):
        self.redis_client = redis_client
    
    async def add_response_to_cache(self, token: str, message_data):
        await self.redis_client.set(
            str(token),message_data)
        
    async def get_response_history(self, token: str):
        
        data = await self.redis_client.get(str(token))
        
        return data

# data = {
#     "hello" :"there"
# }
# async def test_cache():
#     redis_client = Redis()
#     await redis_client.create_connection()
#     cache = Cache(redis_client)
#     await cache.add_response_to_cache(token="abc",message_data=data)

#     response = await cache.get_response_history(token="abc")
#     print(response)
    # await connection.set('foo', 'bar')
    # result = await connection.get('foo')
    # print(result)  # Should print 'bar'

# import asyncio
# asyncio.run(test_cache())
