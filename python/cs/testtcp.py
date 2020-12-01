import socket
import threading
import sys

proxy_server = ('42.192.83.30', 10000) # 代理服务器ip
# proxy_server = ('127.0.0.1', 10000) # 代理服务器ip

def connect_proxy(addr):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(addr)
        while True:
            data = input(">>>")
            if not data:
                break
            client.send(data.encode('utf-8'))
        client.close()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    if len(sys.argv)==2:
        proxy_server = (sys.argv[1], 10000)
    connect_proxy(proxy_server)
    