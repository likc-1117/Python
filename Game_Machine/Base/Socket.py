# -*- coding: utf-8 -*-
'''
Created on 2019年9月19日

@author: likecan
'''
import socket
class socket_client():
    
    
    
    @staticmethod
    def send_msg(order):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect('127.0.0.1',8080)
            s.sendall(order.encode(encoding = 'utf-8'))
            socket_return_data = s.recv(1024)
            print(socket_return_data)
        except Exception as e:
            print(e)
        s.close()
        return socket_return_data
    
    
    
    
    
    
    
    
    
    
    