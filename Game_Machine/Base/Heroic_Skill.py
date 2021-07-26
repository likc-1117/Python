# -*- coding: utf-8 -*-
'''
Created on 2019年9月19日

@author: likecan
'''

from Base.Socket import socket_client

class heroic_skill():
    
    @staticmethod
    def flat_a():
        socket_send_msg = {'OptionRun':'FlatA'}
        socket_return_data = socket_client.send_msg(socket_send_msg)
        return socket_return_data
    
    
    @staticmethod
    def skill_one(point_x,point_y,depth):
        socket_send_msg = {'OptionRun':'Skill1','x':point_x,'y':point_y,'depth':depth}
        socket_return_data = socket_client.send_msg(socket_send_msg)
        return socket_return_data
    
    @staticmethod
    def skill_two(point_x,point_y,depth):
        socket_send_msg = {'OptionRun':'Skill2','x':point_x,'y':point_y,'depth':depth}
        socket_return_data = socket_client.send_msg(socket_send_msg)
        return socket_return_data
    
    @staticmethod
    def skill_three(point_x,point_y,depth):
        socket_send_msg = {'OptionRun':'Skill3','x':point_x,'y':point_y,'depth':depth}
        socket_return_data = socket_client.send_msg(socket_send_msg)
        return socket_return_data
    
    @staticmethod
    def skill_plus_one(point_x,point_y,depth):
        socket_send_msg = {'OptionRun':'SkillPlus1','x':point_x,'y':point_y,'depth':depth}
        socket_return_data = socket_client.send_msg(socket_send_msg)
        return socket_return_data
    
    @staticmethod
    def skill_plus_two(point_x,point_y,depth):
        socket_send_msg = {'OptionRun':'SkillPlus2','x':point_x,'y':point_y,'depth':depth}
        socket_return_data = socket_client.send_msg(socket_send_msg)
        return socket_return_data
    
    @staticmethod
    def skill_plus_three(point_x,point_y,depth):
        socket_send_msg = {'OptionRun':'SkillPlus3','x':point_x,'y':point_y,'depth':depth}
        socket_return_data = socket_client.send_msg(socket_send_msg)
        return socket_return_data