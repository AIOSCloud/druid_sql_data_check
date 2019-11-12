# -*- coding: utf-8 -*-
# @Time    : 2019/10/24 上午10:56
# @Author  : xuchang
# @File    : datas.py
from Params.params import QueueBasic


def package_queue(host, db, start_time, end_time):
    queue = QueueBasic()
    url = queue.url % host
    header = queue.header
    data = queue.data
    data['query'] = data['query'] % (db, start_time, end_time)
    return url, header, data
