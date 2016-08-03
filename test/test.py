#!/usr/bin/env python
#coding=utf-8



from Alcman.Config import config
from Alcman.Actuator import actuator
from Alcman.Invoke import invoke
from Alcman.Task import task


iv = invoke()
iv.set_config(config(filename='./servers.yaml'))

iv.set_actuator(actuator(id_rsa="/root/.ssh/id_rsa", 
                        known_hosts="/root/.ssh/known_hosts", 
                        timeout=30,
                        log_to_file="/tmp/ssh.log"))

d = task(iv)
#d.run()
d.run(cmd="ls")
print d.get_result()