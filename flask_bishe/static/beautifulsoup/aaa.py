import time

from bs4 import BeautifulSoup
import requests
import re
import json
import pymysql

connect = pymysql.Connect(
host='localhost',
port=3306,
user='root',
passwd='123456',
db='bishe',
charset='utf8'
)
# 获取游标
cursor = connect.cursor()
sql_create = '''
create table if not exists data(
area varchar(100),
died int(10),
crued int(10),
curConfirm int(10),
curConfirmRelative int(10),
confirmed int(10)
) 
'''
sql_insert = '''
insert into data(area, died, crued, curConfirm, curConfirmRelative, confirmed) values('%s',%d,%d,%d,%d,%d)
'''

sql_select = '''
select area as "省份", died as "死亡数", crued as "治愈人数", curConfirm as 新增确诊, curConfirmRelative as "新增人数", confirmed as "累计确诊" from data
'''

sql_update = '''
update data set area='%s',died=%d,crued = %d,curConfirm=%d,curConfirmRelative=%d,confirmed=%d where area = "%s"
'''

# 第一步，发请求，想法请求就要有request库，要有url链接
url = "https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner"
# 伪装防止反扒
Headers = {
    'cookie': 'BIDUPSID=580FD855A26DCE31E1BEBB360D3772C1; PSTM=1633847655; __yjs_duid=1_24793f6b65b6620080c9b77e3ad3584c1633863356918; MCITY=-%3A; BAIDUID=763063B271DF62A4E6A6AA7F285E8ADD:FG=1; BDUSS=hhaVZDZEV-TDNXbjRQfnVDclVDSVk0alRwWHFZR0VYZUZyZHlDdlNlRXFyT0JpRVFBQUFBJCQAAAAAAQAAAAEAAABTx7AqTWFrb9zU19NfAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACofuWIqH7lid1; BDUSS_BFESS=hhaVZDZEV-TDNXbjRQfnVDclVDSVk0alRwWHFZR0VYZUZyZHlDdlNlRXFyT0JpRVFBQUFBJCQAAAAAAQAAAAEAAABTx7AqTWFrb9zU19NfAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACofuWIqH7lid1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=763063B271DF62A4E6A6AA7F285E8ADD:FG=1; ZFY=6tZvIKPr71ZQJI:AL9CzZV8UXOTgsK9rht51t7yidMmM:C; BA_HECTOR=2ka02gak21258k842h1hc21gc14; ___wk_scode_token=0RzJzAvDvqgQibh7RV3MBKMrHHl9SxwNQPTtGegoS7A%3D; lscaptain=srcactivitycaptainindexcss_91e010cf-srccommonlibsesljs_e3d2f596-srcactivitycaptainindexjs_a2e9c712; delPer=0; PSINO=1; ab_sr=1.0.1_MDU2M2VkMmYyZDAzNGY4OGE2YjlkN2Y1MDEzODYyMmMzMGU3Yzk2M2ZjYWQzMDU3NTU3YTQxNjlkOTYwYzY2ZmJlY2ZmMTUwNWEzZDUxYTQwNGE1NjQxZGEyZDE4ZDBmODlhMzU2NGU0MDBkMTg3MjJmMGI4OTA1NWUwN2Q1MTZmMjhhMjkxZGEzMzhkMGQ4ZDI1Y2RlZjRjOTljYWRhYw==; H_PS_PSSID=36550_36502_36454_36690_36165_36694_36698_36653_36775_36746_36763_36768_36766_26350_36469_36712_36651; Hm_lvt_68bd357b1731c0f15d8dbfef8c216d15=1655651590,1655651973,1656856116,1656894526; Hm_lpvt_68bd357b1731c0f15d8dbfef8c216d15=1656894526',
    'referer': 'https://www.baidu.com/s?ie=UTF-8&wd=%E7%96%AB%E6%83%85',
    'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44'
}
# 将头添加至get（）方法内，发送请求
response = requests.get(url=url)
# 2.获取数据
html_data = response.text
# 解析数据，输出一个列表
# print(re.findall('"component":\[(.*)\],',html)[0])
json_data = re.findall('"component":\[(.*)\],',html_data)[0]
# 转换字典
json_dict = json.loads(json_data)
caseList = json_dict['caseList']

for case in caseList:
    died = case['died']     # 死亡数
    area = case['area']     # 省份
    confirmed = case['confirmed']       # 累计确诊
    curConfirmRelative = case['curConfirmRelative']     # 当前确诊人数
    curConfirm = case['curConfirm']     #新增确诊
    crued = case['crued']       # 治愈人数
    print(area, died, crued, curConfirm, curConfirmRelative, confirmed)
    data_update = (str(area), int(died), int(crued), int(curConfirm), int(curConfirmRelative), int(confirmed))
    data_insert = (str(area), int(died), int(crued), int(curConfirm), int(curConfirmRelative), int(confirmed))

    cursor.execute(sql_insert % data_insert)
    connect.commit()
    try:
        f = open("data.json", "a")
        data_json = f.read()
        data_json = json.loads(data_json)
        f.close()
    except:
        print("读取错误")
        data_json = {}










print("成功")

connect.close()
