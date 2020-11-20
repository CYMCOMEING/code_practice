#!/usr/bin/env python
import sys
import socket
import time
HOST = 'localhost'
PORT = 9500
BUFSIZ = 1024
ADDR = (HOST,PORT)
  
cliSockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  
def recvfile(filename):
 f = open(filename,'wb')
 while True:
  msg = cliSockfd.recv(4096)
  if msg == 'EOF':
   print('recv file success!')
   break
  f.write(msg)
 f.close
def sendfile(filename):
 f = open(filename,'rb')
 while True:
  msg = f.read(4096)
  if not msg:
    break
  cliSockfd.sendall(msg)
 f.close()
 time.sleep(1)
 cliSockfd.sendall('EOF')
 print('send file success')
def confirm(cliSockfd,client_command):
 cliSockfd.send(client_command)
 msg = cliSockfd.recv(4096)
 if msg == 'no problem':
  return True
  
def handle1(act,filename):
 if act == 'put':
  if confirm(cliSockfd,client_command):
   sendfile(filename)
  else:
   print('server error1!')
 elif act == 'get':
  if confirm(cliSockfd,client_command):
   recvfile(filename)
  else:
   print('server error2!'）
 else:
  print('command error!'）
def handle2(act):
 if act == 'ls':
  cliSockfd.send('ls')
  while True:
   msg = cliSockfd.recv(1024)
   if msg == 'EOF':
    break
   print(msg）
 else:
  print('command error'）
  
try:
 cliSockfd.connect(ADDR)
 print('connect to ',ADDR）
 while True:
  client_command = raw_input('>>>')
  if not client_command:
   continue
  msg = client_command.split()
  if len(msg) == 2:
   handle1(*msg)
  elif len(msg) == 1 and msg != ['close']:
   handle2(*msg)
  elif len(msg) == 1 and msg == ['close']:
   cliSockfd.send('close')
   break
  else:
   print('command error'）
except socket.error,e:
 print('error:',e）
finally:
 cliSockfd.close()