"""
example07.py - 将非异步的三方库封装为异步调用
"""
import asyncio
import concurrent
import json

import tornado
import tornado.web
import pymysql

from pymysql import connect
from pymysql.cursors import DictCursor

from tornado.ioloop import IOLoop
from tornado.options import define, parse_command_line, options
from tornado.platform.asyncio import AnyThreadEventLoopPolicy

define('port', default=8888, type=int)


def get_mysql_connection():
    return connect(
        host='1.2.3.4',
        port=3306,
        db='hrs',
        charset='utf8',
        use_unicode=True,
        user='yourname',
        password='yourpass',
    )


class HomeHandler(tornado.web.RequestHandler):
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=10)

    async def get(self, no):
        return await self._get(no)

    @tornado.concurrent.run_on_executor
    def _get(self, no):
        con = get_mysql_connection()
        try:
            with con.cursor(DictCursor) as cursor:
                cursor.execute("select * from tb_dept where dno=%s", (no, ))
                if cursor.rowcount == 0:
                    self.finish(json.dumps({
                        'code': 20001,
                        'mesg': f'没有编号为{no}的部门'
                    }))
                    return
                row = cursor.fetchone()
                self.finish(json.dumps(row))
        finally:
            con.close()

    async def post(self, *args, **kwargs):
        return await self._post(*args, **kwargs)

    @tornado.concurrent.run_on_executor
    def _post(self, *args, **kwargs):
        no = self.get_argument('no')
        name = self.get_argument('name')
        loc = self.get_argument('loc')
        conn = get_mysql_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute('insert into tb_dept values (%s, %s, %s)',
                               (no, name, loc))
            conn.commit()
        except pymysql.MySQLError:
            self.finish(json.dumps({
                'code': 20002,
                'mesg': '添加部门失败请确认部门信息'
            }))
        else:
            self.set_status(201)
            self.finish()


def main():
    asyncio.set_event_loop_policy(AnyThreadEventLoopPolicy())
    parse_command_line()
    app = tornado.web.Application(
        handlers=[(r'/api/depts/(.*)', HomeHandler), ]
    )
    app.listen(options.port)
    IOLoop.current().start()


if __name__ == '__main__':
    main()
