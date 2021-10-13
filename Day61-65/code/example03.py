from bs4 import BeautifulSoup

import requests

import re


def main():
    # 通过requests第三方库的get方法获取页面
    resp = requests.get('http://sports.sohu.com/nba_a.shtml')
    # 对响应的字节串(bytes)进行解码操作(搜狐的部分页面使用了GBK编码)
    html = resp.content.decode('gbk')
    # 创建BeautifulSoup对象来解析页面(相当于JavaScript的DOM)
    bs = BeautifulSoup(html, 'lxml')
    # 通过CSS选择器语法查找元素并通过循环进行处理
    # for elem in bs.find_all(lambda x: 'test' in x.attrs):
    for elem in bs.select('a[test]'):
        # 通过attrs属性(字典)获取元素的属性值
        link_url = elem.attrs['href']
        resp = requests.get(link_url)
        bs_sub = BeautifulSoup(resp.text, 'lxml')
        # 使用正则表达式对获取的数据做进一步的处理
        print(re.sub(r'[\r\n]', '', bs_sub.find('h1').text))


if __name__ == '__main__':
    main()
