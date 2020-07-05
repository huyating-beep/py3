# encoding: utf-8
# @time: 2020/7/2 2:44 下午
# @author: hyt
# @contact: 2621408918@qq.com
# 导入方法
from httprequests import http_requests
from R_W_excels import read_data
from R_W_excels import wite_data

Token = None


def runs(wb_name, sheet_name, c1, c2):
    global Token
    ip_address = 'http://120.78.128.25:8766'
    wbs = read_data(wb_name, sheet_name)
    for wb_date in wbs:
        response = http_requests(ip_address + wb_date[4], wb_date[3], eval(wb_date[5]), token=Token)
        if 'login' in wb_date[4]:
            Token = "Bearer " + response['data']['token_info']['token']
        print(response)
        # 写入执行数据结果
        wite_data(wb_name, sheet_name, wb_date[0] + 1, c1, str(response))

        actual = {'code': response['code'], 'msg': response['msg']}
        if eval(wb_date[6]) == actual:
            wite_data(wb_name, sheet_name, wb_date[0] + 1, c2, 'pass')
        else:
            wite_data(wb_name, sheet_name, wb_date[0] + 1, c2, 'fial')


runs('test_py.xlsx', 'info_test', 8, 9)
