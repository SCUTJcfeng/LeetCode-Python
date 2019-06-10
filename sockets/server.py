# !/usr/bin/python3.6
# -*- coding:utf-8 -*-
'''
Project: sockets
Author: jc feng (jcfeng2013@gmail.com)
File Created: 2019-06-10 20:32:12
Last Modified: 2019-06-10 20:55:23
'''

import socket

'''
server          client

socket
⬇
bind
⬇
listen
⬇
accept          socket
⬇                 ⬇
⬇               connect
⬇                 ⬇
recv     ⬅      send
⬇                 ⬇
send     ➡     recv
⬇                 ⬇
recv     ⬅     close
⬇
close
'''

HOST = '127.0.0.1'
# 1-65535
PORT = 65432


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    # accept方法阻塞并等待传入连接
    while True:
        conn, addr = s.accept()
        with conn:
            print(f'connected by {addr}')
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f'receive data: {data.decode("utf8")}')
                conn.sendall(data)
