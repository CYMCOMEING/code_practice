# 服务器端
import socket

HOST="localhost"
PORT=9999
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 声明
server.bind((HOST, PORT))  # 确定监听的端口
server.listen()  # 开始监听
client,addr = server.accept()    # 在服务器端生成实例并赋值
print("new conn:", addr)

while True:  # 服务器端循环接收数据
    data = client.recv(1024)  # 接受数据，最多1K
    print(data)     # >>b'abc'
    client.send(data.upper)  # 将数据改为大写发回去
