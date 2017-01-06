#!/usr/bin/env python
# coding=utf-8


import os
import json
import yaml
import base64
import socket
import paramiko
import traceback
from   threading import Thread

'''
mail:wqc2008@gmail.com
createtime:2016-7-20 18:00:00
usege:
    ssh执行器
    将ssh连接 线程化,方便使用时实现并行

'''

__all__ = ['actuator']


def trace_back():
    try:
        return traceback.format_exc()
    except:
        return ''


class actuator(Thread):
    def __init__(self, host={}, id_rsa="~/.ssh/id_rsa", known_hosts="~/.ssh/known_hosts", timeout=1,
                 log_to_file="/tmp/ssh.log"):

        Thread.__init__(self)
        # expanduser自动转义~
        self.id_rsa = os.path.expanduser(id_rsa)
        self.known_hosts = os.path.expanduser(known_hosts)

        self.timeout = timeout
        self.log_to_file = log_to_file
        paramiko.util.log_to_file(self.log_to_file)
        # 建立连接
        self.ssh = paramiko.SSHClient()
        self.host = host
        self.result = None

    def get_result(self):

        return self.result

    def run(self):

        try:

            host = self.host

            # 如果没有密码就走public key
            if host.get('passwd', True) == True:
                paramiko.RSAKey.from_private_key_file(self.id_rsa)

            if host.get('port', True) == True:
                host['port'] = 22

            # 缺失host_knows时的处理方法
            self.ssh.load_system_host_keys(self.known_hosts)
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            # 连接远程客户机器
            try:

                self.ssh.connect(
                    hostname=host['ip'],
                    port=int(host['port']),
                    username=host['username'],
                    password=host['passwd'],
                    compress=True,
                    timeout=1,
                    allow_agent=False,
                    look_for_keys=False
                )
            except:
                self.ssh.close()

                self.result = {'status': -1, 'output': trace_back()}

                return False

                # 获取远程命令执行结果
            stdin, stdout, stderr = self.ssh.exec_command(host['cmd'], bufsize=65535, timeout=self.timeout)
            temp = stdout.readlines()

            status = {'status': 0, 'output': json.dumps(temp)}

            # 输出执行结果
            self.ssh.close()

            self.result = status

        except:

            self.ssh.close()

            self.result = {'status': -1, 'output': trace_back()}

            return False


