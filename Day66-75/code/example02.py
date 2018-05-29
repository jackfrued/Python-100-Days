from bs4 import BeautifulSoup

import re


def main():
    html = """
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>首页</title>
        </head>
        <body>
            <h1>Hello, world!</h1>
            <p>这是一个<em>神奇</em>的网站！</p>
            <hr>
            <div>
                <h2>这是一个例子程序</h2>
                <p>静夜思</p>
                <p class="foo">床前明月光</p>
                <p id="bar">疑似地上霜</p>
                <p class="foo">举头望明月</p>
                <div><a href="http://www.baidu.com"><p>低头思故乡</p></a></div>
            </div>
            <a class="foo" href="http://www.qq.com">腾讯网</a>
            <img src="./img/pretty-girl.png" alt="美女">
            <img src="./img/hellokitty.png" alt="凯蒂猫">
            <img src="/static/img/pretty-girl.png" alt="美女">
            <table>
                <tr>
                    <th>姓名</th>
                    <th>上场时间</th>
                    <th>得分</th>
                    <th>篮板</th>
                    <th>助攻</th>
                </tr>
            </table>
        </body>
    </html>
    """
    soup = BeautifulSoup(html, 'lxml')
    # JavaScript - document.title
    print(soup.title)
    # JavaScript - document.body.h1
    print(soup.body.h1)
    print(soup.p)
    print(soup.body.p.text)
    print(soup.body.p.contents)
    for p_child in soup.body.p.children:
        print(p_child)
    print(len([elem for elem in soup.body.children]))
    print(len([elem for elem in soup.body.descendants]))
    print(soup.findAll(re.compile(r'^h[1-6]')))
    print(soup.body.find_all(r'^h'))
    print(soup.body.div.find_all(re.compile(r'^h')))
    print(soup.find_all(re.compile(r'r$')))
    print(soup.find_all('img', {'src': re.compile(r'\./img/\w+.png')}))
    print(soup.find_all(lambda x: len(x.attrs) == 2))
    print(soup.find_all(foo))
    print(soup.find_all('p', {'class': 'foo'}))
    for elem in soup.select('a[href]'):
        print(elem.attrs['href'])


def foo(elem):
    return len(elem.attrs) == 2


if __name__ == '__main__':
    main()
