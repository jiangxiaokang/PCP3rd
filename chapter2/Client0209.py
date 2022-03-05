import socket
from Server0208 import MyThread,recv_message
HOST = 'localhost'
PORT = 51234
BUFSIZ = 1024

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s_cli:
    s_cli.connect((HOST,PORT))
    print('connecting to svr ')
    #new thread for receiving
    t1 = MyThread(recv_message,(s_cli,(HOST,PORT),BUFSIZ))
    t1.start()
    #input
    while True:
        data = input('input msg>')
        try:
            s_cli.send(data.encode('utf-8'))
        except (ConnectionResetError,ConnectionAbortedError):
            break
        if data == 'bye':
            break
        