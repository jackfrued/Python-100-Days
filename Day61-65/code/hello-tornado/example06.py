"""
example06.py - 异步操作MySQL
"""
import json

import aiomysql
import tornado
import tornado.web

from tornado.ioloop import IOLoop
from tornado.options import define, parse_command_line, options

define('port', default=8888, type=int)


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


class HomeHandler(tornado.web.RequestHandler):

    async def get(self, no):
        async with self.settings['mysql'].cursor(aiomysql.DictCursor) as cursor:
            await cursor.execute("select * from tb_dept where dno=%s", (no, ))
            if cursor.rowcount == 0:
                self.finish(json.dumps({
                    'code': 20001,
                    'mesg': f'没有编号为{no}的部门'
                }))
                return
            row = await cursor.fetchone()
            self.finish(json.dumps(row))

    async def post(self, *args, **kwargs):
        no = self.get_argument('no')
        name = self.get_argument('name')
        loc = self.get_argument('loc')
        conn = self.settings['mysql']
        try:
            async with conn.cursor() as cursor:
                await cursor.execute('insert into tb_dept values (%s, %s, %s)',
                                     (no, name, loc))
            await conn.commit()
        except aiomysql.MySQLError:
            self.finish(json.dumps({
                'code': 20002,
                'mesg': '添加部门失败请确认部门信息'
            }))
        else:
            self.set_status(201)
            self.finish()


def make_app(config):
    return tornado.web.Application(
        handlers=[(r'/api/depts/(.*)', HomeHandler), ],
        **config
    )


def main():
    parse_command_line()
    app = make_app({
        'debug': True,
        'mysql': IOLoop.current().run_sync(connect_mysql)
    })
    app.listen(options.port)
    IOLoop.current().start()


if __name__ == '__main__':
    main()
