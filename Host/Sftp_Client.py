# coding=utf8
import paramiko

class Sftp_Client(object):
    def __init__(self, host, port, username, password):
        self._host = host
        self._port = port
        self._username = username
        self._password = password
        self._transport = None
        self._sftp = None
        self._connect()  #创建链接

    #创建链接
    def _connect(self):
        transport = paramiko.Transport((self._host, self._port))
        transport.connect(username=self._username, password=self._password)
        self._transport = transport

    # 下载文件
    def download(self, remotepath, localpath):
        if self._sftp is None:
            self._sftp = paramiko.SFTPClient.from_transport(self._transport)
        self._sftp.get(remotepath, localpath)

    # 上传文件
    def put(self, localpath, remotepath):
        if self._sftp is None:
            self._sftp = paramiko.SFTPClient.from_transport(self._transport)
        self._sftp.put(localpath, remotepath)

    def close(self):
        if self._transport:
            self._transport.close()


if __name__ == "__main__":
    conn = Sftp_Client('****', 22, 'root', '**')

    # 文件下载  源地址到目的地址
    conn.download("/home/jack/workspace/grub.conf", r"D:\02E_DISK\02_Python\Python_Code\Host\grub.cfg")

    #文件上传  源地址到目的地址
    conn.put(r"D:\02E_DISK\02_Python\Python_Code\Host\Linux_Host.py", "/home/jack/workspace/Linux_Host.py")

    conn.close()