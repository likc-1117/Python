'''
Created on 2019年12月2日

@author: likecan
'''
#coding = utf-8
import yaml
class device_config(object):

            
            
    def get_device_infor_from_config(self,device_name):
        '''
        从yaml文件中获取数据
        '''
        with open('..//Config//UserConfig.yaml') as device_infor:
            device_content = yaml.safe_load(device_infor)
        if device_name in device_content.keys():
            return device_content[device_name]
        return None
        
    def set_device_infor_to_config(self,device_name,bootport,port):
        '''
        将设备信息下入到yaml文件中
        '''
        data = {device_name:{'bp':bootport,'port':port}}
        with open('..//Config//UserConfig.yaml','a') as device_infor:
            yaml.safe_dump(data, device_infor)
            
            
    def clear_device_infor_config(self):
        with open('..//Config//UserConfig.yaml','w') as device_infor:
            device_infor.truncate()
    


    



