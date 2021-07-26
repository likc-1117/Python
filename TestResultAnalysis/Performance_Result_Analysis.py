# coding=utf-8
import re
import os

filenames = os.listdir('./Data')
log_file_content = ''
total_result = {}
for filename in filenames[::-1]:
    log_file_content += open('./Data/{0}'.format(filename), mode='r').read()
re_result = re.findall(r'\d+匹配.+[:：]0\.\d+', log_file_content)
# open('./Result/result.txt', mode='a+').writelines(str(re_result))
filenames = os.listdir('./Result')
if filenames:
    for name in filenames:
        os.remove('./Result/'+name)
f = open('./Result/analysis.txt', mode='a+')
num = 1
i = 0
while i < len(re_result) - 1:
    if i + 1 > len(re_result) - 1:
        break
    fps_num = re.findall(r'\d+', re_result[i])[0]
    result = re.findall(r'0\.\d+', re_result[i])[0]
    if float(result) > 0.85:
        total_result[num] = [re_result[i - 1], re_result[i], re_result[i + 1]]
        f.writelines(str([re_result[i - 1], re_result[i], re_result[i + 1]])+'\n')
        i += 2
        num += 1
    else:
        i += 1
print(total_result)
