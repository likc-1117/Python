import subprocess
import re

pip_list = 'pip list -o'

pip_list_exc_result = subprocess.Popen(pip_list, shell=True, stdout=subprocess.PIPE)
get_pip_list_result = pip_list_exc_result.communicate(0, 60000)[0].decode('utf-8')
print(get_pip_list_result)
result_list = get_pip_list_result.splitlines()
# result_list = ['Package                Version     Latest     Type ', '---------------------- ----------- ---------- -----', 'absl-py                0.7.1       0.9.0      sdist', 'aiohttp                3.5.4       3.6.2      wheel', 'altgraph               0.16.1      0.17       wheel', 'Appium-Python-Client   0.47        0.49       sdist', 'astor                  0.7.1       0.8.1      wheel', 'attrs                  19.1.0      19.3.0     wheel', 'bitarray               0.8.3       1.2.1      sdist', 'certifi                2019.3.9    2019.11.28 wheel', 'colorama               0.4.1       0.4.3      wheel', 'decorator              4.3.2       4.4.1      wheel', 'Django                 2.1.7       3.0.3      wheel', 'fire                   0.1.3       0.2.1      sdist', 'Flask                  1.0.2       1.1.1      wheel', 'gast                   0.2.2       0.3.3      wheel', 'get                    2018.11.19  2019.4.13  sdist', 'grpcio                 1.19.0      1.27.1     wheel', 'h5py                   2.9.0       2.10.0     wheel', 'humanize               0.5.1       1.0.0      wheel', 'Jinja2                 2.10        2.11.1     wheel', 'Keras-Applications     1.0.7       1.0.8      wheel', 'Keras-Preprocessing    1.0.9       1.1.0      wheel', 'kiwisolver             1.0.1       1.1.0      wheel', 'lxml                   4.3.2       4.5.0      wheel', 'Markdown               3.0.1       3.2        wheel', 'matplotlib             3.0.3       3.1.3      wheel', 'mock                   2.0.0       4.0.1      wheel', 'multidict              4.5.2       4.7.4      wheel', 'mysql-connector-python 8.0.15      8.0.19     wheel', 'mysqlclient            1.4.2.post1 1.4.6      wheel', 'numpy                  1.16.2      1.18.1     wheel', 'openpyxl               3.0.0       3.0.3      sdist', 'pandas                 0.24.2      1.0.1      wheel', 'pbr                    5.1.3       5.4.4      wheel', 'Pillow                 5.4.1       7.0.0      wheel', 'post                   2018.11.20  2019.4.13  sdist', 'protobuf               3.7.0       3.11.3     wheel', 'psutil                 5.6.1       5.6.7      wheel', 'public                 2018.11.20  2019.4.13  sdist', 'py                     1.8.0       1.8.1      wheel', 'PyInstaller            3.5         3.6        sdist', 'pyparsing              2.3.1       2.4.6      wheel', 'python-dateutil        2.8.0       2.8.1      wheel', 'pytz                   2018.9      2019.3     wheel', 'PyYAML                 5.1.2       5.3        wheel', 'query-string           2018.11.20  2019.4.13  sdist', 'request                2018.11.20  2019.4.13  sdist', 'requests               2.21.0      2.22.0     wheel', 'response               0.3.0       0.4.0      wheel', 'scipy                  1.2.1       1.4.1      wheel', 'setuptools             41.0.1      45.2.0     wheel', 'six                    1.12.0      1.14.0     wheel', 'SQLAlchemy             1.3.1       1.3.13     sdist', 'tensorboard            1.13.1      2.1.0      wheel', 'tensorflow             1.13.1      2.1.0      wheel', 'tensorflow-estimator   1.13.0      2.1.0      wheel', 'uiautomator2           0.1.11      2.5.4      sdist', 'urllib3                1.24.1      1.25.8     wheel', 'Werkzeug               0.14.1      1.0.0      wheel', 'wheel                  0.33.1      0.34.2     wheel', 'whichcraft             0.5.2       0.6.1      wheel', 'yarl                   1.3.0       1.4.2      wheel']
print(result_list)
result_list = result_list[2:]
# need_update_model_name = {'package': None, 'version': None, 'Latest': None}
for result_list_item in result_list:
    re_result = re.findall(r'[^\s]+', result_list_item, re.I)
    print(re_result)
    # need_update_model_name['package'] = re_result[0]
    # need_update_model_name['version'] = re_result[1]
    # need_update_model_name['Latest'] = re_result[2]
    # print(need_update_model_name)
    if re_result[1] < re_result[2]:
        print('-------------------------- Start update packages --------------------------')
        update_cmd = 'pip install -U {pu}'.format(pu=re_result[0])
        subprocess.call(update_cmd)
        print('**********%s update end *********' % re_result[0])
        print('-------------------------- Update packges end -----------------------------')
