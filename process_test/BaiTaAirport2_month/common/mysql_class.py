# coding:utf-8
import pymysql

"""
class DataBase(object):
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    def open_data_base(self):
        #打开数据库的连接
        self.conn = ps.connect(host=self.host,
                               port=self.port,
                               user=self.user,
                               password=self.password,
                               database=self.database,
                             )
        self.curs = self.conn.cursor()

    def close_database(self):
        #关闭数据库
        self.curs.close()
        self.conn.close()

    def cud(self, sql):
        self.open_data_base()
        try:
            self.curs.execute(sql)
            self.conn.commit()
            print("ok")
        except Exception as A:
            print('cud出现错误'+str(A))
        self.close_database()

    def find_all(self, sql):
        self.open_data_base()
        try:
            self.curs.execute(sql)
            data = self.curs.fetchall()
            return data
        except:
            print("错误")
"""

#连接数据库
def connect_db(
            host = "175.168.1.91",
            port = "3306",
            user = "root",
            password = "123456",
            db = "secsystem",
            charset = "utf8mb4"):
    try:
        # Connect to the database
        connection = pymysql.connect(host=host,
                                     port=int(port),
                                     user=user,
                                     password=password,
                                     db=db,
                                     charset=charset,
                                     cursorclass=pymysql.cursors.DictCursor)
    except pymysql.err.OperationalError as e:
        logger.error("Mysql Error %d: %s" % (e.args[0], e.args[1]))
    return  connection

def query_data(connection,table,str1,str2,str3="",str4=""):
    """
    :param table: 表名
    :param str1: 查询条件1的字段
    :param str2: 查询条件1
    :param str3: 查询条件2的字段
    :param str4: 查询条件2
    :return: 返回查询结果
    """
    sql = 'select * from %s where %s="%s"' % (table, str1, str2)
    if str3 !="" and str4 !="":
        sql = 'select * from %s where %s="%s" and %s="%s"' % (table, str1, str2,str3, str4)
    with connection.cursor() as cursor:
        cursor.execute(sql)
        try:
            data = cursor.fetchall()
        except:
            data = ""
    # logger.info("查询数据库数据为：%s" %data)
    return data


if __name__ == '__main__':
    # shujuku = DataBase("192.168.1.105", 3306, "root", "123456", "htbusyinfo")
    # shujuku.find_all("select * from base_focus_people;")
    connection = connect_db()
    data = query_data(connection,"sec_passenger_entity","checked_time","20190814 11:23:58","flight","LB40111")
    print(data)