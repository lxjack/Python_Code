#_*_ coding: utf-8 _*_
import hashlib
import sys
import getopt
import os
from py_mysql import Mysql_Hander

def usage():
    usage_info = '''
    Usage:{0} [OPTION]
    Login in system for authentication.

    Arguments presentation，including short options and long options.         
        --user      the logining user for the system
        --passwd    the passwd for the logining user 

        Example:
        Get help for the script {0}:
            {0} -h or {0} --help
        Use the script for login linux host:
            {0} --user jack --passwd jack001    
    '''.format(os.path.basename(__file__))
    print usage_info

'''
python  添加搜索路径
方法:增加.pth文件
在site-packages添加一个路径文件，如mypkpath.pth，必须以.pth为后缀，写上你要加入的模块文件所在的目录名称即可。
'''

def md5str(str):
    '''字符串加密函数：对字符串进行md5值加密，返回加密后的字符串'''
    m = hashlib.md5()           # 创建md5对象
    m.update(str)               # 生成加密串
    return m.hexdigest()       # 打印经过md5加密的字符串

'''pre step:1.向数据库中插入数据'''
# mysql_init = Mysql_Hander(host='localhost', user='root', passwd='admin123', db='test',port=3306)
# user=('jack','jane')
# user_passwd=('jack001','jane001')
# sql="insert into users(user_name,passwd,md5_use_namer,md5_passwd) values(%s,%s,%s,%s);"
#
# for i in xrange(len(user)):
#     params=[user[i],user_passwd[i],md5str(user[i]),md5str(user_passwd[i])]
#     count=mysql_init.insert(sql,params)
#     print count


'''
2.使用脚本进行传入用户名   对传入参数进行解析
'''
try:
    opts,args = getopt.getopt(sys.argv[1:], "h", ["help","user=","passwd="])
except getopt.GetoptError as err:
    # print help information and exit:
    print str(err)
    sys.exit(1)

user_name=""
passwd=""

for opt,arg in opts:
    if opt in ("-h", "--help"):
        usage()
        sys.exit(1)
    elif opt == "--user":
        user_name = arg
    elif opt == "--passwd":
        passwd = arg
    else:
        assert False, "not suppurted option"

if user_name=="":
    print "user_name is empty."
    sys.exit(2)
if passwd=="":
    print "passwd is empty."
    sys.exit(2)

#对用户名进行加密
md5_user_name=md5str(user_name)
md5_passwd=md5str(passwd)

'''
3、使用加密后的信息进行对比  进行信息比对   进行用户登录鉴权
'''
'''1.先检索用户检查是否存在   再查看对应用户的密码是否正确'''

mysql_init = Mysql_Hander(host='localhost', user='root', passwd='admin123', db='test',port=3306)

sql="select md5_passwd from users where md5_use_namer = %s;"
params=md5_user_name
query_user_passwd=mysql_init.select_fetchall(sql,params)

if len(query_user_passwd)==0:
    print "user is not exist,please sign first."
    sys.exit(1)
else:
    query_user_md5_passwd=query_user_passwd[0][0]
    if md5_passwd == query_user_md5_passwd:
        print "user authentication success."
        sys.exit(0)
    else:
        print "user authentication failed."
        sys.exit(1)