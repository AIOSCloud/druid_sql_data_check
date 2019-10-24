# -*- coding: utf-8 -*-
# @Time    : 2019/10/24 上午10:56
# @Author  : xuchang
# @File    : datas.py
from Params.params import AgentBasic


def package_agent(host, db, start_time, end_time):
    agent = AgentBasic()
    url = agent.url % host
    header = agent.header
    data = agent.data
    data['query'] = data['query'] % (db, start_time, end_time)
    return url, header, data
