import robobrowser


def main():
    b = robobrowser.RoboBrowser(parser='lxml')
    b.open('https://github.com/login')
    f = b.get_form(action='/session')
    f['login'].value = 'jackfrued@gmail.com'
    f['password'].value = 'yourpassword'
    b.submit_form(f)
    for a_tag in b.select('a[href]'):
        print(a_tag.attrs['href'])


if __name__ == '__main__':
    main()
