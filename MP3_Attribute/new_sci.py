#coding = utf-8
import wave
import matplotlib.pyplot as plt
import numpy as np
from scipy.io.wavfile import read

# 加载音频文件
def load_wav(file):
    sampling_rate, wavsignal = wav.read(file)
    # print('sampling_rate:{0}'.format(sampling_rate))
    # print('wavsignal:{0}'.format(wavsignal))
    return sampling_rate, wavsignal



wav_file = wave.open('output-2021-08-05-11-31-50.wav')
frame_num = wav_file.getparams().nframes
sampling_frequency = wav_file.getparams().framerate
sampling_time = 1 / sampling_frequency
wav_time = frame_num / sampling_frequency
sf, audio_sequence = read('output-2021-08-05-11-31-50.wav')
print('frame_num:{}'.format(frame_num))
print('sampling frequency:{}'.format(sampling_frequency))
print('sf:{}'.format(sf))
print('total time:{}'.format(frame_num / sampling_frequency ))
print('audio:{}'.format(audio_sequence[:,0]))
x = np.arange(0,wav_time,sampling_time)
plt.plot(x, audio_sequence[:,0],'blue')
plt.show()