from http import client
from pydoc import cli
import socket
from threading import Thread
'''
2-9 多用户全双工聊天。进一步修改你的解决方案，以使你的聊天服务支持多用户。
'''

class MyThread(Thread):
    def __init__(self, func,args,name=''):
        Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        self.func(*self.args)

def deal_client(conn ,addr, buffsize):
    if not isinstance(conn,socket.socket):
        raise TypeError
    while True:
        try:
            data =conn.recv(buffsize)
            if not data:
                break
            msg = data.decode('utf-8')
            print(addr,' say:',msg)
            for e in client_list:
                if e == conn:
                    continue
                e.send(data)

            if msg == 'bye':
                client_list.remove(conn)
                break
        except ConnectionResetError:
            print('connection reset')
            break
        except ConnectionAbortedError:
            print('connection abort')
            break

client_list = []
def main():
    HOST = 'localhost'
    PORT = 51234    
    BUFSIZ = 1024
    ADDR = (HOST,PORT)
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as svr:
        svr.bind(ADDR)
        svr.listen(1)
        print('svr wait for connection...')
        while True:
            conn,conn_adr  = svr.accept()
            #new thread for recving msg
            print('new connection : ',conn_adr)
            client_list.append(conn)
            t1 = MyThread(deal_client,(conn,conn_adr,BUFSIZ))
            t1.start()


if __name__ == '__main__':
    main() 