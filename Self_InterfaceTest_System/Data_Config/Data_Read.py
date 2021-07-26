# -*- coding: utf-8 -*-
'''
Created on 2019年7月30日

@author: likecan
'''
#从测试用例文档总读取测试所需要的数据，包括了URL，Data,Hearder,接口类型，用例编号，用例名称，预期结果
#测试数据可存在三类文件中:Excel、txt、json和sqlite四类文件中
import xlrd

class data_read:
    datafile_sheet=None
    datafile_open=None
    
    def __init__(self,datafile_path,datafile_name,case_type):
        datafile_type = datafile_name.split('.')[1]
        if datafile_type =='xlsx':
            self.datafile_open=xlrd.open_workbook(datafile_path+datafile_name)
            self.datafile_sheet=self.datafile_open.sheet_by_index(case_type.value)
        elif datafile_type.lower()=='txt' or datafile_type.lower()=='json':
            self.datafile_open = open(datafile_path+datafile_name, 'r',encoding='utf-8')
            
            
    def data_read_excel(self):
        data_dict={}
        total_data_list=[]
        datacontent_rows = self.datafile_sheet.nrows
        print('content rows is %s'%str(datacontent_rows))
        title_content=self.datafile_sheet.row(0)
        print('title is %s'%title_content[0].value)
        for rows in range(1,datacontent_rows):
            data_content=self.datafile_sheet.row(rows)#获取指定行额所有内容,返回一个列表
            for cell_index in range(0,len(data_content)):
                data_dict_key = title_content[cell_index].value
                data_dict_value = data_content[cell_index].value
                if data_dict_key == 'Data' or data_dict_key == 'Header':#判断当前是不是取的Data或者Header的值，如果是则将这两个单元格中获取的值处理成字典
                    data_dict_value = self.__str_operation(data_dict_value)
                data_dict[data_dict_key] = data_dict_value
            total_data_list.append(data_dict)
            data_dict={}
        print(total_data_list)
        return total_data_list
    
    
    def __str_operation(self,data):
        if data:
            data_opera_result = {}
            data_first_split = data.split('\n')
            print('data first split %s'%data_first_split)
            for data_content in data_first_split[:-1]:
                data_second_split = data_content.split(':',1)
                data_opera_result_key = data_second_split[0]
                data_opera_result_value = data_second_split[1]
                if data_opera_result_value[:1] == ' ':
                    data_opera_result_value = data_opera_result_value[1:]
                data_opera_result[data_opera_result_key] = data_opera_result_value
            print(data_opera_result)
            return data_opera_result
        return None
        
    

