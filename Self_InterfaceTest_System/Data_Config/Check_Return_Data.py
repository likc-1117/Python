'''
Created on 2019年8月22日

@author: likecan
'''


class check_return_data(object):
    '''
    classdocs
    '''


    def check_return_data_by_str(self,repect_data,return_data):
        flag = None
        if repect_data in return_data:
            flag = True
        else:
            flag = False
        return flag
            