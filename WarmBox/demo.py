#coding:utf-8

from device import device

class Warm_Box_Case:

    max_tem=None
    min_tem=None
    avg_tem=None
    def __init__(self):
        self.device=device()

    def check(self):
        self.device.reset()
        print self.device.a_value_up
        print self.device.b_value_up
        self.device.start_calibrate_points({'2': [(44, 46), (48, 50)]})
        print self.device.a_value_down
        print self.device.b_value_down
        print 'Check Side #######################'
        self.device.start_calibrate_points({'3':[(15,20),(16,21),(55,47),(57,49)]})
        print self.device.a_value_side
        print self.device.b_value_side
        self.device.get_room_tem()
    def start_case(self):
        self.device.start_get_thermal_data({'1':[(35,36),(40,41)],'2':[(44,46),(48,50),(15,20),(16,21),(55,47),(57,49)],'3':[(15,20),(16,21),(55,47),(57,49)]})

    def stop_case(self):
        res=self.device.stop_get_thermal_data()
        print res

wbc=Warm_Box_Case()
wbc.check()
wbc.start_case()
wbc.stop_case()
