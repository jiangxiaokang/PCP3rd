import socket
HOST='localhost'
PORT=50007
BUFSIZ = 1024
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    while True:
        #s.sendall(b'hello, world')
        data = input('>')
        if not data:
            break
        s.sendall(data.encode('utf-8'))

        data=s.recv(BUFSIZ)
        if not data:
            break
        print(data.decode('utf-8'))