#!/usr/bin/env python
#coding=utf-8

from multiprocessing.dummy import Pool as ThreadPool 



class task(object):

    def __init__(self,invoke):

        self.invoke  = invoke
        self.result =  None


    def exec_cmd(self, host):
        
        return self.invoke.actuator.run(host)
        

    def run(self):
        
        pool = ThreadPool(10) 

        self.result = pool.map(self.exec_cmd, self.invoke.hosts)
        
        pool.close() 
        pool.join()

    def get_result(self):

        return self.result


