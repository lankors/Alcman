#!/usr/bin/env python
#coding=utf-8

import yaml
import os
import json
import base64
import socket
import paramiko
import traceback

'''
mail:wqc2008@gmail.com
createtime:2016-7-20 18:00:00
usege:
    ssh执行器
    
'''

__all__ = ['actuator']


def trace_back():
    try:
        return traceback.format_exc()
    except:
        return ''
    


class  actuator(object):

    def __init__(self,id_rsa="/root/.ssh/id_rsa", known_hosts="/root/.ssh/known_hosts", timeout=30,log_to_file="/tmp/ssh.log" ):

        self.id_rsa      = id_rsa
        self.known_hosts = known_hosts
        self.timeout     = timeout
        self.log_to_file = log_to_file

        paramiko.util.log_to_file(log_to_file)
        #建立连接
        self.ssh=paramiko.SSHClient()

    def run(self, host):
       
            
        try:
        
            #如果没有密码就走public key
            if host.get('passwd',True) == True:
                
                privatekeyfile = os.path.expanduser(self.id_rsa)
                paramiko.RSAKey.from_private_key_file(privatekeyfile)



            if host.get('port',True) == True:
                host['port'] = 22


            #缺失host_knows时的处理方法
            self.ssh.load_system_host_keys(self.known_hosts)
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


            #连接远程客户机器,这里需要用户自己保证IP可用，不用内外网的偿试
            try:
                self.ssh.connect(
                            hostname =host['ip'],
                            port     =int(host['port']),
                            username =host['username'],
                            password =host['passwd'],
                            compress =True,
                            timeout  = 3

                            )
            except:
                self.ssh.close()

                return {'status':-1,'output':trace_back()}  
                
            #获取远程命令执行结果
            stdin, stdout, stderr = self.ssh.exec_command(host['cmd'],bufsize=65535, timeout=self.timeout)
            temp = stdout.readlines()
            
            status = {'status':0,'output':json.dumps(temp)}
            
            #输出执行结果
            self.ssh.close()

            return status
     
        except  :

            self.ssh.close()

            return {'status':-1,'output':trace_back()}  
