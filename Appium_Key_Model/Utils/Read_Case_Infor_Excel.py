'''
Created on 2020年3月23日

@author: likecan
'''
import xlrd
from xlutils3.copy import copy
class read_case_infor_excel(object):
    '''
    classdocs
    '''

    def __init__(self,sheet_name, case_excel_path = '..\\Config\\Case.xls'):
        self.excel_path = case_excel_path
        self.open_excel = xlrd.open_workbook(case_excel_path)#打开指定路径下的excel文件
        self.sheet_names = self.open_excel.sheet_names()
        self.sheet_content = self.open_excel.sheet_by_name(sheet_name)#根据索引获取指定索引下的sheet内容

    def get_sheet_names(self):
        '''
        获取excel中的sheet名称
        :return:
        '''
        return self.sheet_names

    def get_all_content_from_excel(self):
        '''
        获取excel中的所有内容
        :return:
        '''
        row_num=self.sheet_content.nrows#获取sheet中的总行数
        row_content=[]
        for rows in range(1,row_num):
            row_content.append(self.sheet_content.row(rows))
        return row_content

    def get_cell_content(self,row_num,col_num):
        '''
        获取指定行列的单元值
        :param row_num:
        :param col_num:
        :return:
        '''
        return self.sheet_content.cell(row_num,col_num).value

    def get_excel_row_num(self):
        '''
        获取excel的行数
        :return:
        '''
        return self.sheet_content.nrows


    def set_cell_data(self,row_num,set_value):
        set_data = copy(self.open_excel)
        set_data_save = set_data.get_sheet(0)
        set_data_save.write(row_num,10,set_value)
        set_data_save.save(self.excel_path)
