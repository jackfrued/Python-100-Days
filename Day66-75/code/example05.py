from urllib.error import URLError
from urllib.request import urlopen

import re
import redis
import ssl
import hashlib
import logging
import pickle
import zlib

# Redis有两种持久化方案
# 1. RDB
# 2. AOF


# 通过指定的字符集对页面进行解码(不是每个网站都将字符集设置为utf-8)
def decode_page(page_bytes, charsets=('utf-8',)):
    page_html = None
    for charset in charsets:
        try:
            page_html = page_bytes.decode(charset)
            break
        except UnicodeDecodeError:
            pass
            # logging.error('[Decode]', err)
    return page_html


# 获取页面的HTML代码(通过递归实现指定次数的重试操作)
def get_page_html(seed_url, *, retry_times=3, charsets=('utf-8',)):
    page_html = None
    try:
        if seed_url.startswith('http://') or \
                seed_url.startswith('https://'):
            page_html = decode_page(urlopen(seed_url).read(), charsets)
    except URLError as err:
        logging.error('[URL]', err)
        if retry_times > 0:
            return get_page_html(seed_url, retry_times=retry_times - 1,
                                 charsets=charsets)
    return page_html


# 从页面中提取需要的部分(通常是链接也可以通过正则表达式进行指定)
def get_matched_parts(page_html, pattern_str, pattern_ignore_case=re.I):
    pattern_regex = re.compile(pattern_str, pattern_ignore_case)
    return pattern_regex.findall(page_html) if page_html else []


# 开始执行爬虫程序
def start_crawl(seed_url, match_pattern, *, max_depth=-1):
    client = redis.Redis(host='1.2.3.4', port=6379, password='1qaz2wsx')
    charsets = ('utf-8', 'gbk', 'gb2312')
    logging.info('[Redis ping]', client.ping())
    url_list = [seed_url]
    visited_url_list = {seed_url: 0}
    while url_list:
        current_url = url_list.pop(0)
        depth = visited_url_list[current_url]
        if depth != max_depth:
            page_html = get_page_html(current_url, charsets=charsets)
            links_list = get_matched_parts(page_html, match_pattern)
            for link in links_list:
                if link not in visited_url_list:
                    visited_url_list[link] = depth + 1
                    page_html = get_page_html(link, charsets=charsets)
                    if page_html:
                        hasher = hashlib.md5()
                        hasher.update(link.encode('utf-8'))
                        zipped_page = zlib.compress(pickle.dumps(page_html))
                        client.set(hasher.hexdigest(), zipped_page)


def main():
    ssl._create_default_https_context = ssl._create_unverified_context
    start_crawl('http://sports.sohu.com/nba_a.shtml',
                r'<a[^>]+test=a\s[^>]*href=["\'](.*?)["\']',
                max_depth=2)


if __name__ == '__main__':
    main()
