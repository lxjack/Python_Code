#_*_ coding: utf-8 _*_
import paramiko
from time import sleep

class Linux_Host():

    def __init__(self,ip,port=22,username='root',password=""):
        #初始化一个对谈窗口
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(ip, port, username, password)
        self.channel = self.ssh.invoke_shell()        #登录到远程主机，开一个终端，进行对谈
        #设置终端命令提示符
        self.end = "%s:>" % username
        self.ps1_len = len(self.end)
        self.cmd("export PS1='\u:>'")

    def close_connection(self):
        self.channel.close()
        self.ssh.close()

    def send(self,cmdstr):
        #下发一个命令
        self.channel.send(cmdstr+"\n")

    def receive(self):
        #接受命令的回显
        res=self.channel.recv(1024)
        return res

    def cmd(self,cmdstr,timeout=30):
        #下发命令，接受回显
        self.send(cmdstr)

        self.echostr=""
        for i in xrange(timeout):
            sleep(1)
            self.echostr =self.echostr+self.receive()

            if self.echostr[-self.ps1_len:] == self.end:
                print "receive info end"
                break
        #删除回显中cmdstr和终端命令提示符self.end
        self.echostr=self.echostr.replace(cmdstr+"\r\n","",1)
        self.echostr = self.echostr.replace(self.end,"", 1)
        return self.echostr


if __name__=="__main__":
    host=Linux_Host('192.168.225.129', port=22, username='root', password='lx20117335')
    rece_info=host.cmd("cat -n /home/jack/workspace/temp.txt")
    print  rece_info
    host.close_connection()
