#web server
from aiohttp import web

#view
async def index(request):
    return web.Response(text="hello aiohttp")


#routes
def setup_routes(app):
    app.router.add_get('/',index)


#app
app=web.Application()
setup_routes(app)
web.run_app(app,host='127.0.0.1',port=8080)

#官方文档
#https://github.com/HuberTRoy/aiohttp-chinese-documentation