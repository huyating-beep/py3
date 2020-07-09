# encoding: utf-8 
# @time: 2020/7/2 2:10 下午
# @author: hyt
# @contact: 2621408918@qq.com

# 导入requests
# import sys
# import os
# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = os.path.split(curPath)[0]
# sys.path.append(rootPath)


# import sys
# sys.path.append("/Users/huyating/PycharmProjects/python_test")
import requests
# 接口函数
def http_requests(url, method, data, token=None):
    global res_alljson
    header = {'X-Lemonban-Media-Type': 'lemonban.v2',
              'Authorization': token}
    # 判断请求方式
    if method == 'get':
        request = requests.get(url, json=data, headers=header);
    else:
        request = requests.post(url, json=data, headers=header);
    # json格式输出
    res_alljson = request.json()
    print(res_alljson)
    return res_alljson


if __name__ == '__main__':
    ip_address = 'http://120.78.128.25:8766'
    iphone = 15137912350
    pwd = "lemon123456"
    # 注册信息
    reg_url = ip_address + "/futureloan/member/register"
    reg_data = {"mobile_phone": iphone, "pwd": pwd, "type": "1", "reg_name": "会员用户lemon"}
    # 登录信息
    log_url = ip_address + "/futureloan/member/login"
    log_data = {"mobile_phone": iphone, "pwd": pwd}
    # 充值信息
    rec_url = ip_address + "/futureloan/member/recharge"
    rec_data = {"member_id": 207368, "amount": "100"}
    # 提现信息
    wit_url = ip_address + "/futureloan/member/withdraw"
    wit_data = {"member_id": 207368, "amount": "0.01"}
    # 注册调用
    http_requests(reg_url, 'post', reg_data)
    # 登录调用
    http_requests(log_url, 'post', log_data)
    # 登录后返回的token值
    token = res_alljson['data']['token_info']['token']
    # 充值调用
    http_requests(rec_url, 'post', rec_data, 'Bearer ' + token)
    # 提现调用
    http_requests(wit_url, 'post', wit_data, 'Bearer ' + token)
