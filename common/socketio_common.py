# -*- coding:utf-8 -*-

import json
from common.url import host#连接地址
from websocket import WebSocketApp
try:
    import thread
except ImportError:
    import _thread as thread
import time

'''
新版 对象的方法作为 WebSocketApp 回调
因为新版库不再返回 WebSocketApp 本身，所以参数不再包括 ws，我们保存 WebSocketApp 对象作为实例的一个参数 self.ws，如此，仍可在类中的任意位置使用。
'''
class socketio_common_class():

    '''
    调用这个文件  类   进行传参，需要进行传递三个参数，
    第一个是 data: 跟get与post一样 是传入内容
    第二个是  wenjian1: 是创建路径里面的文件名称:
    第三个是    code: 是返回接口名称的 列如：code:user.login
     '''
    def __init__(self,data,wenjian,code):

        '''
        :param data: 跟get与post一样 是传入内容
        :param wenjian: 是创建路径里面的文件名称:
        :param code: 是返回接口名称的 列如：code:user.login
        '''

        self.url =host#地址
        self.ws = None
        self.wenjian=wenjian
        self.data=data
        self.code=code


    def on_message(self, message):
        '''
        是用来接受消息的，server发送的所有消息都可以用on_message这个方法来收取。
        :param message: 接受返回的值
        :return:
        '''

        print("最开始的",message)


        # 因为接收的值 有许多返回接口，需要定位到具体某一个时 就需要进行 Token  进行判断
        if "{}".format(self.code) in message:
            # 进行替换
            message1 = message.replace("\\", "")

            # 进行切割付，type类型是 list
            msg_list = message1.split("'")

            # 然后进行索引读取一定范围，进行转换成 dict 字典类型
            r1 = (json.loads(msg_list[0][15:-2]))


            # 每次都要进行 登录 需要进行重写文件
            with open("../filename/{0}".format(self.wenjian), "w", encoding="utf8") as fp:
                fp.write("")
            # 然后在重写文件后面进行写入
            with open("../filename/{0}".format(self.wenjian), "a", encoding="utf-8") as fp1:
                fp1.write(str(r1))
            print("转换后的",r1)



    def on_error(self, error):
        '''
        #这个方法是用来处理错误异常的，如果一旦socket的程序出现了通信的问题，就可以被这个方法捕捉到。
        :param error:处理错误异常的
        :return:
        '''
        print("####### on_error #######")
        print(self)
        print(error)


    def on_close(self):
        '''
        主要就是关闭socket连接的。
        :return:
        '''
        print("####### on_close #######")
        print(self)
        print("####### closed #######")

    def on_open(self):
        '''
        方法是用来保持连接的，上面这样的一个例子，就是保持连接的一个过程，每隔一段时间就会来做一件事,他会在30s内一直发送hello。最后停止
        :return:
        '''
        def run():
            for i in range(1):
                time.sleep(1)
                self.ws.send('42["request","{}"]'.format(self.data))
            time.sleep(2)
            self.ws.close()
            print("thread terminating...")

        thread.start_new_thread(run, ())

    def start(self):
        self.ws = WebSocketApp(self.url,
                               on_message=self.on_message,
                               on_error=self.on_error,
                               on_close=self.on_close)
        self.ws.on_open = self.on_open
        self.ws.run_forever()
# if __name__ == '__main__':
#     dl_login().start()


