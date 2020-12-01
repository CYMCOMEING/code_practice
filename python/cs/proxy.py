"""
原理很简单。
1.开一个socket server监听连接请求
2.每接受一个客户端的连接请求，就往要转发的地址建一条连接请求。即client->proxy->forward。proxy既是socket服务端(监听client)，也是socket客户端(往forward请求)。
3.把client->proxy和proxy->forward这2条socket用字典给绑定起来。
4.通过这个映射的字典把send/recv到的数据原封不动的传递
"""

# coding=utf-8
import socket
import select
import sys


class Proxy:
    def __init__(self, addr, to_addr):
        self.proxy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.proxy.bind(addr)
        self.proxy.listen(10)
        self.inputs = [self.proxy]
        self.route = {}
        self.to_addr = (to_addr)  # 转发的地址
        print("to_addr :", to_addr)

    def serve_forever(self):
        print('proxy listen...')
        while 1:
            readable, _, _ = select.select(self.inputs, [], [])
            print("select")
            for self.sock in readable:
                if self.sock == self.proxy:
                    self.on_join()
                else:
                    data = self.sock.recv(8096)
                    if not data:
                        self.on_quit()
                    else:
                        print("转发消息：{}".format(data.decode("utf-8")))
                        self.route[self.sock].send(data)

    def on_join(self):
        client, addr = self.proxy.accept()
        print(addr, 'connect')
        forward = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        forward.connect(self.to_addr)
        self.inputs += [client, forward]
        self.route[client] = forward
        self.route[forward] = client

    def on_quit(self):
        print("on_quit")
        for s in self.sock, self.route[self.sock]:
            self.inputs.remove(s)
            del self.route[s]
            s.close()


if __name__ == '__main__':
    try:
        Proxy(('', 10000), ('', 10001)).serve_forever()  # 代理服务器监听的地址
    except KeyboardInterrupt:
        sys.exit(1)
