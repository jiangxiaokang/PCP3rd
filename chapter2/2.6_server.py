import socket
import os
import time

BUFSIZ = 1024
HOST='localhost'
PORT=50007

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen(1)
    while True:
        conn,add = s.accept()
        print("connected by ",add)
        data = conn.recv(BUFSIZ)
        if not data:break

        msg = data.decode('utf-8')
        if msg == 'os':
            conn.send(os.name.encode('utf-8'))
        elif msg == 'ls':
            conn.send(str(os.listdir()).encode('utf-8'))
        else:
            conn.send(time.ctime().encode('utf-8'))
        conn.sendall(data)

    