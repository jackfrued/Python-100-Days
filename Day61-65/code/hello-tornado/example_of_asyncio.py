import asyncio


async def fetch(host):
    """从指定的站点抓取信息(协程函数)"""
    print(f'Start fetching {host}\n')
    # 跟服务器建立连接
    reader, writer = await asyncio.open_connection(host, 80)
    # 构造请求行和请求头
    writer.write(b'GET / HTTP/1.1\r\n')
    writer.write(f'Host: {host}\r\n'.encode())
    writer.write(b'\r\n')
    # 清空缓存区(发送请求)
    await writer.drain()
    # 接收服务器的响应(读取响应行和响应头)
    line = await reader.readline()
    while line != b'\r\n':
        print(line.decode().rstrip())
        line = await reader.readline()
    print('\n')
    writer.close()


def main():
    """主函数"""
    urls = ('www.sohu.com', 'www.douban.com', 'www.163.com')
    # 获取系统默认的事件循环
    loop = asyncio.get_event_loop()
    # 用生成式语法构造一个包含多个协程对象的列表
    tasks = [fetch(url) for url in urls]
    # 通过asyncio模块的wait函数将协程列表包装成Task（Future子类）并等待其执行完成
    # 通过事件循环的run_until_complete方法运行任务直到Future完成并返回它的结果
    futures = asyncio.wait(tasks)
    print(futures, type(futures))
    loop.run_until_complete(futures)
    loop.close()


if __name__ == '__main__':
    main()
