"""
套接字 - 基于UDP协议Echo服务器

Version: 0.1
Author: 骆昊
Date: 2018-03-22
"""
from socket import *
from time import *

server = socket(AF_INET, SOCK_DGRAM)
server.bind(('localhost', 6789))
while True:
    data, addr = server.recvfrom(1024)
    server.sendto(data, addr)
server.close()
