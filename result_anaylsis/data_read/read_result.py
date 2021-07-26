#--coding:utf-8--

import os,json,xlwt,xlrd,numpy
from xlutils.copy import copy
import matplotlib.pyplot as plt
class Read_Result():
    def __init__(self,folder_path,excel_name):
        self.folder_path=folder_path
        self.excel_name=folder_path+'\\'+excel_name+'.xls'



    def result_data(self,filename):
        data_after_split=[]
        filename_open=open(self.folder_path+'\\'+filename,mode='r',encoding='utf-8')
        read_from_file=filename_open.readlines()
        filename_open.close()
        for data in read_from_file:
            d={}
            if 'unlock_rate' in data:
                continue
            for data_split in data.split(';'):
                data_split_again=data_split.split(':',1)
                if data_split_again[0] == 'unlock_times':
                    data_split_again[1]=data_split_again[1][:-1]
                d[data_split_again[0]]=data_split_again[1]
            data_after_split.append(d)
        return data_after_split

    def data_output_excel(self):
        excel_book=xlwt.Workbook(encoding='utf-8')
        filenamelist_in_folder=os.listdir(self.folder_path)
        for filename in filenamelist_in_folder:
            line=1
            sheet_name=excel_book.add_sheet(filename[:-4])
            data_read=self.result_data(filename)
            for data in data_read:
                row=0
                for key,values in data.items():
                    if line==1:
                        sheet_name.write(0,row,key)
                    sheet_name.write(line,row,values)
                    row+=1
                line+=1
            excel_book.save(self.excel_name)





rr=Read_Result('E:\\dust\\Off','Dust_ff')
rr.data_output_excel()





