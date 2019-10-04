import tornado


class IndexHandler(tornado.web.RequestHandler):

    async def get(self, *args, **kwargs):
        return await self.render('index.html')
