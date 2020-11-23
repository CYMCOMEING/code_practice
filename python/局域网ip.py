import socket
import uuid


def get_host_ip1():
    # 通常使用socket.gethostname()方法即可获取本机IP地址，但有时候获取不到（比如没有正确设置主机名称）
    #获取计算机名称
    hostname=socket.gethostname()
    #获取本机IP
    ip=socket.gethostbyname(hostname)
    return ip

def get_host_ip2():
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(('8.8.8.8',80))
        ip=s.getsockname()[0]
    finally:
        s.close()

    return ip


def get_mac_address(): 
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:] 
    return ":".join([mac[e:e+2] for e in range(0,11,2)])


if __name__ == "__main__":
    print(get_host_ip1())
    print(get_host_ip2())
    print(get_mac_address())
