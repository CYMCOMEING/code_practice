import socket
import threading
import proxy

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 9999))
server.listen(5)
while True:
    conn, addr = server.accept()
    print("连接地址：", addr)
    conn.send(("请创建终点服务器".encode('utf-8')))
    data = conn.recv(1024)
    if not data:
        conn.close()
        break
    print('recive:',data.decode())
    proxy_server = proxy.Proxy(('', 10000), addr)
    th = threading.Thread(target=proxy_server.serve_forever)
    th.start()
    conn.close()
    th.join()



# import socket
# # 建立一个服务端
# server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# server.bind(('',6999)) #绑定要监听的端口
# server.listen(5) #开始监听 表示可以使用五个链接排队
# while True:# conn就是客户端链接过来而在服务端为期生成的一个链接实例
#     conn,addr = server.accept() #等待链接,多个链接的时候就会出现问题,其实返回了两个值
#     print("连接地址：",addr)
#     conn.send(("当前地址：{}".format(addr)).encode('utf-8'))
#     while True:
#         try:
#             data = conn.recv(1024)  #接收数据
#             if not data: # 在客户断开后，客户端会发送null，但是python没有null，所以用''代替
#                 break
#             print('recive:',data.decode()) #打印接收到的数据
#             conn.send(data.upper()) #然后再发送数据
#         except ConnectionResetError as e:
#             print('关闭了正在占线的链接！')
#             break
#     conn.close()
