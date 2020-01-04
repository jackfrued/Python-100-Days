"""
example04.py - 同步请求的例子
"""
import json
import os

import requests
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

    def get(self):
        resp = requests.get(f'{REQ_URL}?key={API_KEY}')
        newslist = json.loads(resp.text)['newslist']
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
