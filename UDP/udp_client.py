import socket
UDP_IP_ADDRESS = "172.16.30.102"
UDP_PORT_NO = 6789

while True:
    Message = input("enter message")
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    clientSock.sendto(bytes(Message,'utf-8'), (UDP_IP_ADDRESS, UDP_PORT_NO))
