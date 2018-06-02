import requests
from bs4 import BeautifulSoup
# selenium是一个自动化测试工具
# 通过它可以模拟浏览器的行为来访问Web页面
from selenium import webdriver


def main():
    # 先下载chromedriver并且将可执行程序放到PATH环境变量路径下
    # 创建谷歌Chrome浏览器内核
    driver = webdriver.Chrome()
    # 通过浏览器内核加载页面(可以加载动态生成的内容)
    driver.get('https://www.taobao.com/markets/mm/mm2017')
    # driver.page_source获得的页面包含了JavaScript动态创建的内容
    soup = BeautifulSoup(driver.page_source, 'lxml')
    all_images = soup.select('img[src]')
    for image in all_images:
        url = image.get('src')
        try:
            if not str(url).startswith('http'):
                url = 'http:' + url
            filename = url[url.rfind('/') + 1:]
            print(filename)
            resp = requests.get(url)
            with open('c:/images/' + filename, 'wb') as f:
                f.write(resp.content)
        except OSError:
            print(filename + '下载失败!')
    print('图片下载完成!')


if __name__ == '__main__':
    main()