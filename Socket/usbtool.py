import socket
import time,os,sys


def usbTool():
    host='127.0.0.1'
    port=8003
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((host,port))
    s.sendall('usbmode true')
    data=s.recv(1024)
    print(type(data))
    print(data)
    s.close()




os.popen('')