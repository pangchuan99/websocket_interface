import pymysql
import os
import yaml

#pip install PyMySQL==0.9.3


#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////数据库操作
'''连接数据库的 host 主机ip   
               user  账号
               password  密码
               port  端口号'''
dbinfo = {
    "host": "20.20.20.42",
    "user": "root",
    "password": "123456aA",
    "port": 7806}

class DbConnect():
    '''database数据库名称'''
    def __init__(self, db_cof, database=""):
        self.db_cof = db_cof
        # 打开数据库连接
        self.db = pymysql.connect(database=database,
                                  #'''读取出来是元组，所以进行了转换成字典'''
                                  cursorclass=pymysql.cursors.DictCursor,**db_cof)

        # 使用cursor()方法获取操作游标----相当于点击激活的意思
        self.cursor = self.db.cursor()

    def select(self, sql):
        # SQL 查询语句
        # sql = "SELECT * FROM EMPLOYEE \
        #        WHERE INCOME > %s" % (1000)

        #通过建立的游标进行查询
        self.cursor.execute(sql)
        #结果
        results = self.cursor.fetchall()
        return results

    def execute(self, sql):
        # SQL 删除、提交、修改语句
        # sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20)
        try:
           # 执行SQL语句
           self.cursor.execute(sql)
           # 提交修改
           self.db.commit()
        except:
           # 发生错误时回滚
           self.db.rollback()

    def close(self):
        # 关闭连接
        self.db.close()

def select_sql(select_sql):
    '''查询数据库'''
    db = DbConnect(dbinfo, database="gsm_backup")
    result = db.select(select_sql)  # 查询
    db.close()
    return result

def execute_sql(insert_sql):
    '''执行sql'''
    db = DbConnect(dbinfo, database="gsm_backup")
    db.execute(insert_sql)  # 查询
    db.close()
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////数据库操作








#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////文件操作----读取文件里面的内容
def get_name_wenjianmingcheng(mingcheng):
    '''

    :param mingcheng0: 他表示的是  文件夹的路径
    :param mingcheng1: 他表示的是   文件夹里面的文件
    :return:
    '''

    # 获取当前文件的上一层路径,上一层路径
    curpath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # print(curpath)

    # 然后在获取某一个文件的绝对路径
    yamlpath = os.path.join(curpath,"filename",mingcheng)
    # print(yamlpath)

    #然后进行读取这个文件，编码
    f = open(yamlpath, "r", encoding='utf-8')
    #读取这个文件里面的内容
    yamldata = f.read()
    # print(yamldata)

    #文件里面的内容是 str类型  需要转换成 dict类型  方便键值获取
    a3=yaml.load(yamldata,Loader=yaml.FullLoader)
    # a1 = (json.dumps(a3, indent=4, ensure_ascii=False))
    # print(a1)
    return a3
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////文件操作----读取文件里面的内容





#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////文件操作----读取文件
def get_file(mingcheng):
    '''
    获取文件路径
    :param mingcheng: 他表示的是  文件夹的路径
    :return:
    '''
    # 获取当前文件的上一层路径,上一层路径
    curpath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # print(curpath)

    # 然后在获取某一个文件的绝对路径
    yamlpath = os.path.join(curpath, "filename", mingcheng)
    # print(yamlpath)
    return yamlpath
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////文件操作----读取文件







#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////对文件进行删除操作
def delete_file(path1):
    '''
    读取文件，然后进行删除
    :return:
    '''
    path2=get_file(path1)
    os.remove(path2)
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////对文件进行删除操作








