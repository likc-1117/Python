#coding=utf-8

from socket import socket

class socket_client:
    @staticmethod
    def sendmsg(msg):
        data = 'fail'
        # localip=socket.gethostbyname(socket.gethostname())
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            # s.settimeout(10)
            s.connect(('127.0.0.1', 8002))
            s.sendall(msg)
            data = s.recv(1024)
            # print(eval(data))
        except socket.timeout:
            print('timeout')
        s.close()
        return data