# -*- coding: utf-8 -*-
# @Time    : 2019/10/24 上午10:56
# @Author  : xuchang
# @File    : datas.py
from Params.params import TrunkBasic


def package_trunk(host, db, start_time, end_time):
    trunk = TrunkBasic()
    url = trunk.url % host
    header = trunk.header
    data = trunk.data
    data['query'] = data['query'] % (db, start_time, end_time)
    print(data['query'])
    return url, header, data
