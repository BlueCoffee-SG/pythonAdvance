import aiohttp
import asyncio

url="http://httpbin.org/get" 

async def fetch(client,url):
    # get 方式请求url
    async with client.get(url) as resp:
        assert resp.status==200
        return await resp.text()
    

async def main():
    # 获取session对象
    async with aiohttp.ClientSession() as client:
        html=await fetch(client,url)   # await 去做其它事情，做异步，等返回再做fetch

loop=asyncio.get_event_loop()
task=loop.create_task(main())
loop.run_until_complete(task)

# zero-sleep 让底层连接得到关闭的缓冲时间
loop.run_until_complete(asyncio.sleep(0))
loop.close()