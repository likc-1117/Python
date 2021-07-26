'''
Created on 2019年9月3日

@author: likecan
'''
from enum import Enum
class total_let_item_index(Enum):
    
    Test_Item = 1
    Max_Delta_Spec = 2
    Max_Delta_Curr = 3
    Max_ResultJudge = 4
    APT_10dBm_Delta_Spec = 5
    APT_10dBm_Delta_Curr = 6
    APT_ResultJudge = 7
    CL_3dBm_Delta_Spec = 8
    CL_3dBm_Delta_Curr = 9
    CL_ResultJudge = 10   
    Min_Spec = 11
    Min_Current = 12
    Min_ResultJudge = 13




#接下来返回LET网络的每个结果列对应的索引值
def get_test_item_index():
    return total_let_item_index.Test_Item.value

def get_max_delta_spec_index():
    return total_let_item_index.Max_Delta_Spec.value

def get_max_delta_curr_index():
    return total_let_item_index.Max_Delta_Curr.value

def get_max_result_judge_index():
    return total_let_item_index.Max_ResultJudge.value

def get_apt_10dbm_delta_spec_index():
    return total_let_item_index.APT_10dBm_Delta_Spec.value

def get_apt_10dbm_delta_curr_index():
    return total_let_item_index.APT_10dBm_Delta_Curr.value

def get_apt_result_judge_index():
    return total_let_item_index.APT_ResultJudge.value

def get_cl_3dbm_delta_spec_index():
    return total_let_item_index.CL_3dBm_Delta_Spec.value

def get_cl_3dbm_delta_curr_index():
    return total_let_item_index.CL_3dBm_Delta_Curr.value

def get_cl_result_judge_index():
    return total_let_item_index.CL_ResultJudge.value

def get_min_spec_index():
    return total_let_item_index.Min_Spec.value

def get_min_curr_index():
    return total_let_item_index.Min_Current.value

def get_min_result_judge_index():
    return total_let_item_index.Min_ResultJudge.value




