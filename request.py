mport requests
import time
import random
import pandas as pd
# 定义一个函数用来更新cookies
def cookies_update(url, my_headers):
    # 自动获取cookies
    s = requests.Session()
    s.get(url, headers=my_headers)
    cookies = s.cookies
    return cookies
# 定义一个爬虫函数
def crawler(req_url, my_headers, cookies, qs_params, form_data):
    # 发送请求
    req_result = requests.post(req_url, headers=my_headers, cookies=cookies,
                           params=qs_params, data=form_data)
    # 将请求结果转换为字典
    result = req_result.json()
    # 提取职位相关的信息并输出
    positions_info = result["content"]["positionResult"]["result"]
    # for循环遍历职位列表并输出
    # 定义一个字典保存每一页的职位信息
    positions = {
            '职位名称': [],
            '公司名称': [],
            '薪资': []
            }
    for i in range(len(positions_info)):
        positions["职位名称"].append(positions_info[i]["positionName"])
        positions["公司名称"].append(positions_info[i]["companyShortName"] )
        positions["薪资"].append(positions_info[i]["salary"] )
    return positions
if __name__ == "__main__":
    # request url
    req_url = '请输入你的URL信息'
    # headers
    my_headers = {
        'Referer': '请输入你的Referer信息',
        'User-Agent': '请输入你的User-Agent信息'
    }
    qs_params = {'needAddtionalResult': 'false'}
    #定义一个字典保存所有的职位信息
    positions_all = {
            '职位名称': [],
            '公司名称': [],
            '薪资': []
            }
    form_data = {'kd':'python'}
    for n in range(1, 6):
        print("爬取第{}页的数据".format(n))
        updated_cookies = cookies_update(my_headers["Referer"], my_headers)
        form_data['pn'] = n
        if n == 1:
            form_data['first'] = True
        else:
            form_data['first'] = False
        positions_page = crawler(req_url, my_headers, updated_cookies,
                    qs_params, form_data)
        positions_all['职位名称'] += positions_page['职位名称']
        positions_all['公司名称'] += positions_page['公司名称']
        positions_all['薪资'] += positions_page['薪资']
        sleep_time = random.randint(3,15)
        time.sleep(sleep_time)
    result = pd.DataFrame(positions_all)
    result.to_excel('./tmp/Python_position.xlsx')