import socket  # 客户端 发送一个数据，再接收一个数据
import threading
import time


def connect_proxy(addr):
    # 声明socket类型，同时生成链接对象
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(addr)  # 建立一个链接，连接到本地的6969端口
    data = client.recv(1024)
    if data:
        print('recv:', data.decode())  # 输出我接收的信息
        th = create_server()
        time.sleep(5)
        client.send(("请连接终点服务器".encode('utf-8')))
    client.close()
    print("服务器运行中")
    th.join()
        


def create_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', 10000))
    server.listen(5)
    th = threading.Thread(target=sever_accept, args=(server,))
    print("服务器绑定端口成功")
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
                print('recive:', data.decode())  # 打印接收到的数据
                conn.send(("收到：{}".format(data.decode())).encode('utf-8'))  # 然后再发送数据
            except ConnectionResetError:
                print('关闭了正在占线的链接！')
                break
        conn.close()


if __name__ == "__main__":
    connect_proxy(('42.192.83.30', 9999))
