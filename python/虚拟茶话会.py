from asyncore import dispatcher
from asynchat import async_chat
import socket, asyncore

PORT = 5005
NAME = 'TestChat'

class EndSession(Exception):pass

class CommandHandler:

        def unknown(self, session, cmd):
                session.push('Unknown command: %s\r\n' % cmd)

        def handle(self, session, line):
                if not line.strip(): return

                parts = line.split(' ',1)
                cmd = parts[0]
                try: line = parts[1].strip()
                except IndexError: line = ''

                meth = getattr(self, 'do_'+cmd, None)

                try:
                        meth(session, line)
                except TypeError:
                        self.unknown(session,cmd)

class Room(CommandHandler):

        def __init__(self, server):
                self.server = server
                self.sessions = []

        def add(self, session):
                self.sessions.append(session)

        def remove(self, session):
                self.sessions.remove(session)

        def broadcast(self, line):
                for session in self.sessions:
                        session.push(line)

        def do_logout(self, session, line):
                raise EndSession

class LoginRoom(Room):

        def add(self,session):
                Room.add(self,session)

                self.broadcast('Welcome to %s\r\n' % self.server.name)

        def unknown(self, session, cmd):
                session.push('Please log in \nUse "login"\r\n')

        def do_login(self, session, line):
                name = line.strip()

                if not name:
                        session.push('Please enter a name\r\n')
                elif name in self.server.users:
                        session.push('The name "%s" is taken.\r\n' % name)
                        sessoin.push('Please try again.\r\n')
                else:
                        session.name = name
                        session.enter(self.server.main_room)

class ChatRoom(Room):

        def add(self, session):
                self.broadcast(session.name + ' has entered the room.\r\n')
                self.server.users[session.name] = session
                Room.add(self, session)

        def remove(self, session):
                Room.remove(self, session)

                self.broadcast(session.name + ' has left the room.\r\n')

        def do_say(self, session, line):
                self.broadcast(session.name + ': ' + line + '\r\n')

        def do_look(self, session, line):
                session.push('The following are in this room:\r\n')
                for other in self.sessions:
                        session.push(other.name + '\r\n')

        def do_who(self, session, line):
                session.push('The following are logged in:\r\n')
                for name in self.server.users:
                        session.push(name + '\r\n')

class LogoutRoom(Room):

        def add(self, session):
                try: del self.server.users[session.name]
                except KeyError: pass

class ChatSession(async_chat):

        def __init__(self, server, sock):
                async_chat.__init__(self,sock)
                self.server = server
                self.set_terminator('\r\n')
                self.data = []
                self.name = None

                self.enter(LoginRoom(server))

        def enter(self, room):

                try: 
                        cur = self.room
                except AttributeError: 
                        pass
                else: cur.remove(self)
                self.room = room
                room.add(self)

        def collect_incoming_data(self, data):
                self.data.append(data)

        def found_terminator(self):
                line = ''.join(self.data)
                self.data = []
                try: self.room.handle(self, line)
                except EndSession:
                        self.handle_close()

        def handle_close(self):
                async_chat.handle_close(self)
                self.enter(LogoutRoom(self.server))

class ChatServer(dispatcher):

        def __init__(self, port, name):
                dispatcher.__init__(self)
                self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
                self.bind(('',port))
                self.listen(5)
                self.name = name
                self.users = {}
                self.main_room = ChatRoom(self)

        def handle_accept(self):
                conn, addr = self.accept()
                ChatSession(self,conn)

if __name__ == '__main__':
        s = ChatServer(PORT, NAME)
        try: asyncore.loop()
        except KeyboardInterrupt: print

"""
整个程序分为我一开始说的三个部分：
提供客户端的socket连接：ChatServer类。
存储每个客户端的连接session，处理每个连接发送的消息：ChatSession类，这个类的作用很简单，接受数据，判断是否有终结符，如果有调用found_terminator这个方法。
解析客户端发送的数据：就是剩下的room相关的类，这些类分别用来处理客户端发送的字符串和命令，都是继承自CommandHandler。


自己使用python中的socket类尝试这个编写了一个简单的通信程序，不过不知为什么，通信中总是出现意外。这段简单的代码如下：
server.py

import socket

mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysocket.bind(('',8888))
mysocket.listen(5)

while True:
        connection,addr = mysocket.accept()
        revStr = connection.recv(1024)
        connection.send('Server:' + revStr)
        connection.close()

clinet.py

import socket
import time

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientsocket.connect(('',8888))
while True:
        time.sleep(2)
        clientsocket.send('hello the5fire')
        print clientsocket.recv(1024)

clientsocket.close()
这个程序出错的原因没有去细揪，因为python中提供了两个封装好的类来完成socket通信过程：asynchat中的async_chat和asyncore中的dispatcher以及asyncore本身。前面的类是用来处理客户端同服务器的每一次会话，后面的类主要是用来提供socket连接服务。并且将每一个socket连接都托管给前者（async_chat）来处理。
"""