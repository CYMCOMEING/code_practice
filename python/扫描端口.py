#!/usr/bin/env python
 
import socket
import threading
import telnetlib
import queue
 
def get_ip_status_socket(ip,port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.connect((ip,port))
        print('{0} port {1} is open'.format(ip, port))
    except Exception as err:
        print('{0} port {1} is not open'.format(ip,port))
    finally:
        server.close()

 
def get_ip_status_telnet(ip,port):
    server = telnetlib.Telnet()      # 创建一个Telnet对象
    try:
        server.open(ip,port)         # 利用Telnet对象的open方法进行tcp链接
        print('{0} port {1} is open'.format(ip, port))
    except Exception as err:
        print('{0} port {1} is not open'.format(ip,port))
    finally:
        server.close()


def get_ip_status_telnet2(ip):
    server = telnetlib.Telnet()
    for port in range(20,100):
        try:
            server.open(ip,port)
            print('{0} port {1} is open'.format(ip, port))
        except Exception as err:
            print('{0} port {1} is not open'.format(ip,port))
        finally:
            server.close()
            
def check_open(q):
    try:
        while True:
            ip = q.get_nowait()
            get_ip_status_telnet2(ip)
    except queue.Empty as e:
        pass
 
if __name__ == '__main__':
    """
    #使用的是python的socket模块完成的端口检测
    host = '127.0.0.1'
    for port in range(20,200):
        get_ip_status_socket(host,port)
    """

    """
    #python的内置模块telnetlib也可以完成端口检测任务
    host = '127.0.0.1'
    for port in range(20,200):
        get_ip_status_telnet(host,port)
    """

    """
    #多线程
    host = '127.0.0.1'
    threads = []
    for port in range(20,200):
        t = threading.Thread(target=get_ip_status_telnet,args=(host,port))
        t.start()
        threads.append(t)
 
    for t in threads:
        t.join()
    """

    """
    这里使用了Queue，那么就会引出生产者和消费者模型，生产者只需要把信息存入到队列中，消费者消费时只需要看队列中有没有，这样极大程度了解耦了我们的程序。
    """
    host = ['10.0.0.10','10.0.0.11','10.0.0.12']     # 这里模拟多IP地址的情况，也可以从文件中读取IP——list
    q = queue.Queue()
    for ip in host:
        q.put(ip)
    threads = []
    for i in range(10):
        t = threading.Thread(target=check_open,args=(q,))
        t.start()
        threads.append(t)
 
    for t in threads:
        t.join()
