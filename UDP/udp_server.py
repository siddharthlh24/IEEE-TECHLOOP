# Import "socket" python module.

import socket

# define IP address and port number.

UDP_IP_ADDRESS = "192.168.43.153"
UDP_PORT_NO = 6789

# declare server socket.

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
while True:
    data, addr = serverSock.recvfrom(1024)
    print ("Message: ", data)
