'''
Created on 2020年5月14日

@author: likecan
'''
#coding = utf-8
import xlrd

class case_doucument_handle(object):
    '''
    classdocs
    '''


    def __init__(self, case_file_path = './Data/Interface_Case.xlsx'):
        '''
        Constructor
        '''
        open_excel = xlrd.open_workbook(filename=case_file_path)
        self.get_sheet_content = open_excel.sheet_by_index(0)
        self.total_row = self.get_sheet_content.nrows

    def get_row_num(self,case_id):
        total_rows = self.get_sheet_content.nrows
        print(total_rows)
        for row in range(1,total_rows):
            if case_id == self.get_sheet_content.cell_value(row,0):
                return row
        
        
    
    def get_cell_content(self,row,colum):
        '''
        根据列数获取单元格内容
        '''
        cell_content = self.get_sheet_content.cell_value(row,colum)
        if cell_content == '' or cell_content == 'None':
            return None
        return cell_content
    

    
    
    
class data_handle(object):
    
    
    def data_to_dict(self,data):
        '''
        将传入的数据转换成字典，主要针对header，cookie，请求数据等
        '''
        data_dict = {}
        if not isinstance(data,str) or not data:
            return data
        data_list = data.split('\n')
        # print(data_list)
        for d in data_list:
            if d != '':
                data_dict[d.split(' ',1)[0]] = d.split(' ',1)[1][1:]
        return data_dict

# import sys
# sys.path.append('./')
# from Json_File_Handle.Json_File_Read import json_file_read
# jf_read = json_file_read()
# case_d = case_doucument_handle()
# data_h = data_handle()
# data = []
# for r in range(1,case_d.total_row):
#     data.append({case_d.get_cell_content(r,0):case_d.get_cell_content(r,4)})
# jf_read.send_request_result_data_to_json('Request_Data',data,'Request_Data.json')
# jf_read.read_content_from_json('','Request_Data')