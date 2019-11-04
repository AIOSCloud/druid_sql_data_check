# -*- coding: utf-8 -*-
# @Time    : 2019/10/24 上午10:56
# @Author  : xuchang
# @File    : datas.py
from Params.params import TrunkBasic


def package_trunk(host, db, start_time, end_time):
    call = TrunkBasic()
    url = call.url % host
    header = call.header
    data = call.data
    data['query'] = data['query'] % (db, start_time, end_time)
    print(data['query'])
    return url, header, data
