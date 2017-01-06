#!/usr/bin/env python
#coding=utf-8



from Alcman.Config import config
from Alcman.Invoke import invoke
from Alcman.Task import task


iv = invoke()
iv.set_config(config(filename='./servers.yaml'))



d = task(iv)
d.run()
print d.get_result()