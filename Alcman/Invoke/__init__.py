#!/usr/bin/env python
#coding=utf-8

'''
mail:wqc2008@gmail.com
createtime:2016-7-20 18:00:00
usege:
    组装ymal文件
    ###与ssh执行器的信息 对于程序员来讲不是特别友好,应该屏蔽SSH的设置

'''

__all__ = ['invoke']

class invoke(object):

    def __init__(self):

        self.hosts  = []
        self.ssh    = None

    def set_config(self,config=None,group=None):

        if group == None:
            self.hosts = config.get_hosts()['hosts']
        else:
            self.hosts = config.get_hosts()[group]
    #
    # def set_actuator(self,actuator=None):
    #     self.actuator = actuator