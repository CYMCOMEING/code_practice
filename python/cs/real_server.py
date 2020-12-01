import socket  # 客户端 发送一个数据，再接收一个数据
import threading
import time
import sys

proxy_server = ('42.192.83.30', 9999) # 连接远程普通服务器
local_server = ('127.0.0.1', 10000) # 本地的真正服务器

def connect_proxy(addr):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(addr)
    data = client.recv(1024)
    if not data:
        client.close()
        return
    print('recv:', data.decode())
    th = create_server()
    time.sleep(3)
    client.send(("请连接终点服务器".encode('utf-8')))
    print("服务器运行中")
    th.join()
    client.close()
    
        


def create_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(local_server)
    server.listen(5)
    th = threading.Thread(target=sever_accept, args=(server,))
    print("服务器绑定端口成功", local_server)
    th.start()
    return th


def sever_accept(server):
    while True:
        print("服务器accepting...")
        conn, addr = server.accept()
        print("连接地址：", addr)
        while True:
            try:
                data = conn.recv(1024)
                if not data:
                    break
                print('recive:', data.decode())
                conn.send(("收到：{}".format(data.decode())).encode('utf-8'))
            except ConnectionResetError:
                print('关闭了正在占线的链接！')
                break
        conn.close()


if __name__ == "__main__":
    if len(sys.argv)==2:
        proxy_server = (sys.argv[1], 10000)
    connect_proxy(proxy_server)
    # th = create_server()
    # th.join()
