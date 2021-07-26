'''
Created on 2019年9月3日

@author: likecan
'''
from enum import Enum
class total_wcdma_item_index(Enum):
    Max_Delta_Spec = 0
    Max_Delta_Curr = 1
    Max_ResultJudge = 2  
    Min_Spec = 3
    Min_Current = 4
    Min_ResultJudge = 5

#接下来返回wcdma网络的每个结果列对应的索引值
def get_max_delta_spec_index():
    return total_wcdma_item_index.Max_Delta_Spec.value

def get_max_delta_curr_index():
    return total_wcdma_item_index.Max_Delta_Curr.value

def get_max_result_judge_index():
    return total_wcdma_item_index.Max_ResultJudge.value

def get_min_spec_index():
    return total_wcdma_item_index.Min_Spec.value

def get_min_curr_index():
    return total_wcdma_item_index.Min_Current.value

def get_min_result_judge_index():
    return total_wcdma_item_index.Min_ResultJudge.value




