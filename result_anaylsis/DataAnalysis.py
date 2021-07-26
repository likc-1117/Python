#coding=utf-8
import xlrd
import numpy as np
import pandas


'''读取Excel文件中的内容如步骤如下：
    打开excel文件open_excel=xlrd.open_workbook(filename='')
    定义需要读取的excel中哪一页的内容，页的标号从0开始
    读取excel中的内容sheet_content=self.opera_excel.sheet_by_index(self.sheet_id)
    读取数据，可以读取一整行sheet_content.row(rows),也可以读取指定行列的内容read_excel.sheet_content.cell_value(row,get_run_way())
'''
# def data_read_from_excel():
#     date_check=[]
#     balance=[]
#     open_excel=xlrd.open_workbook('Data_Excel.xls')
#     sheet_content=open_excel.sheet_by_index(0)
#     for rows in range(1,sheet_content.nrows):
#         date_check.append(sheet_content.cell_value(rows,1))
#         balance.append(sheet_content.cell_value(rows,5))
#     return Series(balance,index=date_check)
#
#
#
#
# if __name__=='__main__':
#     print(data_read_from_excel())


































































































#end