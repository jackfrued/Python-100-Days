import asyncio
import aiohttp


async def download(url):
    print('Fetch:', url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(url, '--->', resp.status)
            print(url, '--->', resp.cookies)
            print('\n\n', await resp.text())


def main():
    loop = asyncio.get_event_loop()
    urls = [
        'https://www.baidu.com',
        'http://www.sohu.com/',
        'http://www.sina.com.cn/',
        'https://www.taobao.com/',
        'https://www.jd.com/'
    ]
    tasks = [download(url) for url in urls]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


if __name__ == '__main__':
    main()
