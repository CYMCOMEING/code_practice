#客户端
import socket

HOST="localhost"
PORT=9999
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)    #实例化
client.connect((HOST, PORT))    #绑定IP和端口
client.send(b"abc")    #转为二进制发送
data=client.recv(1024)
print(data)