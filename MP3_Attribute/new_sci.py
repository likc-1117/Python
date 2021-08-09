#coding = utf-8
import wave
from think.thinkdsp import *
import matplotlib.pyplot as plt
import numpy as np
from scipy.io.wavfile import read

# 加载音频文件
def load_wav(file):
    sampling_rate, wavsignal = read(file)
    # print('sampling_rate:{0}'.format(sampling_rate))
    # print('wavsignal:{0}'.format(wavsignal))
    return sampling_rate, wavsignal



wave_file = read_wave('output-2021-08-05-11-31-50.wav')
wf = wave_file.diff()
# spe = wave_file.make_spectrum()
wf.plot()
plt.show()