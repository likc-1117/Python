# -*- coding: utf-8 -*-
import xlrd,xlwt,os
from xlutils.copy import copy

class OperationExcel:
    def __init__(self,excelpath=None,sheet_id=None):
        if not excelpath:
            self.excelpath='..\\'
        else:
            self.excelpath=excelpath
        if not sheet_id:
            self.sheet_id=0
        else:
            self.sheet_id=sheet_id
        self.opera_excel=xlrd.open_workbook(filename=self.excelpath+'tem_result.xlsx')
        #sheet_table_content=opera_excel.sheet_names()[0]
        self.sheet_content=self.opera_excel.sheet_by_index(self.sheet_id)
        #content_rows_num=self.sheet_content.nrows-1
        #print(self.sheet_content.col_values(1,start_rowx=1,end_rowx=content_rows_num))



    def read_content_by_row(self,row='ALL'):
        row_num=self.sheet_content.nrows
        row_content=[]
        if str(row).upper() == 'ALL':
            for rows in range(row_num):
                row_content.append(self.sheet_content.row(rows))
        else:
            row_content.append(self.sheet_content.row(row))
        for subContent in row_content:
            print(str((subContent[0].value)).split('=')[-1][:-1])
        return row_content


if __name__=='__main__':
    excel_op=OperationExcel('C:\\Users\\likecan\\Desktop\\',1)
    print(excel_op.read_content_by_row('ALL'))