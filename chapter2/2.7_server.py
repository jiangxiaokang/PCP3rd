import socket

HOST = 'localhost'
PORT = 56123
BUFSIZ = 1024

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as srv:
    srv.bind((HOST,PORT))
    srv.listen(1)
    print('accepting connection...')
    conn,addr = srv.accept()
    print('new connection ',addr)
    while True:
        data = conn.recv(BUFSIZ)
        msg = data.decode('utf-8')
        print(addr,' say ',msg)
        if msg == 'bye':
            break
        reply_data = input('input replay>')
        conn.send(reply_data.encode('utf-8'))