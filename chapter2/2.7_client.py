from socket import *

HOST='localhost'
BUFSIZ=1024
udp_cli=socket(AF_INET,SOCK_DGRAM)
while True:
    PORT = getservbyname("daytime",'udp')
    udp_cli.sendto('get day time '.encode('utf-8'),(HOST,PORT));
    data,addr = udp_cli.recvfrom(BUFSIZ)
    print('svr receive from ',addr,' msg is ',data)
udp_cli.close()
