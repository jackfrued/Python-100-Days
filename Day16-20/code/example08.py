"""
加密和解密
对称加密 - 加密和解密是同一个密钥 - DES / AES
非对称加密 - 加密和解密是不同的密钥 - RSA
pip install pycrypto
"""
import base64

from hashlib import md5

from Crypto.Cipher import AES
from Crypto import Random
from Crypto.PublicKey import RSA

# # AES加密的密钥（长度32个字节）
# key = md5(b'1qaz2wsx').hexdigest()
# # AES加密的初始向量（随机生成）
# iv = Random.new().read(AES.block_size)


def main():
    """主函数"""
    # 生成密钥对
    key_pair = RSA.generate(1024)
    # 导入公钥
    pub_key = RSA.importKey(key_pair.publickey().exportKey())
    # 导入私钥
    pri_key = RSA.importKey(key_pair.exportKey())
    message1 = 'hello, world!'
    # 加密数据
    data = pub_key.encrypt(message1.encode(), None)
    # 对加密数据进行BASE64编码
    message2 = base64.b64encode(data[0])
    print(message2)
    # 对加密数据进行BASE64解码
    data = base64.b64decode(message2)
    # 解密数据
    message3 = pri_key.decrypt(data)
    print(message3.decode())
    # # AES - 对称加密
    # str1 = '我爱你们！'
    # cipher = AES.new(key, AES.MODE_CFB, iv)
    # # 加密
    # str2 = cipher.encrypt(str1)
    # print(str2)
    # # 解密
    # cipher = AES.new(key, AES.MODE_CFB, iv)
    # str3 = cipher.decrypt(str2)
    # print(str3.decode())


if __name__ == '__main__':
    main()
