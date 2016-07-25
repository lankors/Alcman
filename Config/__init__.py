#!/usr/bin/env python
#coding=utf-8

import yaml

'''
mail:wqc2008@gmail.com
createtime:2016-7-20 18:00:00
usege:
    设置yaml文件来读取host信息
    
'''

__all__ = ['config']

class config(object):


    def __init__(self,filename):

        self.filename = filename

    def __del__(self):
        pass


    def set_host(self,data={}):

      
        stream=file(self.filename,'w')

        yaml.dump(data,stream,encoding='utf-8',allow_unicode=True)


    def get_hosts(self):
   

        return yaml.load(file(self.filename, 'r'))
  
'''
if __name__ == '__main__':

    y = config(filename='../servers.yaml')

    data={'hosts':[
                    {'host':'192.168.56.101','username':'username','passwd':'123456','cmd':'ls'},
                    {'host':'192.168.56.102','username':'username','passwd':'123456','cmd':'uptime'}
                ]}
    y.set_host(data=data)

    print y.get_hosts(group='hosts')
'''
