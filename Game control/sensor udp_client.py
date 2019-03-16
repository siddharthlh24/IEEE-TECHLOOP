import ctypes
import time
import socket


UDP_IP = "192.168.43.153"               
UDP_PORT = 5007
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)                      # UDP
sock.bind((UDP_IP, UDP_PORT))


flg=0
        
while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        #print(data)

        a=data.decode()
        ar1=a.split(',')
        y=ar1[4]
        z=ar1[3]
        print(z)
        #k=3*float(z)

        



                

