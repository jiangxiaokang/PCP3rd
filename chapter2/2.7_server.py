from socket import *
from time import ctime


HOST='localhost'
PORT=13
BUFSIZ=1024

udp_svr=socket(AF_INET,SOCK_DGRAM)
udp_svr.bind((HOST,PORT))
while True:
    print('svr waiting form message...')
    data,addr=udp_svr.recvfrom(BUFSIZ)
    if data:
        udp_svr.sendto(ctime().encode('utf-8'),addr);
        print('svr receive from ',addr,' msg is ',data)
    else :
        break
udp_svr.close()
