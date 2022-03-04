import socket

HOST = 'localhost'
PORT = 56123
BUFSIZ = 1024

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s_cli:
    s_cli.connect((HOST,PORT))
    print('connecting to svr ')
    while True:
        data = input('input msg>')
        s_cli.send(data.encode('utf-8'))
        recv_data = s_cli.recv(BUFSIZ)
        if recv_data:
            print('receive msg '+recv_data.decode('utf-8'))
        else :
            break