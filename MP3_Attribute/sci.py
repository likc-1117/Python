from numpy.ma.core import where
import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.io.wavfile import write

# 加载音频文件
def load_wav(file):
    sampling_rate, wavsignal = wav.read(file)
    return sampling_rate, wavsignal
# 录音
def record_audio(file,record_time):
    """采集语音数据
    Args:
        file: 语音数据存放的文件.
        record_time: 采样时间（s）.
    Returns:
        None
    """
    fs = 44100
    print('查询设备：')
    print(sd.query_devices())
    # 设置默认设备
    sd.default.device = 'Analog (1+2) (RME Fireface UCX), MME'
    print('使用设备：')
    print(sd.default.device)
    # 录音
    duration = record_time  # seconds
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2,dtype='int16')

    sd.wait()
    write(file, fs, myrecording)

def is_silence(sampling_rate, wavsignal, channel_id,threshold=200):
    """是否静音 给出指定的声道
    Args:
        sampling_rate: 采样率.
        wavsignal: 声音数据.
        channel_id: 通道id.
        threshold: 静音阈值.
    Returns:
        True 静音，False，有声音
    """
    if channel_id < wavsignal.shape[1]:
        channel_wav = wavsignal[:,channel_id]
    else:
        print('通道数越界')
        exit()
    channel_wav = channel_wav[:,np.newaxis]
    res = detect_silence(sampling_rate,channel_wav,threshold)
    return True if len(res[0]) > 0  else False

def has_voice(sampling_rate, wavsignal, channel_id,threshold=200):
    """是否静音 给出指定的声道
    Args:
        sampling_rate: 采样率.
        wavsignal: 声音数据.
        channel_id: 通道id.
        threshold: 静音阈值.
    Returns:
        True 有声，False，无声
    """
    if channel_id < wavsignal.shape[1]:
        channel_wav = wavsignal[:,channel_id]
    else:
        print('通道数越界')
        exit()
    cha_1 = np.abs(channel_wav)
    min_pause_time = sampling_rate//1000

    j = min_pause_time
    while j < len(cha_1):
        clip = cha_1[j-min_pause_time:j]
        if clip.max() > threshold:
            return True
        j += min_pause_time
    return False
    

def detect_silence_by_channel(sampling_rate, wavsignal, channel_id, threshold=200):
    """静音检测 给出指定的声道
    Args:
        sampling_rate: 采样率.
        wavsignal: 声音数据.
        channel_id: 通道id.
        threshold: 静音阈值.
    Returns:
        返回静音时间段
    """
    if channel_id < wavsignal.shape[1]:
        channel_wav = wavsignal[:,channel_id]
    else:
        print('通道数越界')
        exit()
    channel_wav = channel_wav[:,np.newaxis]
    return detect_silence(sampling_rate,channel_wav,threshold)


def detect_silence(sampling_rate, wavsignal,threshold=200):
    """静音检测
    Args:
        sampling_rate: 采样率.
        wavsignal: 声音数据.
        threshold: 静音阈值.
    Returns:
        返回静音时间段,包含若干个通道
    """
    min_pause_time = sampling_rate//10
    abs_sig = np.abs(wavsignal)
    res = []
    #双通道
    for i in range(abs_sig.shape[1]): #通道个数
        cha_1 = abs_sig[:,i]
        j = min_pause_time
        channel = []
        while j < len(cha_1):
            clip = cha_1[j-min_pause_time:j]
            if clip.max() < threshold:
                start = j-min_pause_time
                channel.append([start,j])
            j += min_pause_time
        res.append(channel)

    # 转为时间并合并间隙
    result = merge_gap(res)
    for channel in result:
        i = 0
        n = len(channel)
        while i < n:
            if channel[i][1] - channel[i][0] < 1:
                channel.pop(i)
                n -= 1
            else:
                i += 1
    return result


def detect_pause_by_channel(sampling_rate, wavsignal, channel_id, rate=0.035):
    """给出指定的声道 的静音检测结果
    Args:
        sampling_rate: 采样率.
        wavsignal: 声音数据.
        channel_id: 通道id.
        rate:  波峰与波谷差占最大值的比例 默认0.035
    Returns:
        返回静音时间段
    """
    if channel_id < wavsignal.shape[1]:
        channel_wav = wavsignal[:,channel_id]
    else:
        print('通道数越界')
        exit()
    channel_wav = channel_wav[:,np.newaxis]
    return detect_pause_2(sampling_rate,channel_wav,rate)
# 卡顿检测
def detect_pause_2(sampling_rate, wavsignal, rate=0.035):
    '''
    通过计算波峰和波谷之间的差距，差距小于某个阈值，认为是卡顿
    Args:
        sampling_rate: 采样率.
        wavsignal: 声音数据.
        channel_id: 通道id.
        rate:  波峰与波谷差占最大值的比例 默认0.035
    Returns:
        返回静音时间段
    '''
    diff = int(rate*sampling_rate)
    min_pause_time = sampling_rate//1000
    slient = 10
    # 双通道
    res = []
    for i in range(wavsignal.shape[1]): # 通道个数
        cha_1 = wavsignal[:,i]
        j = min_pause_time
        channel = []
        while j < len(cha_1):
            clip = cha_1[j-min_pause_time:j]
            if clip.max() - clip.min() < diff and clip.max() - clip.min() > slient:
                start = j-min_pause_time
                
                channel.append([start,j])
            j += min_pause_time
        res.append(channel)
    # 转为时间并合并间隙
    
    result = merge_gap(res,15000)
    if result and result[0] and result[0][0][0] < 0.1:
        result[0].pop(0)
    if len(result) == 2 and result[1] and result[1][0][0] < 0.1:
        result[1].pop(0)
    for channel in result:
        i = 0
        n = len(channel)
        while i < n:
            if channel[i][1] - channel[i][0] > 1:
                channel.pop(i)
                n -= 1
            else:
                i += 1
    return result

def detect_pause_by_normalize(sampling_rate, wavsignal, rate=0.035):
    '''
    通过计算波峰和波谷之间的差距，差距小于某个阈值，认为是卡顿
    Args:
        sampling_rate: 采样率.
        wavsignal: 声音数据.
        channel_id: 通道id.
        rate:  波峰与波谷差占最大值的比例 默认0.035
    Returns:
        返回静音时间段
    '''
    diff = rate
    
    min_pause_time = sampling_rate//100
    slient = 0.001
    # 双通道
    res = []
    for i in range(wavsignal.shape[1]): # 通道个数
        
        cha_1 = wavsignal[:,i]
        normal_size = (abs(cha_1.max())+abs(cha_1.min()))/2
        simple_channel = cha_1 / normal_size
        j = min_pause_time
        channel = []
        while j < len(simple_channel):
            clip = simple_channel[j-min_pause_time:j]
            if clip.max() - clip.min() < diff and clip.max() - clip.min() > slient:
                start = j-min_pause_time
                
                channel.append([start,j])
            j += min_pause_time
        res.append(channel)
    # 转为时间并合并间隙
    
    result = merge_gap(res,15000)
    if result and result[0] and result[0][0][0] < 0.1:
        result[0].pop(0)
    if len(result) == 2 and result[1] and result[1][0][0] < 0.1:
        result[1].pop(0)
    for channel in result:
        i = 0
        n = len(channel)
        while i < n:
            if channel[i][1] - channel[i][0] > 1:
                channel.pop(i)
                n -= 1
            else:
                i += 1
    return result

def detect_noise_by_channel(sampling_rate, wavsignal, channel_id):
    """给出指定的声道 的静音检测结果
    Args:
        sampling_rate: 采样率.
        wavsignal: 声音数据.
        channel_id: 通道id.
    Returns:
        返回静音时间段
    """
    if channel_id < wavsignal.shape[1]:
        channel_wav = wavsignal[:,channel_id]
    else:
        print('通道数越界')
        exit()
    channel_wav = channel_wav[:,np.newaxis]
    return detect_noise2(sampling_rate,channel_wav)
# 噪音检测
def detect_noise2(sampling_rate,wavsignal):
    '''
    只针对固定正弦波，波峰一般固定不变，如果有噪声的话，那么波峰就会
    发生变化，
    通过计算波峰的方差，来判断是否有噪音，如果没有其它噪音，方差就会很小，反之方差很大
    '''
    min_pause_time = sampling_rate//100
    res = []
    for i in range(wavsignal.shape[1]): # 通道个数
        cha_1 = wavsignal[:,i]
        j = min_pause_time
        channel = []
        while j < len(cha_1):
            clip = cha_1[j-min_pause_time:j]
            max_value = clip.max()
            channel.append(np.array([j-min_pause_time,max_value]))
            j += min_pause_time
        res.append(channel)
    inter = 500
    result = []
    for cha_1 in res:
        
        cha_1 = np.array(cha_1)
        j = inter
        sub_channel = []
        while j < len(cha_1):
            clip = cha_1[j-inter:j,:]
            clip_var = np.var(clip[:,1])
            if clip_var > 600000000:
                sub_channel.append([clip[0][0],clip[-1][0]])
            j += inter
        result.append(sub_channel)
    ans = merge_gap(result)
    return ans





def merge_gap(res,gap = 5000):
    """给出指定的声道 的静音检测结果
    Args:
        res: 很多个.
        gap: 合并间隙帧数.
    Returns:
        返回静音时间段
    """
    reslut = []
    # gap = 10000
    for channel in res:
        if len(channel) == 0:
            reslut.append([])
            continue
        i = 0
        sub_res = []
        start = 0
        while i < len(channel)-1:
            if channel[i+1][0] - channel[i][1] < gap:
                i += 1
            else:
                
                sub_res.append([round(channel[start][0]/sampling_rate,2),round(channel[i][1]/sampling_rate,2)])
                i += 1
                start = i
        sub_res.append([round(channel[start][0]/sampling_rate,2),round(channel[i][1]/sampling_rate,2)])
        reslut.append(sub_res)
    
    return reslut


def match(file):
    '''
    语音匹配
    '''
    sampling_rate, wavsignal = wav.read(file)
    _,temp_disconnect = wav.read('sin2.wav')
    temp_len = len(temp_disconnect)
    wavsignal_len = len(wavsignal)
    wavsignal = wavsignal / wavsignal.max()
    temp_disconnect = temp_disconnect/temp_disconnect.max()
    for i in range(temp_len,wavsignal_len+1):
        diff = np.abs(temp_disconnect-wavsignal[i-temp_len:i,:])
        avg = np.mean(diff)
        if avg < 0.1:
            return True
    return False             



import argparse
parser = argparse.ArgumentParser(description="WAVE")
#parser.add_argument('--wavfile', type=str, default='record.wav',help='wav path')
parser.add_argument('--time', type=int, default=30,help='录音时间,单位s')

args = parser.parse_args()
if __name__ == '__main__':
    file = 'output-2021-07-26-20-43-32.wav'
    time = args.time
    print(time)
    # record_audio(file,time)
    sampling_rate, wavsignal = load_wav(file=file)
    # wavdata = wavsignal / (2**16-1)
    wavdata = np.array(wavsignal,dtype='int32')
    wavdata = wavdata * 100
    if len(wavdata.shape) < 2:
        wavdata = wavdata[:,np.newaxis]
    
    
    
    # 针对某一通道 进行检测
    res_silent_1 = has_voice(sampling_rate,wavdata,0,threshold=50)
    print('是否有声------------------------')
    print(res_silent_1)

    print('静音检测---------------------------------')
    res_silent = detect_silence(sampling_rate,wavdata,threshold=50)
    for i in range(len(res_silent)):
        print('{0}通道：{1}'.format(i,res_silent[i]))
        print('总段数:{0}'.format(len(res_silent[i])))

    print('卡顿检测---------------------------------')
    res_pause = detect_pause_2(sampling_rate,wavdata,rate=0.025)
    for i in range(len(res_pause)):
        print('{0}通道：{1}'.format(i,res_pause[i]))
        print('总段数:{0}'.format(len(res_pause[i])))

    print('卡顿检测2---------------------------------')
    res_pause_2 = detect_pause_by_normalize(sampling_rate,wavdata,rate=0.01)
    for i in range(len(res_pause_2)):
        print('{0}通道：{1}'.format(i,res_pause_2[i]))
        print('总段数:{0}'.format(len(res_pause_2[i])))
    

    print('噪音检测---------------------------------')
    res_noise = detect_noise2(sampling_rate,wavdata)
    for i in range(len(res_noise)):
        print('{0}通道：{1}'.format(i,res_noise[i]))
        print('总段数:{0}'.format(len(res_noise[i])))
