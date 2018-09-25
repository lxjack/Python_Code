# coding=utf-8

from socket import *
HOST=""
PORT=21567
BUFSIZE=1024
ADDR=(HOST,PORT)

tcpSerSock=socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

tcpCliSock,addr=tcpSerSock.accept()
print "...connect from:",addr
while True:
    data = tcpCliSock.recv(BUFSIZE)
    print "receive info:" + data
    if not data or data == "exit":
        break

tcpCliSock.close()

tcpSerSock.close()
