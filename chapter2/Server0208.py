import socket
from threading import Thread
import CommonConfig
'''
2.8 全双工聊天。更新上一个练习的解决方案，修改它以使你的聊天服务现在成为全双
工模式，意味着通信两端都可以发送并接收消息，并且二者相互独立。
用多线程来做
'''

class MyThread(Thread):
    def __init__(self, func,args,name=''):
        Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        self.func(*self.args)

def recv_message(conn,addr,buffsize):
    if not isinstance(conn,socket.socket):
        raise TypeError
    while True:
        try:
            data =conn.recv(buffsize)
            if not data:
                break
            msg = data.decode('utf-8')
            print('\n',addr,' say:',msg)
            if msg == 'bye':
                break
        except ConnectionResetError:
            print('connection reset')
            break
        except ConnectionAbortedError:
            print('connection abort')
            break;


def main():
    HOST = 'localhost'
    PORT = 51234    
    BUFSIZ = 1024
    ADDR = (HOST,PORT)
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as svr:
        svr.bind(ADDR)
        svr.listen(1)
        print('svr wait for connection...')
        conn,conn_adr  = svr.accept()
        #new thread for recving msg
        print('new connection : ',conn_adr)
        t1 = MyThread(recv_message,(conn,conn_adr,BUFSIZ))
        t1.start()
        while True:
            reply_data = input('input replay>')
            try:
                conn.send(reply_data.encode('utf-8'))
            except ConnectionResetError:
                print('send data connection reset error')
                break
            except ConnectionAbortedError:
                print('connection aborted')
                break;


if __name__ == '__main__':
    main() 