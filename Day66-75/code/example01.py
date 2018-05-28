from urllib.error import URLError
from urllib.request import urlopen

import re
import pymysql


def get_page_code(start_url, *, retry_times=3, charsets=('utf-8', )):
    try:
        for charset in charsets:
            try:
                html = urlopen(start_url).read().decode(charset)
                break
            except UnicodeDecodeError:
                html = None
    except URLError as ex:
        print('Error:', ex)
        return get_page_code(start_url, retry_times=retry_times - 1, charsets=charsets) if \
            retry_times > 0 else None
    return html


def main():
    url_list = ['http://sports.sohu.com/nba_a.shtml']
    visited_list = set({})
    while len(url_list) > 0:
        current_url = url_list.pop(0)
        visited_list.add(current_url)
        print(current_url)
        html = get_page_code(current_url, charsets=('utf-8', 'gbk', 'gb2312'))
        if html:
            link_regex = re.compile(r'<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
            link_list = re.findall(link_regex, html)
            url_list += link_list
            conn = pymysql.connect(host='localhost', port=3306,
                                   db='crawler', user='root',
                                   passwd='123456', charset='utf8')
            try:
                for link in link_list:
                    if link not in visited_list:
                        visited_list.add(link)
                        print(link)
                        html = get_page_code(link, charsets=('utf-8', 'gbk', 'gb2312'))
                        if html:
                            title_regex = re.compile(r'<h1>(.*)<span', re.IGNORECASE)
                            match_list = title_regex.findall(html)
                            if len(match_list) > 0:
                                title = match_list[0]
                                with conn.cursor() as cursor:
                                    cursor.execute('insert into tb_result (rtitle, rurl) values (%s, %s)',
                                               (title, link))
                                conn.commit()
            finally:
                conn.close()
    print('执行完成!')


if __name__ == '__main__':
    main()

