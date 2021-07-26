# -*- coding: utf-8 -*-
'''
Created on 2019年9月19日

@author: likecan
'''
from Base.Socket import socket_client

class hero_move():
    @staticmethod
    def up(instance_x,instance_y):
        socket_send_msg = {'OptionRun':'Up','x':instance_x,'y':instance_y}
        socket_return_data = socket_client.send_msg(socket_send_msg)
        return socket_return_data
    
    @staticmethod
    def down(instance_x,instance_y):
        socket_send_msg = {'OptionRun':'Down','x':instance_x,'y':instance_y}
        socket_return_data = socket_client.send_msg(socket_send_msg)
        return socket_return_data
    
    
    @staticmethod
    def left(instance_x,instance_y):
        socket_send_msg = {'OptionRun':'Left','x':instance_x,'y':instance_y}
        socket_return_data = socket_client.send_msg(socket_send_msg)
        return socket_return_data
    
    
    @staticmethod
    def right(instance_x,instance_y):
        socket_send_msg = {'OptionRun':'Right','x':instance_x,'y':instance_y}
        socket_return_data = socket_client.send_msg(socket_send_msg)
        return socket_return_data
    
    
    @staticmethod
    def top_left(instance_x,instance_y):
        socket_send_msg = {'OptionRun':'TopLeft','x':instance_x,'y':instance_y}
        socket_return_data = socket_client.send_msg(socket_send_msg)
        return socket_return_data
    
    
    @staticmethod
    def upper_right(instance_x,instance_y):
        socket_send_msg = {'OptionRun':'UpperRight','x':instance_x,'y':instance_y}
        socket_return_data = socket_client.send_msg(socket_send_msg)
        return socket_return_data
    
    
    @staticmethod
    def bottom_right(instance_x,instance_y):
        socket_send_msg = {'OptionRun':'BottomRight','x':instance_x,'y':instance_y}
        socket_return_data = socket_client.send_msg(socket_send_msg)
        return socket_return_data
    
    
    @staticmethod
    def bottom_left(instance_x,instance_y):
        socket_send_msg = {'OptionRun':'BottomLeft','x':instance_x,'y':instance_y}
        socket_return_data = socket_client.send_msg(socket_send_msg)
        return socket_return_data