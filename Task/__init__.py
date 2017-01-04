#!/usr/bin/env python
# coding=utf-8

from multiprocessing.dummy import Pool as ThreadPool

# from multiprocessing import Pool as ThreadPool

'''
mail:wqc2008@gmail.com
createtime:2016-7-20 18:00:00
usege:
    根据组装参数来执行任务列表

'''

__all__ = ['task']


class task(object):
    def __init__(self, invoke, thread_nums=500):

        self.invoke = invoke

        #设置开启进程池数,如果小于100个服务器,就只开相对于服务数量的线程数
        if len(self.invoke.hosts) < 100:

            self.thread_nums = len(self.invoke.hosts)
        else:

            self.thread_nums = thread_nums

        self.result = []

    def exec_cmd(self, host):
        '''
        在线程池中调用线程化的ssh
        注意:对于socket和ssh在同一时间不能做多次连接
        :param host:
        :return:
        '''

        from Alcman.Actuator import actuator
        atr = actuator(host)
        atr.start()
        atr.join()
        return atr.get_result()

    def run(self):
        '''
        任务进行进程池管理,避免开的线程过多,拖死服务器
        :return:
        '''

        pool = ThreadPool(self.thread_nums)

        self.result = pool.map(self.exec_cmd, self.invoke.hosts)

        pool.close()
        pool.join()

    def get_result(self):

        return self.result