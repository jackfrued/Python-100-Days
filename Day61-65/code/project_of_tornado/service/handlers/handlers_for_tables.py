import json

import aiomysql
import tornado


class EmpHandler(tornado.web.RequestHandler):

    async def get(self, *args, **kwargs):
        async with self.settings['mysql'].cursor(aiomysql.DictCursor) as cursor:
            await cursor.execute("select eno as no, ename as name, job, sal, intro from tb_emp")
            emps = list(await cursor.fetchall())
            self.finish(json.dumps(emps))
