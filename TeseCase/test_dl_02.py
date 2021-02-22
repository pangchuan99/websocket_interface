#from selenium import webdriver
#要操作下拉框：from selenium.webdriver.support.select import Select
#要操作键盘：from selenium.webdriver.common.keys import Keys
#要用系统时间：from datetime import datetime
#要操作Excel：from openpyxl import load_workbook
#from selenium.webdriver import ActionChains  #鼠标事件

import pytest
import time
from common.socketio_common import socketio_common_class


'''
调用这个文件  类   进行传参，需要进行传递三个参数， 
第一个是 data: 跟get与post一样 是传入内容 
第二个是  wenjian0: 是创建路径文件名称:  
第三个是  wenjian1: 是创建路径里面的文件名称:  
第四个是    code: 是返回接口名称的 列如：code:user.login
 '''



from common.all_common import get_name_wenjianmingcheng,execute_sql,select_sql,delete_file


class Test_audioCfg:



    def test_audioCfg_insert(self):
        '''
         此接口是  进行音频配置添加
        :param delete_audiocfg: 后置条件   进行删除此接口添加的数据
        :return:
        '''
        data ={
                    "code":"audioCfg.insert",
                    "body":{
                        "audioCfgList":[
                            {
                                "uuid":"",
                                "audioId":"庞川添加的测试接口123",
                                "name":"10",
                                "version":"10",
                                "src":"",
                                "extra":""
                            }
                        ]
                    },
                    "timestamp":time.time(),
                    "nonestr":get_name_wenjianmingcheng("get_token.yaml")["nonestr"],
                    "token":get_name_wenjianmingcheng("get_token.yaml")["body"]["token"]
                }
        r1=socketio_common_class(data=data,wenjian="audioCfg_insert.yaml",code="audioCfg.insert")
        r1.start()

        #进行断言操作
        assert "audioCfg.insert"==get_name_wenjianmingcheng("audioCfg_insert.yaml")["code"]

        #接口添加了这条数据，通过数据库进行删除
        execute_sql('DELETE FROM audio_cfg  WHERE audio_id="庞川添加的测试接口123"')

        #执行完后，我们需要把这个文件进行删除
        delete_file("audioCfg_insert.yaml")


    def test_audioCfg_update(self):
        execute_sql('INSERT INTO audio_cfg(uuid,audio_id,name)  VALUES("258","庞川添加的测试接口123456",12)')

        data = {
            "code": "audioCfg.update",
            "body": {
                "audioCfgList": [
                    {
                        "uuid": 258,
                        "audioId": "audioId22222",
                        "name": "name",
                        "version": "version",
                        "src": "src",
                        "extra": ""
                    }
                ]
            },
            "timestamp": time.time(),
            "nonestr": get_name_wenjianmingcheng("get_token.yaml")["nonestr"],
            "token": get_name_wenjianmingcheng("get_token.yaml")["body"]["token"]

               }
        r1 = socketio_common_class(data=data, wenjian="audioCfg_update.yaml", code="audioCfg.update")
        r1.start()

        # 进行断言操作
        assert "audioCfg.update" == get_name_wenjianmingcheng("audioCfg_update.yaml")["code"]
        execute_sql('DELETE FROM audio_cfg  WHERE uuid="258"')
        delete_file("audioCfg_update.yaml")


    def test_audioCfg_delete(self):
        execute_sql('INSERT INTO audio_cfg(uuid,audio_id,name)  VALUES("2589","庞川添加的测试接口123456",12)')

        data={
                "code":"audioCfg.delete",
                "body":["2589"],
                "timestamp":time.time(),
                "nonestr":get_name_wenjianmingcheng("get_token.yaml")["nonestr"],
                "token":get_name_wenjianmingcheng("get_token.yaml")["body"]["token"]
                }

        r1 = socketio_common_class(data=data, wenjian="audioCfg_delete.yaml", code="audioCfg.delete")
        r1.start()


        # 进行断言操作
        assert "audioCfg.delete" == get_name_wenjianmingcheng("audioCfg_delete.yaml")["code"]
        delete_file("audioCfg_delete.yaml")



















