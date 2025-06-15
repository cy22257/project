#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist

# モジュール仕様
motor_spec = ["implementation_id", "Motor",
              "type_name", "Motor",
              "description", "Motor Component",
              "version", "1.0.1",
              "vendor", "Nishimura Shunsei",
              "category", "Category",
              "activity_type", "STATIC",
              "max_instance", "1",
              "language", "Python",
              "lang_type", "SCRIPT",
              ""]

class Motor(OpenRTM_aist.DataFlowComponentBase):
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        # TimedBoolean型のInPort
        self._d_Signal = OpenRTM_aist.instantiateDataType(RTC.TimedBoolean)
        self._SignalIn = OpenRTM_aist.InPort("Signal", self._d_Signal)

        # TimedShort型のOutPort (通信マネージャーに送信するためのOutPort)
        self._d_Manager = OpenRTM_aist.instantiateDataType(RTC.TimedShort)
        self._ManagerOut = OpenRTM_aist.OutPort("Manager", self._d_Manager)

    def onInitialize(self):
        self.addInPort("Signal", self._SignalIn)
        self.addOutPort("Manager", self._ManagerOut)
        return RTC.RTC_OK

    def onActivated(self, ec_id):
        # 初期値として5を通信マネージャーに送信
        self._d_Manager.data = 5
        self._ManagerOut.write()
        print("Sent initial value (5) to Communication Manager.")
        return RTC.RTC_OK

    def onExecute(self, ec_id):
        if self._SignalIn.isNew():
            self._d_Signal=self._SignalIn.read()
            boolean_value = self._d_Signal.data
            if boolean_value:
                self._d_Manager.data = 4
                print("Sent to Communication Manager: 4")
            else:
                self._d_Manager.data = 5
                print("Sent to Communication Manager: 5")
            self._ManagerOut.write()
        return RTC.RTC_OK

def MotorInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=motor_spec)
    manager.registerFactory(profile,
                            Motor,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    MotorInit(manager)

    instance_name = [i for i in sys.argv if "--instance_name=" in i]
    if instance_name:
        args = instance_name[0].replace("--", "?")
    else:
        args = ""
    comp = manager.createComponent("Motor" + args)

def main():
    argv = [i for i in sys.argv if not "--instance_name=" in i]
    mgr = OpenRTM_aist.Manager.init(argv)
    mgr.setModuleInitProc(MyModuleInit)
    mgr.activateManager()
    mgr.runManager()

if __name__ == "__main__":
    main()
