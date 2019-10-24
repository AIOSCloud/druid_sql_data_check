#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pydruid.client import PyDruid
import configparser
import datetime
import os

parser = configparser.ConfigParser()
parser.read(os.path.join(os.path.join(os.path.dirname(__file__)).split("common")[0], 'env.ini'))
online_host = parser.get('druid-prod', 'host')
online_db = parser.get('druid-prod', 'db')
offline_host = parser.get('druid-test', 'host')
offline_db = parser.get('druid-test', 'db')
start = parser.get('common', 'start')
end = parser.get('common', 'end')
