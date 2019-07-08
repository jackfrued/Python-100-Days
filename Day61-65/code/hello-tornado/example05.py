"""
example05.py - 异步请求的例子
"""
import aiohttp
import json
import os

import tornado.gen
import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.httpclient
from tornado.options import define, options, parse_command_line

define('port', default=8888, type=int)

REQ_URL = 'http://api.tianapi.com/guonei/'
API_KEY = '772a81a51ae5c780251b1f98ea431b84'


class MainHandler(tornado.web.RequestHandler):
    """自定义请求处理器"""

    async def get(self):
        async with aiohttp.ClientSession() as session:
            resp = await session.get(f'{REQ_URL}?key={API_KEY}')
            json_str = await resp.text()
            print(json_str)
            newslist = json.loads(json_str)['newslist']
            self.render('news.html', newslist=newslist)


def main():
    """主函数"""
    parse_command_line()
    app = tornado.web.Application(
        handlers=[(r'/', MainHandler), ],
        template_path=os.path.join(os.path.dirname(__file__), 'templates'),
    )
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
