import pandas as pd


df = pd.read_csv('./json/DXYArea_20220822.csv')
# df.style.hide_index()
print(df)

# pd.DataFrame.from_dict(dict1)

df.to_csv('test3.csv', columns=["provinceName", "province_confirmedCount", "province_suspectedCount",
                                "province_deadCount", "province_curedCount",  "cityName",
                                "city_confirmedCount",  "city_suspectedCount", "city_deadCount",
                                "city_curedCount", "updateTime"], index=False)


# province = df["provinceName"]  # 省
# updateTime = df["updateTime"]  # 最后更新时间
#
# province_curedCount = df["province_curedCount"]  # 省治愈人数
# city_curedCount = df["city_curedCount"]  # 市治愈人数
#
# province_suspectedCount = df["province_suspectedCount"]  # 省疑似病例
# city_suspectedCount = df["city_suspectedCount"]  # 市疑似病例
#
# province_deadCount = df["province_deadCount"]  # 省死亡人数
# city_deadCount = df["city_deadCount"]  # 市死亡人数
#
# province_confirmedCount = df["province_confirmedCount"]  # 省感染计数
# city_confirmedCount = df["city_confirmedCount"]  # 市治愈人数
#
# print(province, updateTime, province_confirmedCount, city_confirmedCount, province_curedCount, city_curedCount,
#       province_deadCount, city_deadCount, province_suspectedCount, city_suspectedCount)




