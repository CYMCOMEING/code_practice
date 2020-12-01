#!/usr/bin/env python
import sys
import socket
import time
HOST = '42.192.83.30'
PORT = 12345
BUFSIZ = 1024
ADDR = (HOST, PORT)

cliSockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def recvfile(filename):
    f = open(filename, 'wb')
    while True:
        msg = cliSockfd.recv(4096)
        if msg.decode() == 'EOF':
            print('recv file success!')
            break
        f.write(msg)
    f.close


def sendfile(filename):
    f = open(filename, 'rb')
    while True:
        msg = f.read(4096)
        if not msg:
            break
        cliSockfd.sendall(msg)
    f.close()
    time.sleep(1)
    cliSockfd.sendall(b'EOF')
    print('send file success')


def confirm(cliSockfd, client_command):
    print("confirm " + client_command)
    cliSockfd.send(bytes(client_command, encoding='utf-8'))
    msg = cliSockfd.recv(4096)
    print("recv p aaa  " + msg.decode())
    if msg.decode() == 'no problem':
        return True


def handle1(act, filename):
    if act == 'put':
        if confirm(cliSockfd, client_command):
            sendfile(filename)
        else:
            print('server error1!')
    elif act == 'get':
        if confirm(cliSockfd, client_command):
            recvfile(filename)
        else:
            print('server error2!')
    else:
        print('command error!')


def handle2(act):
    if act == 'ls':
        cliSockfd.send(b'ls')
        while True:
            bmsg = cliSockfd.recv(1024)
            msg = bmsg.decode()
            if msg == 'EOF':
                break
            print(msg)
    else:
        print('command error')


try:
    cliSockfd.connect(ADDR)
    print('connect to ', ADDR)
    while True:
        client_command = input('>>>')
        if not client_command:
            continue
        print("command " + client_command)
        msg = client_command.split()
        if len(msg) == 2:
            handle1(*msg)
        elif len(msg) == 1 and msg != ['close']:
            handle2(*msg)
        elif len(msg) == 1 and msg == ['close']:
            cliSockfd.send(b'close')
            break
        else:
            print('command error')
except socket.error as e:
    print('error:', e)
finally:
    cliSockfd.close()
