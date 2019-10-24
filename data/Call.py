# -*- coding: utf-8 -*-
# @Time    : 2019/10/24 上午10:56
# @Author  : xuchang
# @File    : datas.py
from Params.params import CallBasic


def package_agent(host, db, start_time, end_time):
    call = CallBasic()
    url = call.url % host
    header = call.header
    data = call.data
    data['query'] = data['query'] % (db, start_time, end_time)
    return url, header, data
