import visa
from visa import constants
import time
import datetime
import collections
import math
import re


Resource = collections.namedtuple('Resource', ['channel', 'type'])
Data = collections.namedtuple('Data', ['channel', 'time', 'value'])


class agilent34970:

    def __init__(self):
        self.rm = visa.ResourceManager()

    def open(self, resource_name=None):
        ''' open resouce and init 34970A ''' 
        devices = self.rm.list_resources()
        devices = [d for d in devices if d.startswith('GPIB')]
        if len(devices) == 0:
            raise Exception('no device found')
        if resource_name is None:
            resource_name = devices[0]
        self.inst = self.rm.open_resource(resource_name, access_mode=4, open_timeout=2000)
        self.inst.set_visa_attribute(constants.VI_ATTR_TMO_VALUE, 4000)
        self.inst.get_visa_attribute(constants.VI_ATTR_INTF_TYPE)
        
        # clear error
        for i in range(4):
            if 'No error' not in self.inst.query("SYST:ERR?"):
                if i == 3:
                    raise Exception('Error in device')
                else:
                    break
            time.sleep(1) 
        # check device
        if "HEWLETT-PACKARD,34970" not in self.inst.query("*IDN?"):
            raise Exception('Device not compatited')

        self.inst.query("INST:DMM:INST?")
        # expect "1")
        self.inst.query("INST:DMM?")
        # expect "1")

        # check board
        if "HEWLETT-PACKARD,34901" not in self.inst.query("SYST:CTYP? 100"):
            raise Exception('Board not compatited')

        self.inst.query("STAT:OPER:COND?")
        # expect "+0")
        self.inst.query("DATA:POINts?")
        # expect "+0")
        self.inst.query("ROUTe:SCAN?")
        # expect "#218(@101,102,103,104)")
        self.inst.query("DISP?")
        # expect "1")
        self.inst.write("*RST")
        self.inst.write("ROUT:SCAN (@)")
        self.inst.write("DISP ON")
        self.inst.write("OUTP:ALAR:MODE LATC")
        self.inst.write("OUTP:ALAR:SLOP NEG")
        if 'No error' not in self.inst.query("SYST:ERR?"):
            raise Exception('init device error')

    def stopScan(self):
        self.inst.write('ABOR')
        dataNum = self.inst.query_ascii_values("DATA:POIN?")[0]
        self.inst.query('R? %d' % dataNum)

    def close(self):
        self.inst.close()

    def __del__(self):
        self.stopScan()
        self.close()

    def setupDevice(self, *resources):
        assert type(resources[0]) == Resource
           # raise TypeError('the resource must be Resource type')
        for res in resources:
            self.inst.write("CONF:TEMP TC,{typ},(@{channel})".format(typ=res.type, channel=res.channel))
            self.inst.write("TEMP:NPLC 1 ,(@{channel})".format(channel=res.channel))
            self.inst.write("UNIT:TEMP C,(@{channel})".format(channel=res.channel))
            self.inst.write("TEMP:TRAN:TC:RJUN 0,(@{channel})".format(channel=res.channel))
            self.inst.write("TEMP:TRAN:TC:RJUN:TYPE INT,(@{channel})".format(channel=res.channel))
            self.inst.write("TEMP:TRAN:TC:CHEC OFF,(@{channel})".format(channel=res.channel))
            self.inst.write("ROUT:CHAN:DEL 0.001,(@{channel})".format(channel=res.channel))
            self.inst.write("ROUT:CHAN:DEL:AUTO ON,(@{channel})".format(channel=res.channel))
            self.inst.write("CALC:SCAL:GAIN 1,(@{channel})".format(channel=res.channel))
            self.inst.write("CALC:SCAL:OFFS 0,(@{channel})".format(channel=res.channel))
            self.inst.write("CALC:SCAL:UNIT 'C',(@{channel})".format(channel=res.channel))
            self.inst.write("CALC:SCAL:STAT OFF,(@{channel})".format(channel=res.channel))
            self.inst.write("OUTP:ALAR1:SOUR (@{channel})".format(channel=res.channel))
            self.inst.write("CALC:LIM:UPP MAX,(@{channel})".format(channel=res.channel))
            self.inst.write("CALC:LIM:LOW:STAT OFF,(@{channel})".format(channel=res.channel))
            self.inst.write("CALC:LIM:UPP:STAT OFF,(@{channel})".format(channel=res.channel))
            self.inst.write("CALC:LIM:LOW 0,(@{channel})".format(channel=res.channel))
            self.inst.write("CALC:LIM:UPP 1,(@{channel})".format(channel=res.channel))
            if 'No error' not in self.inst.query("SYST:ERR?"):
                raise Exception('params error, setup failed')
        self.resouces = resources
    
    def startScan(self, interval=10):
        if self.resouces is None:
            raise Exception('please setup device first')
        channels = ','.join([str(c.channel) for c in self.resouces])
        self.inst.write("ROUT:SCAN (@%s)" % channels)
        self.inst.write("TRIG:TIM {tm}".format(tm=interval))
        self.inst.write("TRIG:SOUR Timer")
        self.inst.write("TRIG:COUN INF")
        if 'No error' not in self.inst.query("SYST:ERR?"):
            raise Exception('start scan error')
        # expect "+0,"No error"")
    
        t = datetime.datetime.now()
        self.inst.write("SYST:DATE %d,%d,%d" % (t.year, t.month, t.day))
        t = datetime.datetime.now()
        self.inst.write("SYST:TIME %d,%d,%d" % (t.hour, t.minute, t.second))
        if channels not in self.inst.query("ROUT:SCAN?"):
            raise Exception('set channels error')
        # expect "#218(@101,102,103,104)")
        self.inst.write("FORM:READ:ALAR OFF")
        self.inst.write("FORM:READ:CHAN ON")
        self.inst.write("FORM:READ:TIME ON")
        self.inst.write("FORM:READ:UNIT OFF")
        self.inst.write("FORM:READ:TIME:TYPE ABS")
        #    self.inst.write("FORM:READ:TIME:TYPE REL")
        self.inst.write("TRIG:TIM {tm}".format(tm=interval))
        self.inst.write("TRIG:SOUR Timer")
        self.inst.write("TRIG:COUN INF")
        self.inst.write("INIT")
        if self.inst.query_ascii_values("STAT:OPER:COND?")[0] != 16:
            raise Exception('Scan not started')
        
        if 'No error' not in self.inst.query("SYST:ERR?"):
            raise Exception('start scan error')
        # expect "+16")


    def fetchData(self):
        self.inst.query("STAT:OPER:COND?")
        # expect "+16")
        dataNum = int(self.inst.query_ascii_values("DATA:POIN?")[0])
        if dataNum == 0:
            return
        rawdata = self.inst.query('R? %d' % dataNum)
        for value in dataAnalyse(rawdata, dataNum):
            yield value
    
    def fetchDataInfinity(self, intervaltime=2):
        while True:
            for value in self.fetchData():
                yield value
            time.sleep(intervaltime)

			

def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] 
             for i in range(wanted_parts) ]


def dataAnalyse(data, parts):
    ''' '''
    regex = '#[0-9]+'
    matches = re.findall(regex, data)
    match = matches[0]
    startpoint = data.find(match) + len(match) + 1
    datasplit = split_list(data[startpoint: -1].split(','), parts)
    for dt in datasplit:
        channel = int(dt[-1])
        value = float(dt[0])
        t = datetime.datetime(int(dt[1]), int(dt[2]), int(dt[3]), int(dt[4]), int(dt[5]), int(math.floor(float(dt[6]))))
        yield Data(channel, t, value)


def printData():
    while True:
        value = yield
        if value is None:
            break
        print(value)
    return


if __name__ == '__main__':
    agilent = agilent34970()
    agilent.open()
    time.sleep(2)
    # res = Resource(101, 'T')
    agilent.setupDevice(Resource(101,'T'))
    #agilent.setupDevice(Resource(101,'T'))
    # agilent.setupDevice(res)
    time.sleep(2)
    agilent.startScan(interval=6)

    printdata = printData()
    next(printdata)

    for d in agilent.fetchDataInfinity():
        printdata.send(d)