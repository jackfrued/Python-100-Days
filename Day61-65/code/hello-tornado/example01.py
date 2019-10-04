"""
example01.py - 五分钟上手Tornado
"""
import tornado.ioloop
import tornado.web

from tornado.options import define, options, parse_command_line

# 定义默认端口
define('port', default=8000, type=int)


class MainHandler(tornado.web.RequestHandler):
    """自定义请求处理器"""

    def get(self):
        # 向客户端（浏览器）写入内容
        self.write('<h1>Hello, world!</h1>')


def main():
    """主函数"""
    # 解析命令行参数，例如：
    # python example01.py --port 8888
    parse_command_line()
    # 创建了Tornado框架中Application类的实例并指定handlers参数
    # Application实例代表了我们的Web应用，handlers代表了路由解析
    app = tornado.web.Application(handlers=[(r'/', MainHandler), ])
    # 指定了监听HTTP请求的TCP端口（默认8000，也可以通过命令行参数指定）
    app.listen(options.port)
    # 获取Tornado框架的IOLoop实例并启动它（默认启动asyncio的事件循环）
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
