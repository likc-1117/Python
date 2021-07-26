# coding=utf-8


# import pymysql
#
# mysql_connect = pymysql.Connect(host='127.0.0.1', port=3306, user='root', passwd='limoyi180801', db='room',
#                                 charset='utf8')
# mysql_cursor = mysql_connect.cursor()
# mysql_cursor.execute('explain select * from price_trend order by Price')
# print(mysql_cursor.fetchone())
# mysql_cursor.close()
# mysql_connect.close()
name = 0
import os
file_path = 'E:\\Face人脸设备\\Face\\bin\\x64\\Debug\\lockimgs\\lockimgs\\'
path = os.listdir(file_path)
for i in path:
    old_name = file_path + os.sep + str(path[name])
    print(old_name)
    if name < 10:
        new_n = '000'+str(name)+'_img.bmp'
    elif name > 99:
        new_n = '0'+str(name)+'_img.bmp'
    else:
        new_n = '00'+str(name)+'_img.bmp'
    new_name = file_path + os.sep + new_n
    print(new_name)
    os.rename(old_name,new_name)
    name += 1
print(path)