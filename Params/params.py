# -*- coding: utf-8 -*-
# @Time    : 2019/10/24 上午10:56
# @Author  : xuchang
# @File    : datas.py

import os
from Params import tools
from common import Log

log = Log.MyLog()
path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))


def get_parameter(name):
    data = tools.GetPages().get_page_list()
    param = data[name]
    return param


class AgentBasic:
    def __init__(self):
        log.info('解析yaml,Path:' + path_dir + '/params/Yaml/Agent.yaml')
        params = get_parameter('Agent')
        self.url = params['url']
        self.header = params['header']
        self.data = params['json']


class CallBasic:
    def __init__(self):
        log.info('解析yaml,Path:' + path_dir + '/params/Yaml/Agent.yaml')
        params = get_parameter('Call')
        self.url = params['url']
        self.header = params['header']
        self.data = params['json']


class TrunkBasic:
    def __init__(self):
        log.info('解析yaml,Path:' + path_dir + '/params/Yaml/Agent.yaml')
        params = get_parameter('Trunk')
        self.url = params['url']
        self.header = params['header']
        self.data = params['json']


class QueueBasic:
    def __init__(self):
        log.info('解析yaml,Path:' + path_dir + '/params/Yaml/Agent.yaml')
        params = get_parameter('Trunk')
        self.url = params['url']
        self.header = params['header']
        self.data = params['json']
