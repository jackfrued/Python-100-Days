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
        <p>Good!!!</p>
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
        <img src="./static/img/pretty-girl.png" alt="美女">
        <goup>Hello, Goup!</goup>
    </body>
    </html>
    """
    # resp = requests.get('http://sports.sohu.com/nba_a.shtml')
    # html = resp.content.decode('gbk')
    soup = BeautifulSoup(html, 'lxml')
    print(soup.title)
    # JavaScript: document.body.h1
    # JavaScript: document.forms[0]
    print(soup.body.h1)
    print(soup.find_all(re.compile(r'p$')))
    print(soup.find_all('img', {'src': re.compile(r'\./img/\w+.png')}))
    print(soup.find_all(lambda x: len(x.attrs) == 2))
    print(soup.find_all('p', {'class': 'foo'}))
    for elem in soup.select('a[href]'):
        print(elem.attrs['href'])


if __name__ == '__main__':
    main()
