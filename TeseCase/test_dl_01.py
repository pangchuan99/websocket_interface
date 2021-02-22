#from selenium import webdriver
#要操作下拉框：from selenium.webdriver.support.select import Select
#要操作键盘：from selenium.webdriver.common.keys import Keys
#要用系统时间：from datetime import datetime
#要操作Excel：from openpyxl import load_workbook
#from selenium.webdriver import ActionChains  #鼠标事件


import time
from common.socketio_common import socketio_common_class
'''
调用这个文件  类   进行传参，需要进行传递三个参数， 
第一个是 data: 跟get与post一样 是传入内容 
第二个是  wenjian1: 是创建路径里面的文件名称:  
第三个是    code: 是返回接口名称的 列如：code:user.login
 '''





# os.system('python ../TestDase/dg_01_dl.py/dl_login')  # 执行这个文件
# dl_login().start()

class Test_Login:

    def test_login(self):
        data = {
            "code": "user.login",
            "body": {
                "userName": "13547324646",
                "password": "278a97d3b74b6ff8da2c66d33842c210"
            },
            "token": "",
            "timestamp": time.time(),
            "sign": "aDlPwGnEeYR0uLGOMsfjWBbmeum_MjZ2",
            "nonestr": "8f88c6a0-99f4-42f9-ae99-c40e4d7efeeb",
            "extra": "null"
        }
        r1=socketio_common_class(data=data,wenjian="get_token.yaml",code="user.login")
        r1.start()











