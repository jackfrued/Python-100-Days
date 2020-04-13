"""
backend_server.py - 后台服务器
"""
import asyncio
import os
import threading

import aiomysql
import tornado.web

from tornado.ioloop import IOLoop
from tornado.platform.asyncio import AnyThreadEventLoopPolicy

from service.handlers.handlers_for_charts import send_data
from service.handlers.handlers_for_nav import IndexHandler
from service.handlers.handlers_for_tables import EmpHandler
from service.handlers.handlers_for_charts import ChartHandler


async def connect_mysql():
    return await aiomysql.connect(
        host='1.2.3.4',
        port=3306,
        db='hrs',
        charset='utf8',
        use_unicode=True,
        user='yourname',
        password='yourpass',
    )


def main():
    # Tornado 5开始使用线程必须指定事件循环的策略否则无法启动线程
    asyncio.set_event_loop_policy(AnyThreadEventLoopPolicy())
    # 启动通过WebSocket长连接发送数据的线程
    threading.Thread(target=send_data, daemon=True, args=(5, )).start()
    app = tornado.web.Application(
        handlers=[
            (r'/', IndexHandler),
            (r'/api/emps', EmpHandler),
            (r'/ws/charts', ChartHandler),
        ],
        template_path=os.path.join(os.path.dirname(__file__), 'templates'),
        static_path=os.path.join(os.path.dirname(__file__), 'assets'),
        cookie_secret='MWM2MzEyOWFlOWRiOWM2MGMzZThhYTk0ZDNlMDA0OTU=',
        mysql=IOLoop.current().run_sync(connect_mysql),
        debug=True
    )
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
