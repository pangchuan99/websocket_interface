import pytest
import requests
import json


# sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "D:\PYcharm\python16")))



@pytest.fixture(scope="session")
def login_fixture1():
    '''登录 前置操作'''
    s=requests.session()
    # Login_interface(s).Login_fixture0()
    yield s
    print("后置操作")
    # s.close()





