#!/usr/bin/env python
#coding=utf-8

#from multiprocessing.dummy import Pool as ThreadPool 

from multiprocessing import Pool as ThreadPool 

'''
mail:wqc2008@gmail.com
createtime:2016-7-20 18:00:00
usege:
    根据组装参数来执行任务列表
    
'''

__all__ = ['task']

class task(object):

    def __init__(self,invoke):

        self.invoke  = invoke
        self.result =  None


    def exec_cmd(self, host):
        
        return self.invoke.actuator.run(host)
        

    def run(self,cmd=None):
        
        if cmd!= None:
            for host in  self.invoke.hosts:
                host['cmd'] = cmd

        pool = ThreadPool(10) 

        self.result = pool.map(self.exec_cmd, self.invoke.hosts)
        
        pool.close() 
        pool.join()

    def get_result(self):

        return self.result


