#_*_ coding: utf-8 _*_
import MySQLdb

class Mysql_Hander():
    def __init__(self,host,user,passwd,db,port=3306,charset='utf8'):
        self.host=host
        self.port=port
        self.db=db
        self.user=user
        self.passwd=passwd
        self.charset=charset

    def connect(self):
        self.conn=MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db,port=self.port,charset=self.charset)
        self.cursor=self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def select_fetchone(self,sql,params=()):
        result=None
        try:
            self.connect()
            self.cursor.execute(sql, params)
            result = self.cursor.fetchone()
            self.close()
        except Exception, e:
            print e.message
        return result

    def select_fetchall(self,sql,params=()):
        result=()
        try:
            self.connect()
            self.cursor.execute(sql,params)
            result=self.cursor.fetchall()
            self.close()
        except Exception,e:
            print e.message
        return result

    def insert(self,sql,params=()):
        return self.__edit(sql,params)

    def update(self, sql, params=()):
        return self.__edit(sql, params)

    def delete(self, sql, params=()):
        return self.__edit(sql, params)

    def __edit(self,sql,params):
        count=0
        try:
            self.connect()
            count=self.cursor.execute(sql,params)  #将影响的行数赋值给count
            self.conn.commit()
            self.close()
        except Exception,e:
            print e.message
        return count

if __name__=="__main__":
    ##eg:对数据进行查询并返回结果
    mysql_init = Mysql_Hander(host='localhost', user='root', passwd='admin123', db='test1',port=3306)

    sql="select * from student where id between %s and %s;"
    params=(2,3)
    result=mysql_init.select_fetchall(sql,params)
    print result