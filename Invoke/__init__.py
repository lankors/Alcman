#!/usr/bin/env python
#coding=utf-8


class invoke(object):

    def __init__(self):

        self.hosts  = []
        self.ssh    = None

    def set_config(self,config=None,group=None):

        if group == None:
            self.hosts = config.get_hosts()['hosts']
        else:
            self.hosts = config.get_hosts()[group]

    def set_actuator(self,actuator=None):
        self.actuator = actuator