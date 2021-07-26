'''
Created on 2019年10月16日

@author: likecan
'''
#coding=utf-8
import configparser
class get_config(object):



    def __init__(self, config_addr=None):
        if config_addr == None:
            self.cofig_addr = '..\\Config\\LocalElement.ini'
        else:
            self.config_addr = config_addr
        self.get_config = configparser.ConfigParser()
        self.get_config.read(self.config_addr, encoding='utf-8')#从给定的配置文件中读取内容，并形成对象
    
    def get_config_by_key(self,key_name):
        for ini_sections in self.get_config.sections():#获取指定配置文件下的所有根节点的名称并返回名称列表（即所有用中括号括起来的内容并形成列表）
            if self.get_config.has_option(ini_sections, key_name):#判断指定关键字在不在某一个根节点中
                return self.get_config.get(ini_sections, key_name)#返回关键字对应的元素信息
        return None
    
    
    def get_config_by_section_key(self,ini_section,key_name):
        if self.get_config.has_option(ini_section, key_name):
            get_config_result = self.get_config.get(ini_section, key_name)
            return get_config_result
        return None
    
    
        
        
    def get_app_information(self,section,app_infor):
        app_return = []
        app_value = self.get_config_by_section_key(section, app_infor)
        if section == 'package':
            app_packge = app_value.split('/')[0]
            app_activity = app_value.split('/')[1]
            app_return.append(app_packge)
            app_return.append(app_activity)
        elif section == 'app':
            app_return.append(app_value)
        return app_return
    
    


    