"""
套接字 - 基于UDP协议创建Echo客户端

Version: 0.1
Author: 骆昊
Date: 2018-03-22
"""

from socket import *

client = socket(AF_INET, SOCK_DGRAM)
while True:
    data_str = input('请输入: ')
    client.sendto(data_str.encode('utf-8'), ('localhost', 6789))
    data, addr = client.recvfrom(1024)
    data_str = data.decode('utf-8')
    print('服务器回应:', data_str)
    if data_str == 'bye':
        break
client.close()
