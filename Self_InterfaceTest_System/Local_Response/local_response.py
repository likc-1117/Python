'''
Created on 2019年8月22日

@author: likecan
'''
import mock

class local_response(object):
    '''
    classdocs
    '''
    def __init__(self,return_data):
        self.return_data = return_data

    def local_res(self):
        mock_data = mock.Mock(return_value = self.return_data)
        return mock_data