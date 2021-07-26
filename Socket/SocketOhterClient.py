import socket

def SocketClient():
    host='127.0.0.1'
    port =2001
    message=['nnnnnnnnnnnn']
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((host,port))
    for line in message:
        s.sendall(line.encode(encoding='utf-8',errors='strict'))
        data=s.recv(1024)
        if len(data)>0:
            print('Comunicate is',data)
    s.close()

while True:
    SocketClient()