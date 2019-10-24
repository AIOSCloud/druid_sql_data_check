import requests
import pandas as pd
import json


# 根据用户给的url和查询的sql,查询数据并返回DataFrame
def query(url, body):
    print(url)
    response = requests.post(url, json=body)
    print(response.text)
    return pd.DataFrame(json.loads(response.text))
