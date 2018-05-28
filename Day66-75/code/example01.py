from urllib.error import URLError
from urllib.request import urlopen

import re
import pymysql
import ssl

from pymysql import Error


def decode_page(page_bytes, charsets=('utf-8', )):
    page_html = None
    for charset in charsets:
        try:
            page_html = page_bytes.decode(charset)
            break
        except UnicodeDecodeError:
            pass
            # logging.error('Decode:', error)
    return page_html


def get_page_html(seed_url, *, retry_times=3, charsets=('utf-8', )):
    page_html = None
    try:
        page_html = decode_page(urlopen(seed_url).read(), charsets)
    except URLError:
        # logging.error('URL:', error)
        if retry_times > 0:
            return get_page_html(seed_url, retry_times=retry_times - 1,
                                 charsets=charsets)
    return page_html


def get_matched_parts(page_html, pattern_str, pattern_ignore_case=re.I):
    pattern_regex = re.compile(pattern_str, pattern_ignore_case)
    return pattern_regex.findall(page_html) if page_html else []


def start_crawl(seed_url, match_pattern):
    conn = pymysql.connect(host='localhost', port=3306,
                           database='crawler', user='root',
                           password='123456', charset='utf8')
    try:
        with conn.cursor() as cursor:
            url_list = [seed_url]
            while url_list:
                current_url = url_list.pop(0)
                page_html = get_page_html(current_url, charsets=('utf-8', 'gbk', 'gb2312'))
                links_list = get_matched_parts(page_html, match_pattern)
                url_list += links_list
                param_list = []
                for link in links_list:
                    page_html = get_page_html(link, charsets=('utf-8', 'gbk', 'gb2312'))
                    headings = get_matched_parts(page_html, r'<h1>(.*)<span')
                    if headings:
                        param_list.append((headings[0], link))
                cursor.executemany('insert into tb_result values (default, %s, %s)',
                                   param_list)
                conn.commit()
    except Error:
        pass
        # logging.error('SQL:', error)
    finally:
        conn.close()


def main():
    ssl._create_default_https_context = ssl._create_unverified_context
    start_crawl('http://sports.sohu.com/nba_a.shtml', 
                r'<a[^>]+test=a\s[^>]*href=["\'](.*?)["\']')


if __name__ == '__main__':
    main()
