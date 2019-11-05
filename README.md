#配置sql,根据sql查询结果,进行数据对比校验# druid_sql_data_check
pytest + allure 数据最对比,最终展示子页面上,方便用户对数据问题进行排查

python包
pip install pytest==4.0.2
pip install py.test
pip install pytest-allure-adaptor

#Mac下安装allure
brew install allure

#执行测试用例,生成测试报告 
python3 $(which py.test) -v --alluredir result 
#清除历史报告,将测试用例的报告转化成可展示优美的HTML报告 
allure generate result -o report --clean 
#在本地创建服务,展示 
allure open -h 127.0.0.1 -p 8083 report