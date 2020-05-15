# coding:utf-8
import paramiko
import time


def sshclient_execmd(hostname, port, username, password, execmd):
    """
    远程聊
    :param hostname:
    :param port:
    :param username:
    :param password:
    :param execmd:
    :return:
    """
    paramiko.util.log_to_file("paramiko.log")

    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname=hostname, port=port, username=username, password=password)
    while True:
        stdin, stdout, stderr = s.exec_command(execmd)
        stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction.
        print(str(stdout.read(), encoding="utf-8"))
        print(type(str(stdout.read(), encoding="utf-8")))
        time.sleep(1)
    s.close()


def main():

    hostname = '192.168.1.107'
    port = 22
    username = 'root'
    password = '11111111'
    execmd = "w"

    #     execmd = "top -bcn 1 -p 1449 | grep mysql"

    sshclient_execmd(hostname, port, username, password, execmd)


if __name__ == "__main__":
    main()