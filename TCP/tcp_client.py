import socket


TCP_IP = '192.168.43.153'
TCP_PORT = 5005
BUFFER_SIZE = 1024
#MESSAGE = "yeah man"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
while True:
    MESSAGE = input()
    s.send(bytes(MESSAGE,'utf-8'))
    data = s.recv(BUFFER_SIZE)
    #s.close()

print ("received data:", data)
