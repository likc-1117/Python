# -*- coding: utf-8 -*-
'''
Created on 2019年9月3日

@author: likecan
'''
from enum import Enum

class part_result_item_index(Enum):
    Network = 0
    Band = 1
    #实测功率
    Measured_Power_LCH = 2
    Measured_Power_MCH = 3
    Measured_Power_HCH = 4
    #实测整机电流
    Measured_Current_LCH = 5
    Measured_Current_MCH = 6 
    Measured_Current_HCH = 7  
    Spectrum_Switching_LCH = 8   
    Spectrum_Switching_MCH = 9
    Spectrum_Switching_HCH = 10   
    #归一化功率
    Normalized_Power_LCH = 11
    Normalized_Power_MCH = 12   
    Normalized_Power_HCH = 13    
    Whole_Avg_Current = 14    
    Integration_Rate = 15    
    Whole_Integration_Current = 16 
    Whole_PA_Current = 17  
    Benchmark_PA_Integral_Curren = 18
    PLC_OR_Judgement = 19
    
    
def get_network_index():
    return part_result_item_index.Network.value

def get_band_index():
    return part_result_item_index.Band.value

def get_measured_power_lch_index():
    return part_result_item_index.Measured_Power_LCH.value

def get_measured_power_mch_index():
    return part_result_item_index.Measured_Power_MCH.value

def get_measured_power_hch_index():
    return part_result_item_index.Measured_Power_HCH.value

def get_measured_current_lch_index():
    return part_result_item_index.Measured_Current_LCH.value

def get_measured_current_mch_index():
    return part_result_item_index.Measured_Current_MCH.value

def get_measured_current_hch_index():
    return part_result_item_index.Measured_Current_HCH.value

def get_spectrum_switching_lch_index():
    return part_result_item_index.Spectrum_Switching_LCH.value

def get_spectrum_switching_mch_index():
    return part_result_item_index.Spectrum_Switching_MCH.value

def get_spectrum_switching_hch_index():
    return part_result_item_index.Spectrum_Switching_HCH.value

def get_normalized_power_lch_index():
    return part_result_item_index.Normalized_Power_LCH.value

def get_normalized_power_mch_index():
    return part_result_item_index.Normalized_Power_MCH.value

def get_normalized_power_hch_index():
    return part_result_item_index.Normalized_Power_HCH.value

def get_whole_ave_current_index():
    return part_result_item_index.Whole_Avg_Current.value

def get_integration_rate_index():
    return part_result_item_index.Integration_Rate.value

def get_whole_integrtion_current_index():
    return part_result_item_index.Whole_Integration_Current.value

def get_whole_pa_current_index():
    return part_result_item_index.Whole_PA_Current.value

def get_benchmark_pa_integral_current_index():
    return part_result_item_index.Benchmark_PA_Integral_Curren.value

def get_plc_or_judgement():
    return part_result_item_index.PLC_OR_Judgement.value