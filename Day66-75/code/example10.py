import robobrowser


def main():
    b = robobrowser.RoboBrowser(parser='lxml')
    b.open('https://v.taobao.com/v/content/live?catetype=704&from=taonvlang')
    for img_tag in b.select('img[src]'):
        print(img_tag.attrs['src'])


if __name__ == '__main__':
    main()
