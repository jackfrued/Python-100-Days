import base64

from PIL import Image, ImageFilter
from pytesseract import image_to_string

import requests
from io import BytesIO


def main():
    guido_img = Image.open(open('guido.jpg', 'rb'))
    guido2_img = guido_img.filter(ImageFilter.GaussianBlur)
    guido2_img.save(open('guido2.jpg', 'wb'))

    img1 = Image.open(open('tesseract.png', 'rb'))
    img2 = img1.point(lambda x: 0 if x < 128 else 255)
    img2.save(open('tesseract2.png', 'wb'))

    print(image_to_string(img2))

    resp = requests.get('https://pin2.aliyun.com/get_img?type=150_40&identity=mailsso.mxhichina.com&sessionid=k0xHyBxU3K3dGXb59mP9cdeTXxL9gLHSTKhRZCryHxpOoyk4lAVuJhgw==')
    img3 = Image.open(BytesIO(resp.content))
    img3.save('captcha.jpg')
    print(image_to_string(img3))
    print(base64.b64encode(resp.content))


if __name__ == '__main__':
    main()
