import asyncio
import re

import aiohttp

PATTERN = re.compile(r'\<title\>(?P<title>.*)\<\/title\>')


async def show_title(url):
    async with aiohttp.ClientSession() as session:
        resp = await session.get(url, ssl=False)
        html = await resp.text()
        print(PATTERN.search(html).group('title'))


def main():
    urls = ('https://www.python.org/',
            'https://git-scm.com/',
            'https://www.jd.com/',
            'https://www.taobao.com/',
            'https://www.douban.com/')
    # asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    # 获取事件循环（）
    loop = asyncio.get_event_loop()
    tasks = [show_title(url) for url in urls]
    loop.run_until_complete(asyncio.wait(tasks))


if __name__ == '__main__':
    main()
