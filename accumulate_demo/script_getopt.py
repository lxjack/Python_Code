#_*_ coding: utf-8 _*_
import getopt
import sys
import os
#介绍python脚本接受参数的处理

def usage():
    usage_info='''
    Usage:{0} [OPTION]
    Login in linux host,and operate some steps.
    
    Arguments presentation，including short options and long options. 
        -h,--help   show the help info
        --port      the port for the linux host
        --ip        the ip address for the linux host
        --user      the logining user for the linux host
        --passwd    the passwd for the logining user 
        
        Example:
        Get help for the script {0}:
            {0} -h or {0} --help
        Use the script for login linux host:
            {0} -p 22 --ip 8.46.11.224 --user root --passwd jack001    
    '''.format(os.path.basename(__file__))
    print usage_info

#选项类型：1.短选项     2.长选项
#1.短选项   1.1.开关选项  h        1.2.参数选项  d:
#2.长选项   2.1.开关选项  help     2.2.参数选项  name=
try:
    opts,args = getopt.getopt(sys.argv[1:], "hp:", ["help", "port=","ip=","user=","passwd="])
except getopt.GetoptError as err:
    # print help information and exit:
    print str(err)
    usage()
    sys.exit(1)

print opts

port=""
ip_address=""
user_name=""
passwd=""

for opt,arg in opts:
    if opt in ("-h", "--help"):
        usage()
        sys.exit(1)
    elif opt in ("-p", "--port"):
        port = arg
    elif opt == "--ip":
        ip_address = arg
    elif opt == "--user":
        user_name = arg
    elif opt == "--passwd":
        passwd = arg
    else:
        usage()
        assert False, "not suppurted option"

print port
print ip_address
print user_name
print passwd