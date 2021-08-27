import scipy.io.wavfile as wav
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
import argparse
from collections import Counter
from functools import reduce

# 加载音频文件


def load_wav(file):
    sampling_rate, wavsignal = wav.read(file)
    # print('sampling_rate:{0}'.format(sampling_rate))
    # print('wavsignal:{0}'.format(wavsignal))
    return sampling_rate, wavsignal


# 录音
def record_audio(file, record_time):
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
    sd.default.device = 'Analog (3+4) (RME Fireface UCX), MME'
    print('使用设备：')
    print(sd.default.device)
    # 录音
    duration = record_time  # seconds
    myrecording = sd.rec(int(duration * fs), samplerate=fs,
                         channels=2, dtype='int16')

    sd.wait()
    write(file, fs, myrecording)


def is_silence(sampling_rate, wavsignal, channel_id, threshold=200):
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
        channel_wav = wavsignal[:, channel_id]
    else:
        print('通道数越界')
        exit()
    channel_wav = channel_wav[:, np.newaxis]
    res = detect_silence(sampling_rate, channel_wav, threshold)
    return True if len(res[0]) > 0 else False


def split(arr:list, size:int) -> list:
    """将数组按等长切分, 最后一段可以不按要求长度

    Args:
        arr (list): 原始数组
        size (int): 每段数组的长度

    Returns:
        [list]: 切割后的数组
    """    
    arrs = []
    while len(arr) > size:
        pice = arr[:size]
        arrs.append(pice)
        arr = arr[size:]
    arrs.append(arr)
    return arrs


def has_voice(sampling_rate, wavsignal, channel_id, threshold=200):
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
        channel_wav = wavsignal[:, channel_id]
    else:
        print('通道数越界')
        exit()

    # # 绝对值化
    # cha_1 = np.abs(channel_wav)
    # # 最小静音时间
    # min_pause_time = 0.01
    # # 最小静音帧数
    # min_pause_frame = int(min_pause_time * sampling_rate)
    # # 切分成最小静音时间片段后，判断是否有声音
    # has_voice_list = [x.max() > threshold for x in split(cha_1, min_pause_frame)]

    # # 有声音的片段数量
    # has_voice_count = Counter(has_voice_list)[True]

    # # 有声音的片段数量是否超过1秒
    # return has_voice_count > 1 / min_pause_time

    # 根据阈值 1/0化
    has_voice_list = np.abs(channel_wav) > threshold
    # True的总量大于1秒
    return Counter(has_voice_list)[True] > sampling_rate


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
        channel_wav = wavsignal[:, channel_id]
    else:
        print('通道数越界')
        exit()
    channel_wav = channel_wav[:, np.newaxis]
    return detect_silence(sampling_rate, channel_wav, threshold)


def detect_silence(sampling_rate, wavsignal, threshold=200):
    """静音检测
    Args:
        sampling_rate: 采样率.
        wavsignal: 声音数据.
        threshold: 静音阈值.
    Returns:
        返回静音时间段,包含若干个通道
    """
    min_pause_time = sampling_rate//1000
    abs_sig = np.abs(wavsignal)
    res = []
    # 双通道
    # for i in range(abs_sig.shape[1]):
    #     cha_1 = abs_sig[:, i]
    #     # silence_list = [x.max() < threshold and abs(x.min()) < threshold for x in split(cha_1, min_pause_time)]
    #     # ch = [[index * min_pause_time, (index + 1) * min_pause_time] for index, v in enumerate(silence_list) if v == True]

    #     # 阈值化
    #     silence_list2 = (abs(cha_1) < threshold)
    #     zzz = [(i,(list(v)).count(i)) for i,v in groupby(silence_list2)]
    #     print(len(zzz))
    #     print(zzz[:20])

    for i in range(abs_sig.shape[1]):  # 通道个数
        cha_1 = abs_sig[:, i]
        j = min_pause_time
        channel = []
        while j < len(cha_1):
            clip = cha_1[j - min_pause_time:j]
            if clip.max() < threshold and abs(clip.min()) < threshold:
                start = j - min_pause_time
                j += min_pause_time
                while j < len(cha_1) and cha_1[j] < threshold:
                    j += min_pause_time
                channel.append([start, j])
            j += min_pause_time
        # print(channel[:20])
        res.append(channel)
    # 转为时间并合并间隙
    result = merge_gap(res, 500)

    # 只保留 >= 0.4秒的数据
    for channel in result:
        yield [ch for ch in channel if ch[1] - ch[0] >= 1]


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
        channel_wav = wavsignal[:, channel_id]
    else:
        print('通道数越界')
        exit()
    channel_wav = channel_wav[:, np.newaxis]
    return detect_pause_2(sampling_rate, channel_wav, rate)


# 卡顿检测
def detect_pause_2(sampling_rate, wavsignal, rate=0.035, min_length=0, max_length=1):
    '''
    通过计算波峰和波谷之间的差距，差距小于某个阈值，认为是卡顿
    Args:
        sampling_rate: 采样率.
        wavsignal: 声音数据.
        channel_id: 通道id.
        rate:  波峰与波谷差占最大值的比例 默认0.035
    Returns:
        返回卡顿时间段
    '''
    diff = int(rate * sampling_rate)
    min_pause_time = sampling_rate // 1000
    slient = 10
    # 双通道
    res = []
    for i in range(wavsignal.shape[1]):  # 通道个数
        cha_1 = wavsignal[:, i]
        j = min_pause_time
        channel = []
        while j < len(cha_1):
            clip = cha_1[j - min_pause_time:j]
            if clip.max() - clip.min() < diff:  # and clip.max() - clip.min() > slient:
                start = j - min_pause_time
                channel.append([start, j])
            j += min_pause_time
        res.append(channel)
    # 转为时间并合并间隙

    result = list(merge_gap(res, 700))
    # 只保留小于等于1秒的数据
    for channel in result:
        yield [ch for ch in channel if min_length < ch[1] - ch[0] < max_length]


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
        channel_wav = wavsignal[:, channel_id]
    else:
        print('通道数越界')
        exit()
    channel_wav = channel_wav[:, np.newaxis]
    return detect_noise2(sampling_rate, channel_wav)


# 噪音检测
def detect_noise2(sampling_rate, wavsignal):
    '''
    只针对固定正弦波，波峰一般固定不变，如果有噪声的话，那么波峰就会
    发生变化，
    通过计算波峰的方差，来判断是否有噪音，如果没有其它噪音，方差就会很小，反之方差很大
    '''

    # 最小间隔时间(秒)
    min_pause_time = 0.01
    # 最小间隔的帧数
    min_pause_frame = int(sampling_rate * min_pause_time)

    res = []
    for i in range(wavsignal.shape[1]):  # 通道个数
        # 按最短停顿时间等分， 并去掉最后一个元素
        splited_data = split(wavsignal[:, i], min_pause_frame)
        # 返回当前坐标和最大值的数组
        channel = [np.array([j * min_pause_frame, v.max()]) for j, v in enumerate(splited_data)]

        res.append(channel)

    # 噪音检测时间(秒)
    interval_time = 0.2
    # 噪音检测的片段数量
    interval_segment = int(interval_time / min_pause_time)
    result = []

    for cha_1 in res:
        splited_cha_1 = split(cha_1, interval_segment)

        sub_channel = []
        for chip in splited_cha_1:
            chip = np.array(chip)
            # 计算方差
            variance = np.var(chip[:,-1])
            sub_time = [chip[0][0], chip[-1][0]]
            # print('variance={:.3e}, sub_time={}, actual_time={}'.format(variance, sub_time, [round(sub_time[0] / 44100, 3), round(sub_time[1] / 44100, 3)]))
            # 如果方差大于一定值, 就视为噪音
            if variance > 5.2e+4:                
                sub_channel.append([chip[0][0], chip[-1][0]])        
        
        result.append(sub_channel)


    return merge_gap(result)



def merge_gap(res, gap=5000, sampling=44100):
    """给出指定的声道 的静音检测结果
    Args:
        res: 很多个.
        gap: 合并间隙帧数.
        sampling: 帧率.
    Returns:
        返回静音时间段
    """

    for channel in res:
        sub_res = []
        if len(channel) > 0:
            start = 0
            for i in range(len(channel) - 1):
                if channel[i+1][0] - channel[i][1] >= gap:
                    sub_res.append([channel[start][0], channel[i][1]])
                    start = i + 1
            sub_res.append([channel[start][0], channel[-1][1]])

        yield [[round(v[0] / sampling, 3), round(v[1] / sampling, 3)] for v in sub_res]


def merge_gap2(res, gap=5000):
    """给出指定的声道 的静音检测结果
    Args:
        res: 很多个.
        gap: 合并间隙帧数.
    Returns:
        返回静音时间段
    """
    result = []
    # gap = 10000
    for channel in res:
        if len(channel) == 0:
            result.append([])
            continue
        i = 0
        sub_res = []
        start = 0
        while i < len(channel)-1:
            if channel[i+1][0] - channel[i][1] < gap:
                i += 1
            else:
                sub_res.append(
                    [round(channel[start][0]/sampling_rate, 2), round(channel[i][1]/sampling_rate, 2)])
                i += 1
                start = i
        print('i={}'.format(i))
        print('channel len = {}'.format(len(channel)))
        sub_res.append([round(channel[start][0]/sampling_rate, 2),
                        round(channel[i][1]/sampling_rate, 2)])
        result.append(sub_res)
    return result


def match(file):
    '''
    语音匹配
    '''
    _, wavsignal = wav.read(file)
    _, temp_disconnect = wav.read('sin2.wav')
    temp_len = len(temp_disconnect)
    wavsignal_len = len(wavsignal)
    wavsignal = wavsignal / wavsignal.max()
    temp_disconnect = temp_disconnect/temp_disconnect.max()
    for i in range(temp_len, wavsignal_len+1):
        diff = np.abs(temp_disconnect-wavsignal[i-temp_len:i, :])
        avg = np.mean(diff)
        if avg < 0.1:
            return True
    return False


def not_include(list_a: list, list_b: list):
    """判断列表A是否在列表B的范围内

    Args:
        list_a (list): 列表A
        list_b (list): 列表B

    Returns:
        bool: 是否包含
    """
    return list_a[0] < list_b[0] or list_a[1] > list_b[1]


def remove_kadun_from_silent(kadun_list: list, silent_list: list):
    """从卡顿列表中去掉跟静音列表重复的部分

    Args:
        kadun_list (list): 卡顿列表
        silent_list (list): 静音列表

    Returns:
        list: 去掉重复部分的卡顿列表
    """
    if len(silent_list) == 0:
        return kadun_list
    else:
        return [x for x in kadun_list if reduce((lambda a, b: a and b), [not_include(x, y) for y in silent_list])]


def remove_first_kadun_segment(kadun_list: list, threthold=0.5):
    """去头部录音的卡顿部分

    Args:
        kadun_list (list): 卡顿列表
        threthold (float, optional): 头部部分的阈值. Defaults to 0.5.

    Returns:
        list: 去掉头部后的卡顿列表
    """
    if len(kadun_list) >= 1 and kadun_list[0][1] < threthold:
        return kadun_list[1:]
    else:
        return kadun_list


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="WAVE")
    #parser.add_argument('--wavfile', type=str, default='record.wav',help='wav path')
    parser.add_argument('--time', dest='time', type=int,
                        default=30, help='录音时间,单位s')
    parser.add_argument('--file', dest='file', type=str,
                        help="检测用的文件", default="test.wav")

    args = parser.parse_args()
    file = './BJ-EarPhone-20210409-126/双通道-故障音-卡顿检测.wav'
    time = 10

    print('file name: {}'.format(file))
    # record_audio(file,time)
    sampling_rate, wavsignal = load_wav(file=file)

    # wavdata = wavsignal / (2**16-1)
    wavdata = np.array(wavsignal, dtype='int32')
    if len(wavdata.shape) < 2:
        wavdata = wavdata[:, np.newaxis]

    channel_count = wavdata.shape[1]

    total_max_value = np.max(np.abs(wavdata))
    print('总最大音量: {0}', total_max_value)

    # 当最大音量小于 min_value_threthold时， 将最大音量调整为 stard_max_value
    min_value_threthold = 800
    standard_max_value = 1000

    if total_max_value < min_value_threthold:
        total_max_value = standard_max_value

    # 静音阈值
    silent_threthold_rate = 0.1
    silent_threthold = total_max_value * silent_threthold_rate

    # 针对某一通道 进行检测
    print('{}{}{}'.format('-'*15, '是否有声', '-'*15))

    result_silent = []
    for i in range(channel_count):
        max_value = np.max(np.abs(wavdata[:, i]))
        print('{0}通道, 最大音量: {1}', i, max_value)
        res_silent_1 = has_voice(
            sampling_rate, wavdata, i, threshold=silent_threthold)
        result_silent.append(res_silent_1)
        print('{0}通道：{1}'.format(i, res_silent_1))

    print('{}{}{}'.format('-'*15, '静音检测', '-'*15))
    res_silent = list(detect_silence(
        sampling_rate, wavdata, threshold=silent_threthold))

    # 如果是静音, 就清零
    for i, v in enumerate(result_silent):
        if v == False:
            res_silent[i] = [[0, wavdata.shape[0] / sampling_rate]]

    for i, v in enumerate(res_silent):
        print('{0}通道：{1}'.format(i, v))
        print('总段数:{0}'.format(len(v)))

    print('{}{}{}'.format('-'*15, '卡顿检测', '-'*15))
    res_pause = list(detect_pause_2(sampling_rate, wavdata, rate=0.0005))

    # 去掉卡顿在静音中的部分
    res_pause_clear = []
    for i in range(len(res_pause)):
        res_pause_clear.append(
            remove_kadun_from_silent(res_pause[i], res_silent[i]))

    # 去掉头部的卡顿
    res_pause_clear = [remove_first_kadun_segment(v) for v in res_pause_clear]

    for i, val in enumerate(res_pause_clear):
        print('{0}通道：{1}'.format(i, val))
        print('总段数:{0}'.format(len(val)))

    print('{}{}{}'.format('-'*15, '噪音检测', '-'*15))
    res_noise = detect_noise2(sampling_rate, wavdata)

    for i, val in enumerate(res_noise):
        print('{0}通道：{1}'.format(i, val))
        print('总段数:{0}'.format(len(val)))
