import socket
import threading

proxy_server = ('42.192.83.30', 10000) # 代理服务器ip

def connect_proxy(addr):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(addr)
    while True:
        data = input(">>>")
        if not data:
            break
        client.send(data.encode('utf-8'))
    client.close()

if __name__ == "__main__":
    connect_proxy(proxy_server)