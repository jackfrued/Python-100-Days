import pickle
import zlib
from enum import Enum, unique
from hashlib import sha1
from random import random
from threading import Thread, current_thread, local
from time import sleep
from urllib.parse import urlparse

import pymongo
import redis
import requests
from bs4 import BeautifulSoup
from bson import Binary


@unique
class SpiderStatus(Enum):
    IDLE = 0
    WORKING = 1


def decode_page(page_bytes, charsets=('utf-8',)):
    page_html = None
    for charset in charsets:
        try:
            page_html = page_bytes.decode(charset)
            break
        except UnicodeDecodeError:
            pass
    return page_html


class Retry(object):

    def __init__(self, *, retry_times=3,
                 wait_secs=5, errors=(Exception, )):
        self.retry_times = retry_times
        self.wait_secs = wait_secs
        self.errors = errors

    def __call__(self, fn):

        def wrapper(*args, **kwargs):
            for _ in range(self.retry_times):
                try:
                    return fn(*args, **kwargs)
                except self.errors as e:
                    print(e)
                    sleep((random() + 1) * self.wait_secs)
            return None

        return wrapper


class Spider(object):

    def __init__(self):
        self.status = SpiderStatus.IDLE

    @Retry()
    def fetch(self, current_url, *, charsets=('utf-8', ),
              user_agent=None, proxies=None):
        thread_name = current_thread().name
        print(f'[{thread_name}]: {current_url}')
        headers = {'user-agent': user_agent} if user_agent else {}
        resp = requests.get(current_url,
                            headers=headers, proxies=proxies)
        return decode_page(resp.content, charsets) \
            if resp.status_code == 200 else None

    def parse(self, html_page, *, domain='m.sohu.com'):
        soup = BeautifulSoup(html_page, 'lxml')
        for a_tag in soup.body.select('a[href]'):
            parser = urlparse(a_tag.attrs['href'])
            scheme = parser.scheme or 'http'
            netloc = parser.netloc or domain
            if scheme != 'javascript' and netloc == domain:
                path = parser.path
                query = '?' + parser.query if parser.query else ''
                full_url = f'{scheme}://{netloc}{path}{query}'
                redis_client = thread_local.redis_client
                if not redis_client.sismember('visited_urls', full_url):
                    redis_client.rpush('m_sohu_task', full_url)

    def extract(self, html_page):
        pass

    def store(self, data_dict):
        # redis_client = thread_local.redis_client
        # mongo_db = thread_local.mongo_db
        pass


class SpiderThread(Thread):

    def __init__(self, name, spider):
        super().__init__(name=name, daemon=True)
        self.spider = spider

    def run(self):
        redis_client = redis.Redis(host='1.2.3.4', port=6379, password='1qaz2wsx')
        mongo_client = pymongo.MongoClient(host='1.2.3.4', port=27017)
        thread_local.redis_client = redis_client
        thread_local.mongo_db = mongo_client.msohu 
        while True:
            current_url = redis_client.lpop('m_sohu_task')
            while not current_url:
                current_url = redis_client.lpop('m_sohu_task')
            self.spider.status = SpiderStatus.WORKING
            current_url = current_url.decode('utf-8')
            if not redis_client.sismember('visited_urls', current_url):
                redis_client.sadd('visited_urls', current_url)
                html_page = self.spider.fetch(current_url)
                if html_page not in [None, '']:
                    hasher = hasher_proto.copy()
                    hasher.update(current_url.encode('utf-8'))
                    doc_id = hasher.hexdigest()
                    sohu_data_coll = mongo_client.msohu.webpages
                    if not sohu_data_coll.find_one({'_id': doc_id}):
                        sohu_data_coll.insert_one({
                            '_id': doc_id,
                            'url': current_url,
                            'page': Binary(zlib.compress(pickle.dumps(html_page)))
                        })
                    self.spider.parse(html_page)
            self.spider.status = SpiderStatus.IDLE


def is_any_alive(spider_threads):
    return any([spider_thread.spider.status == SpiderStatus.WORKING
                for spider_thread in spider_threads])


thread_local = local()
hasher_proto = sha1()


def main():
    redis_client = redis.Redis(host='1.2.3.4', port=6379, password='1qaz2wsx')
    if not redis_client.exists('m_sohu_task'):
        redis_client.rpush('m_sohu_task', 'http://m.sohu.com/')

    spider_threads = [SpiderThread('thread-%d' % i, Spider())
                      for i in range(10)]
    for spider_thread in spider_threads:
        spider_thread.start()

    while redis_client.exists('m_sohu_task') or is_any_alive(spider_threads):
        pass

    print('Over!')


if __name__ == '__main__':
    main()
