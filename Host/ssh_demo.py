# coding=utf8
import paramiko

class SSHConnection(object):
    def __init__(self, host, port, username, password):
        self._host = host
        self._port = port
        self._username = username
        self._password = password
        self._transport = None
        self._sftp = None
        self._client = None
        self._connect()  # 建立连接

    def _connect(self):
        transport = paramiko.Transport((self._host, self._port))
        transport.connect(username=self._username, password=self._password)
        self._transport = transport

    # 下载
    def download(self, remotepath, localpath):
        if self._sftp is None:
            self._sftp = paramiko.SFTPClient.from_transport(self._transport)
        self._sftp.get(remotepath, localpath)

    # 上传
    def put(self, localpath, remotepath):
        if self._sftp is None:
            self._sftp = paramiko.SFTPClient.from_transport(self._transport)
        self._sftp.put(localpath, remotepath)

    # 执行命令
    def exec_command(self, command):
        if self._client is None:
            self._client = paramiko.SSHClient()
            self._client._transport = self._transport
        stdin, stdout, stderr = self._client.exec_command(command)
        data = stdout.read()
        if len(data) > 0:
            print data.strip()  # 打印正确结果
            return data
        err = stderr.read()
        if len(err) > 0:
            print err.strip()  # 输出错误结果
            return err

    def close(self):
        if self._transport:
            self._transport.close()
        if self._client:
            self._client.close()

if __name__ == "__main__":
    conn = SSHConnection('*.*.*.*', 22, 'root', '***')

    #文件上传  从哪里到哪里
    conn.put(r"D:\02E_DISK\02_Python\Python_Code\Host\Linux_Host.py", "/home/jack/workspace/Linux_Host.py")
    #文件下载
    conn.download("/home/jack/workspace/grub.conf", r"D:\02E_DISK\02_Python\Python_Code\Host\grub.cfg")
