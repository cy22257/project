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
sevseg_spec = ["implementation_id", "SevSeg",
               "type_name", "SevSeg",
               "description", "7-Segment Display Component",
               "version", "1.0.1",
               "vendor", "Nishimura Shunsei",
               "category", "Category",
               "activity_type", "STATIC",
               "max_instance", "1",
               "language", "Python",
               "lang_type", "SCRIPT",
               ""]

class SevSeg(OpenRTM_aist.DataFlowComponentBase):
    def __init__(self, manager):
        OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

        # TimedBooleanSeq型のInPort
        self._d_Signal = OpenRTM_aist.instantiateDataType(RTC.TimedBooleanSeq)
        self._SignalIn = OpenRTM_aist.InPort("Signal", self._d_Signal)

        # TimedShort型のOutPort (通信マネージャーに送信するためのOutPort)
        self._d_Manager = OpenRTM_aist.instantiateDataType(RTC.TimedShort)
        self._ManagerOut = OpenRTM_aist.OutPort("Manager", self._d_Manager)

    def onInitialize(self):
        self.addInPort("Signal", self._SignalIn)
        self.addOutPort("Manager", self._ManagerOut)
        return RTC.RTC_OK

    def onActivated(self, ec_id):
        # 初期値として0を通信マネージャーに送信
        self._d_Manager.data = 0
        self._ManagerOut.write()
        print("Sent initial value (0) to Communication Manager.")
        return RTC.RTC_OK

    def onExecute(self, ec_id):
        # InPortに新しいデータがあるか確認
        if self._SignalIn.isNew():
            # データを正しく読み込むため、戻り値を変数に直接保存
            data_obj = self._SignalIn.read()  # 戻り値を使って取得
            signal_data = data_obj.data  # data部分にアクセス

            # デバッグ用: 受信したデータを表示
            print(f"Received Signal Array: {signal_data}")

            # Boolean配列に基づいて通信マネージャーに送信するデータを設定
            if signal_data == [False, False]:
                self._d_Manager.data = 0
            elif signal_data == [False, True]:
                self._d_Manager.data = 1
            elif signal_data == [True, False]:
                self._d_Manager.data = 2
            elif signal_data == [True, True]:
                self._d_Manager.data = 3
            else:
                print(f"Unexpected Signal Array: {signal_data}")
                return RTC.RTC_OK

            # OutPortにデータを送信
            self._ManagerOut.write()
            print(f"Sent to Communication Manager: {self._d_Manager.data}")
        return RTC.RTC_OK


def SevSegInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=sevseg_spec)
    manager.registerFactory(profile,
                            SevSeg,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    SevSegInit(manager)

    instance_name = [i for i in sys.argv if "--instance_name=" in i]
    if instance_name:
        args = instance_name[0].replace("--", "?")
    else:
        args = ""
    comp = manager.createComponent("SevSeg" + args)

def main():
    argv = [i for i in sys.argv if not "--instance_name=" in i]
    mgr = OpenRTM_aist.Manager.init(argv)
    mgr.setModuleInitProc(MyModuleInit)
    mgr.activateManager()
    mgr.runManager()

if __name__ == "__main__":
    main()
