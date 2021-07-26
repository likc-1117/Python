'''
Created on 2020年5月14日

@author: likecan
'''
#coding = utf-8
from enum import Enum
class case_item(Enum):
    case_id = 0#用例id
    is_run = 1#是否运行
    request_type = 2#请求类型
    request_url = 3#URL
    request_data = 4#请求数据
    request_header = 5#请求时的header
    request_cookie = 6#请求时的cookie
    dependent_case_id = 7#依赖用例id
    dependent_data = 8#依赖数据
    dependent_data_item = 9#依赖数据的字段
    expect_result = 10#预期结果
    actual_result = 11#实际结果

class case_item_handle(object):
    def case_id(self):
        return int(case_item.case_id.value)


    def is_run(self):
        return int(case_item.is_run.value)

    def request_type(self):
        return int(case_item.request_type.value) 

    def request_url(self):
        return int(case_item.request_url.value)


    def request_data(self):
        return int(case_item.request_data.value)


    def request_header(self):
        return int(case_item.request_header.value) 

    def request_cookie(self):
        return int(case_item.request_cookie.value)


    def dependent_case_id(self):
        return int(case_item.dependent_case_id.value)

    def dependent_data(self):
        return int(case_item.dependent_data.value) 

    def dependent_data_item(self):
        return int(case_item.dependent_data_item.value)

    def expect_result(self):
        return int(case_item.expect_result.value)

    def actual_result(self):
        return int(case_item.actual_result.value)



