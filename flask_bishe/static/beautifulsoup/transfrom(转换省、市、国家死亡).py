import json
import random
import heapq
import numpy
import requests
import time
import csv
import pandas as pd


def heapqsort1(li):
    h = []
    for v in li:
        heapq.heappush(h, v)  # 向h列表里面添加要进行排序的列表
    return [heapq.heappop(h) for i in range(len(h))]  # 返回排序好的结果


# /***********************************************************************************/
# /**********************************************************************************
# */
# /*************************    城市死亡人数解析    ***********************************/
# /**************     数据结构为：列表--->字典--->键（str）:值列表（list）   ***********/
# /***********************************************************************************/
# /***********************************************************************************/

# /***********************************************************************************/
# /**********************************    Action    ***********************************/
# /*********************************     提取数据   ***********************************/
# /***********************************************************************************/
def ergodicArea():
    i = 0
    dict1 = {}
    dict3 = {}
    dict6 = {}
    list7 = []
    list3 = []
    list6 = []
    list10 = []
    list11 = []
    list1 = ["境外输入", "外地来湘人员", "外来返川人员", "待确认", "涉冬（残）奥闭环人员", "经济开发区", "外地来京人员", "外地来沪人员",
             "外来人员", "待确认人员", "外地来津人员", "境外来沪人员", "境外输入"]
    with open("../beautifulsoup/json/theWholeWorld.json", "r", encoding="utf-8") as area:
        erg = json.load(area)
        for i in range(len(erg["caseList"])):
            for j in range(len(erg["caseList"][i]["subList"])):
                city = erg["caseList"][i]["subList"][j]["city"]
                if city == "境外输入" or city == "外地来湘人员" or city == "外来返川人员" or city == "待确认" or \
                        city == "外来人员" or city == "待确认人员" or city == "涉冬（残）奥闭环人员" or city == "经济开发区" \
                        or city == "外地来京人员" or city == "外地来沪人员" or city == "外地来津人员" or city == "境外来沪人员" or \
                        city == "武汉":
                    continue
                else:
                    pass
                    # print(erg["caseList"][i]["subList"][j]["city"] + "\t" + erg["caseList"][i]["subList"][j]["confirmed"])
                # for k in list1:
                #     if erg["caseList"][i]["subList"][j]["city"] == k:
                #         continue
                #     else:
                #         print(erg["caseList"][i]["subList"][j]["city"] + "\t" + erg["caseList"][i]["subList"][j][
                #             "confirmed"])
                #         break

                list10.append(erg["caseList"][i]["subList"][j]["city"])
                list11.append(erg["caseList"][i]["subList"][j]["confirmed"])
                # dict1["name"] = erg["caseList"][i]["subList"][j]["city"]
                # dict3["value"] = erg["caseList"][i]["subList"][j]["confirmed"]
                # print(list10)
                # print(list11)
                dict1["name"] = list10
                dict3["value"] = list11
        print(dict3)
        print(dict1)
        list7.append(dict(dict1, **dict3))
        print(list7)
        # print(list7)
        # list3.append(dict(dict1))
        # list6.append(dict(dict3))

        save1 = open("../beautifulsoup/json/mapcity1.json", "w", encoding="utf-8")
        save2 = open("../beautifulsoup/json/mapcity2.json", 'w', encoding="utf-8")
        save3 = open("../beautifulsoup/json/mapcity4.json", 'w', encoding="utf-8")
        # print(list3)
        # print(list6)
        # print(list7)

        # for i in range(len(list7) - 1):  # 外循环控制遍历次数，这里取列表长度-1，因为有一个数字需要拿出来比较，循环多少次，久比较多少次
        #     for j in range(
        #             len(
        #                 list7) - 1 - i):  # 内循环控制第i个数字跟后面的所有数字比较的次数，这里减i是因为比较完一个数字就要拿下一个数字，前面是比较好的数字，不需要比较，所以外循环比较完完毕一次就少一个
        #         if list7[j] < list7[j + 1]:  # 判断判断数是否小于下一个数（被判断数），如果小于，那么交换双方的位置
        #             list7[j], list7[j + 1] = list7[j + 1], aaa[j]
        #     print(list7)
        json.dump(list3, save1, indent=5)
        json.dump(list6, save2, indent=5)
        json.dump(list7, save3, indent=5)
    return list7


# /***********************************************************************************/
# /*************************************    End    ***********************************/
# /***********************************************************************************/
# /***********************************************************************************/


# /***********************************************************************************/
# /**********************************    Action    ***********************************/
# /*******************************    对提取数据去最大值前十   *************************/
# /***********************************************************************************/
# 对城市死亡人数进行前十解析
# 对列表进行降序排序
def analysisArea():
    aaaa = []
    list1 = []
    list2 = []
    dict3 = {}
    aaa = ergodicArea()
    aaa = aaa[0]["value"]  # 将列表中第0位置取出来，也就是字典，一共只有一个字典，再从字典中去除value键的所有值，也就是一个列表
    print("aaa:", aaa)
    # print("shell", shell(aaa))
    print("insort", heapqsort1(aaa))
    value = list(map(int, aaa))  # 使用map将列表元素转换为int，且生成一个新数组
    value1 = list(map(int, aaa))  # 使用map将列表元素转换为int，且生成一个新数组
    index = ergodicArea()[0]["name"]
    print(value)
    print("城市index", index)

    for b in range(len(index)):
        print("%s死亡%d" % (index[b], value[b]))
    for i in range(len(value) - 1):  # 外循环控制遍历次数，这里取列表长度-1，因为有一个数字需要拿出来比较，循环多少次，久比较多少次
        for j in range(
                len(value) - 1 - i):  # 内循环控制第i个数字跟后面的所有数字比较的次数，这里减i是因为比较完一个数字就要拿下一个数字，前面是比较好的数字，不需要比较，所以外循环比较完完毕一次就少一个
            if value[j] < value[j + 1]:  # 判断判断数是否小于下一个数（被判断数），如果小于，那么交换双方的位置
                value[j], value[j + 1] = value[j + 1], value[j]
    print(value)

    # print("%s死亡%d" % (index, value))

    for o in range(7):
        aaaa.append(value[o])
    print("aaaa", aaaa)

    count3 = 0
    for m in value1:
        # print("m",m)
        for f in aaaa:
            if m == f:
                print("%s死亡%d" % (index[count3], m))
                list1.append(index[count3])
                list2.append(m)
        count3 += 1
    dict3["area"] = list1
    dict3["died"] = list2
    print(dict3)
    obj = open("../beautifulsoup/json/CityTopTen.json", "w")
    json.dump(dict3, obj, indent=5)
    obj.close()


# /***********************************************************************************/
# /*************************************    End    ***********************************/
# /***********************************************************************************/
# /***********************************************************************************/


# /***********************************************************************************/
# /*************************                       ***********************************/
# /*************************          END          ***********************************/
# /*************************                       ***********************************/
# /***********************************************************************************/


def getCaseList():
    with open("../beautifulsoup/json/theWholeWorld.json", "r", encoding="utf-8") as area:
        erg = json.load(area)
        for i in range(len(erg["caseList"])):
            pass
            # print(erg["caseList"])
            # print(erg["caseList"][i]["area"], erg["caseList"][i]["confirmed"])
        return erg["caseList"]


def getGlobalList():
    with open("../beautifulsoup/json/theWholeWorld.json", "r", encoding="utf-8") as area:
        erg = json.load(area)
        for i in range(len(erg["globalList"])):
            pass
            # print(erg["caseList"])
            # print(erg["caseList"][i]["area"], erg["caseList"][i]["confirmed"])
        return erg["globalList"]


# 省死亡人数
def Provinces():
    caseList = getCaseList()
    print(caseList)
    for i in range(len(caseList)):
        print(caseList[i]["area"], caseList["caseList"][i]["confirmed"])

        # for j in range(len(erg["caseList"][i])):
    return caseList["caseList"]


# 转换国家死亡人数
def countryDiedTop5():
    aaaa = []
    list1 = []
    list2 = []
    dict3 = {}
    dict6 = {}
    dict1 = {}
    confirmed = []
    country = []
    globalList = getGlobalList()
    newGlobalList = []
    # print(globalList)
    for i in range(len(globalList) - 1):
        # print(globalList[i])
        newGlobalList.append(globalList[i])
        for j in range(len(newGlobalList[i]["subList"])):
            # print(newGlobalList[i]["subList"][j])
            confirmed.append(newGlobalList[i]["subList"][j]["died"])
            country.append(newGlobalList[i]["subList"][j]["country"])
    index = country
    value = list(map(int, confirmed))  # 使用map将列表元素转换为int，且生成一个新数组
    value1 = list(map(int, confirmed))  # 使用map将列表元素转换为int，且生成一个新数组
    print(country)
    print(confirmed)
    print("int化value", value)

    for i in range(len(value) - 1):  # 外循环控制遍历次数，这里取列表长度-1，因为有一个数字需要拿出来比较，循环多少次，久比较多少次
        for j in range(
                len(value) - 1 - i):  # 内循环控制第i个数字跟后面的所有数字比较的次数，这里减i是因为比较完一个数字就要拿下一个数字，前面是比较好的数字，不需要比较，所以外循环比较完完毕一次就少一个
            if value[j] < value[j + 1]:  # 判断判断数是否小于下一个数（被判断数），如果小于，那么交换双方的位置
                value[j], value[j + 1] = value[j + 1], value[j]
    print("降序排序value", value)
    for k in range(6):
        aaaa.append(value[k])
    count3 = 0
    for m in value1:
        # print("m",m)
        for f in aaaa:
            if m == f:
                print("%s死亡%d" % (index[count3], m))
                list1.append(index[count3])
                list2.append(m)
        count3 += 1
    dict3["area"] = list1
    dict3["died"] = list2
    print(dict3)

    obj = open("../beautifulsoup/json/CountryTopTen.json", "w")
    json.dump(dict3, obj, indent=5)
    obj.close()


def get_tencent_data():
    """
    :return: 返回历史数据和当日详细数据
    """
    url_det = 'https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=diseaseh5Shelf'
    url_his = "https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=chinaDayList,chinaDayAddList,nowConfirmStatis,provinceCompare"
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    }

    r_det = requests.get(url_det, headers)
    r_his = requests.get(url_his, headers)
    res_det = json.loads(r_det.text)  # json字符串转字典
    res_his = json.loads(r_his.text)
    print(r_det.text)
    print(r_his.text)
    data_det = res_det['data']['diseaseh5Shelf']
    data_his = res_his['data']
    list(data_det)
    list(data_his)
    obj1 = open("../beautifulsoup/json/tencent1.json", "w")
    obj2 = open("../beautifulsoup/json/tencent2.json", "w")
    json.dump(data_his, obj1, indent=5)
    json.dump(data_det, obj2, indent=5)
    history = {}  # 历史数据


def time_stamp():
    time_stamp = 1663117928
    time_str1 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time_stamp))
    time_str2 = time.strftime('%Y-%m-%d', time.localtime(time_stamp))
    print(time_str2)


def to_time():
    time_list = []
    dict3 = {}
    conflist = []
    dead_add = []
    mean1 = []
    # list1 = []
    # datas = pd.read_csv('../beautifulsoup/test31.csv')
    # print(datas["provinceName"])
    # print(datas)
    # count = 0
    # for i in datas["provinceName"]:
    #     if i == "三明市":
    #         print(i)
    #         print(datas["updateTime"][count])
    #         str = datas["updateTime"][count]
    #         # strlist = filter(None, str.split(" "))
    #         # list1.append(datas["updateTime"][count])
    #         list1.append(str.split())
    #         print(count)
    #         count += 1
    #     else:
    #         continue
    # # print(list(set(list1)))
    # print(list1)
    # for j in list1:
    #     print(j[0])
    with open("../beautifulsoup/json/history.json", "r", encoding="utf-8") as area:
        erg = json.load(area)
        for i in range(len(erg)):
            print(erg[i]["ds"].split()[0])
            time_list.append(erg[i]["ds"].split()[0])
            conflist.append(int(erg[i]["confirm_add"]))
            dead_add.append(int(erg[i]["dead_add"]))
            mean = dead_add[i] / conflist[i]
            b = '%.2f' % (mean * 100)
            mean1.append(b)
            print(time_list)
    conflist = list(map(float, conflist))
    print(conflist)
    dict3["time"] = time_list
    dict3["confirm"] = conflist
    dict3["dead"] = dead_add
    dict3["mean"] = mean1
    obj = open("../beautifulsoup/json/history1.json", "w", encoding="utf-8")
    json.dump(dict3, obj, indent=5)


def Overseas():
    name = []
    value = []
    dict6 = {}
    with open("../beautifulsoup/json/theWholeWorld.json", "r", encoding="utf-8") as area:
        erg = json.load(area)
        for i in range(len(erg["topOverseasInput"])):
            print(erg["topOverseasInput"][i])
            name.append(erg["topOverseasInput"][i]["name"])
            value.append(erg["topOverseasInput"][i]["value"])
    dict6["area"] = name
    dict6["died"] = value
    print(dict6)
    save = open("../beautifulsoup/json/topOverseasInput.json", "w")
    json.dump(dict6, save, indent=5)


def asymptomaticTopProvince():
    name = []
    value = []
    dict6 = {}
    with open("../beautifulsoup/json/theWholeWorld.json", "r", encoding="utf-8") as area:
        erg = json.load(area)
        for i in range(len(erg["asymptomaticTopProvince"])):
            print(erg["asymptomaticTopProvince"][i])
            name.append(erg["asymptomaticTopProvince"][i]["name"])
            value.append(erg["asymptomaticTopProvince"][i]["value"])
        dict6["area"] = name
        dict6["died"] = value
        print(dict6)
        save = open("../beautifulsoup/json/asymptomaticTopProvince.json", "w")
        json.dump(dict6, save, indent=5)




def newAddTopProvince():
    name = []
    value = []
    dict6 = {}
    with open("../beautifulsoup/json/theWholeWorld.json", "r", encoding="utf-8") as area:
        erg = json.load(area)
        for i in range(len(erg["newAddTopProvince"])):
            print(erg["newAddTopProvince"][i])
            name.append(erg["newAddTopProvince"][i]["name"])
            value.append(erg["newAddTopProvince"][i]["local"])
        dict6["area"] = name
        dict6["died"] = value
        print(dict6)
        save = open("../beautifulsoup/json/newAddTopProvince.json", "w")
        json.dump(dict6, save, indent=5)

def cityConfirmed():
    # with open("../beautifulsoup/json/theWholeWorld.json", "r", encoding="utf-8") as area:
    #     erg = json.load(area)
    #     caseList = getCaseList()
    #     print(caseList)
    #     for i in range(len(caseList)):
    #         print(caseList[i]["subList"])
    #         for j in range(len(caseList[i]["subList"])):
    #             print(caseList[i]["subList"][j]["city"], caseList[i]["subList"][j]["confirmed"])
    i = 0
    dict1 = {}
    dict3 = {}
    dict6 = {}
    list7 = []
    list3 = []
    list6 = []
    index = []
    value = []
    value1 = []
    aaaa = []
    list1 = []
    list2 = []
    list111 = ["境外输入", "外地来湘人员", "外来返川人员", "待确认", "涉冬（残）奥闭环人员", "经济开发区", "外地来京人员", "外地来沪人员",
             "外来人员", "待确认人员", "外地来津人员", "境外来沪人员", "境外输入"]
    with open("../beautifulsoup/json/theWholeWorld.json", "r", encoding="utf-8") as area:
        erg = json.load(area)
        for i in range(len(erg["caseList"])):
            for j in range(len(erg["caseList"][i]["subList"])):
                city = erg["caseList"][i]["subList"][j]["city"]
                if city == "境外输入" or city == "外地来湘人员" or city == "外来返川人员" or city == "待确认" or \
                        city == "外来人员" or city == "待确认人员" or city == "涉冬（残）奥闭环人员" or city == "经济开发区" \
                        or city == "外地来京人员" or city == "外地来沪人员" or city == "外地来津人员" or city == "境外来沪人员" or \
                        city == "武汉":
                    continue
                else:
                    print(
                        erg["caseList"][i]["subList"][j]["city"] + "\t" + erg["caseList"][i]["subList"][j]["confirmed"])
                    if erg["caseList"][i]["subList"][j]["died"] == '':
                        continue
                    else:
                        index.append(erg["caseList"][i]["subList"][j]["city"])
                        value.append(erg["caseList"][i]["subList"][j]["died"])
                        value1.append(erg["caseList"][i]["subList"][j]["died"])
                # for k in list1:
                #     if erg["caseList"][i]["subList"][j]["city"] == k:
                #         continue
                #     else:
                #         print(erg["caseList"][i]["subList"][j]["city"] + "\t" + erg["caseList"][i]["subList"][j][
                #             "confirmed"])
                #         break

                # list10.append(erg["caseList"][i]["subList"][j]["city"])
                # list11.append(erg["caseList"][i]["subList"][j]["confirmed"])

        print(value)
        value = list(map(int, value))
        value1 = list(map(int, value1))

        for i in range(len(value) - 1):  # 外循环控制遍历次数，这里取列表长度-1，因为有一个数字需要拿出来比较，循环多少次，久比较多少次
            for j in range(
                    len(
                        value) - 1 - i):  # 内循环控制第i个数字跟后面的所有数字比较的次数，这里减i是因为比较完一个数字就要拿下一个数字，前面是比较好的数字，不需要比较，所以外循环比较完完毕一次就少一个
                if value[j] < value[j + 1]:  # 判断判断数是否小于下一个数（被判断数），如果小于，那么交换双方的位置
                    value[j], value[j + 1] = value[j + 1], value[j]
        print(value)

        for h in range(5):
            aaaa.append(value[h])
        print(aaaa)
        count3 = 0
        for m in value1:
            # print("m",m)
            for f in aaaa:
                if m == f:
                    print("%s死亡%d" % (index[count3], m))
                    list1.append(index[count3])
                    list2.append(m)
            count3 += 1
        dict1["area"] = list1
        dict1["died"] = list2
                # print(list10)
                # print(list11)
                # list7.append(dict(dict1, **dict3))
                # print(list7)
                # print(list7)
                # list3.append(dict(dict1))
                # list6.append(dict(dict3))

        # save1 = open("../beautifulsoup/json/mapcity1.json", "w", encoding="utf-8")
        # save2 = open("../beautifulsoup/json/mapcity2.json", 'w', encoding="utf-8")
        save3 = open("../beautifulsoup/json/mapcity6.json", 'w', encoding="utf-8")
        # print(list3)
        # print(list6)
        # print(list7)

        # for i in range(len(list7) - 1):  # 外循环控制遍历次数，这里取列表长度-1，因为有一个数字需要拿出来比较，循环多少次，久比较多少次
        #     for j in range(
        #             len(
        #                 list7) - 1 - i):  # 内循环控制第i个数字跟后面的所有数字比较的次数，这里减i是因为比较完一个数字就要拿下一个数字，前面是比较好的数字，不需要比较，所以外循环比较完完毕一次就少一个
        #         if list7[j] < list7[j + 1]:  # 判断判断数是否小于下一个数（被判断数），如果小于，那么交换双方的位置
        #             list7[j], list7[j + 1] = list7[j + 1], aaa[j]
        #     print(list7)
        # json.dump(list3, save1, indent=5)
        # json.dump(list6, save2, indent=5)
        json.dump(dict1, save3, indent=5)


if __name__ == "__main__":
    ergodicArea()
    # Provinces()
    analysisArea()
    countryDiedTop5()
    get_tencent_data()
    time_stamp()
    to_time()
    asymptomaticTopProvince()
    Overseas()
    newAddTopProvince()
    cityConfirmed()
