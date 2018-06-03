import requests
from bs4 import BeautifulSoup


def main():
    resp = requests.get('https://github.com/login')
    if resp.status_code != 200:
        return
    cookies = resp.cookies.get_dict()
    print(cookies)
    soup = BeautifulSoup(resp.text, 'lxml')
    utf8_value = \
        soup.select_one('form input[name=utf8]').attrs['value']
    authenticity_token_value = \
        soup.select_one('form input[name=authenticity_token]').attrs['value']
    data = {
        'utf8': utf8_value,
        'authenticity_token': authenticity_token_value,
        'login': 'jackfrued@gmail.com',
        'password': 'yourpassword'
    }
    resp = requests.post('https://github.com/session',
                         data=data, cookies=cookies)
    print(resp.text)


if __name__ == '__main__':
    main()
