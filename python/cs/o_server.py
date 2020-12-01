#!/usr/bin/env python
from socket import *
import time
import sys
import os

HOST = 'localhost'
PORT = 9500
BUFIZ = 1024
ADDR = (HOST, PORT)


def recvfile(filename):
    print('starting receive file...')
    f = open(filename, 'wb')
    cliSockfd.send(b'no problem')
    while True:
        data = cliSockfd.recv(4096)
        if data.decode() == 'EOF':
            print('recved file success!')
            break
        f.write(data)
    f.close()


def sendfile(filename):
    print('starting send file...')
    cliSockfd.send(b'no problem')
    f = open(filename, 'rb')
    while True:
        data = f.read(4096)
        if not data:
            break
        cliSockfd.send(data)
    f.close()
    time.sleep(1)
    cliSockfd.send(b'EOF')
    print('send file success!')


def handle1(act, filename):
    if act == 'put':
        print('recving msg!')
        recvfile(filename)
    elif act == 'get':
        print('sending msg! ' + filename)
        sendfile(filename)
    else:
        print('error!')


def handle2(act):
    if act == 'ls':
        path = sys.path[0]
        every_file = os.listdir(path)
        for filename in every_file:
            cliSockfd.send(bytes(filename + ' ', encoding='utf-8'))
        time.sleep(1)
        cliSockfd.send(b'EOF')
        print('all filename has send to client success!')
    else:
        print('command error')


sockfd = socket(AF_INET, SOCK_STREAM)
sockfd.bind(ADDR)
sockfd.listen(5)
while True:
    print('waiting for connection...')
    cliSockfd, addr = sockfd.accept()
    print('...connected from:', addr)

    while True:
        bmsg = cliSockfd.recv(4096)
        msg = bmsg.decode()
        if msg == 'close':
            print('client closed')
            break
        info = msg.split()
        print("msg {}  info {}".format(msg, info))
        if len(info) == 2:
            handle1(*info)
        elif len(info) == 1:
            handle2(*info)
        else:
            print('command error!' + msg)
            break
