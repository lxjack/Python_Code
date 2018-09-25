# coding=utf-8

from socket import *
HOST="127.0.0.1"
PORT=21567
BUFSIZE=1024
ADDR=(HOST,PORT)

tcpCliSock=socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = raw_input(">>>")
    if not data:
        break
    tcpCliSock.send(data)
    if data == "exit":
        break

tcpCliSock.close()

