"""
坐席相关的指标进行查询
"""
import pytest
from config.conf import *
from data import Agent
from query import query

online_url, online_header, online_json = Agent.package_agent(online_host, online_db, start, end)
offline_url, offline_header, offline_json = Agent.package_agent(offline_host, offline_db, start, end)
online_data = query.query(online_url, online_json)
offline_data = query.query(offline_url, offline_json)


@pytest.fixture(params=online_data.index)
def index(request):
    return request.param


def test_agent(index):
    line_online = online_data.loc[index]
    line_offline = offline_data[(offline_data["dataDate"] == line_online["dataDate"]) & (
            offline_data["vccId"] == line_online["vccId"]) & (offline_data["agId"] == line_online["agId"])]
    if line_offline.index > 0:
        line_offline = line_offline.loc[line_offline.index[0]]
        print("测试:\n" + str(line_offline))
        print("线上:\n" + str(line_online))
        assert (line_offline.values == line_online.values).all()
    else:
        print("测试:\n" + str(line_offline))
        print("线上:\n" + str(line_online))
        line_offline = line_offline.loc[line_offline.index[0]]
        assert (line_offline.values == line_online.values).all()
    pass
