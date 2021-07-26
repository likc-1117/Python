#coding:utf-8



with open('D:\\task.xml', 'r+', buffering=1024,encoding='utf-8') as fw:
    data = fw.readlines()
    print(data)
    fw.seek(0)
    fw.truncate()
    fw.writelines(data[1:])