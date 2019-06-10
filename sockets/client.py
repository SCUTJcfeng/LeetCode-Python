# !/usr/bin/python3.6
# -*- coding:utf-8 -*-
'''
Project: sockets
Author: jc feng (jcfeng2013@gmail.com)
File Created: 2019-06-10 20:45:26
Last Modified: 2019-06-10 20:52:55
'''

import socket


HOST = '127.0.0.1'
PORT = 65432


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'hello, world')
    data = s.recv(1024)
    print(f'receive data: {data.decode("utf8")}')
