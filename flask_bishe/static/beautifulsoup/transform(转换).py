import json
import re


# 遍历json中的caseList键中的0键中的dangerousAreas(高危城市)键,subList（高位城市子表）键中的0键中的area（城市）键
# 就是查看风险城市
def select_dangerousAreas():
    with open("../beautifulsoup/json/theWholeWorld.json", "r",
              encoding="utf-8") as dictObj:  # 使用open（）方法读取外部json文件，将as重命名为dictObj
        obj1 = json.load(dictObj)  # 使用json.load读取已经拿到的文本数据，将dictObj文本内容转换为dict，使用obj1存储
        print(len(obj1["caseList"]))
        for j in range(
                len(obj1["caseList"])):  # 使用for循环遍历，以caseList键的长度为结束为外循环结束条件，外循环是caseList的下标，caseList包含很多subList（子表）
            for submitJ in range(len(obj1["caseList"][j]["dangerousAreas"][
                                         "subList"])):  # 以caseList键中的0-34键中的dangerousAreas键中的subList键中的area长度作为内循环结束条件，内循环是caseList中subList（caseList的子表）的下标
                print(obj1["caseList"][j]["dangerousAreas"]["subList"][submitJ]["level"] + "\t\t\t" +
                      obj1["caseList"][j]["dangerousAreas"]["subList"][submitJ]["area"])


# 遍历json中的caseList键
def select_China_all():
    with open("../beautifulsoup/json/test.json", "r") as dictObj:  # 使用open（）方法读取外部json文件
        obj2 = json.load(dictObj)  # 使用json.load读取已经拿到的文本数据，转换为dict
        for count1 in range(len(obj2)):  # 使用for循环遍历每个dict字典下标
            print(obj2[count1])  # 每个省的个个城市，每个省份就是一个下标
        print(len(obj2))  # 中国一共对应34个省，所以计数34,这里打印obj2的长度，obj2中存储了中国个城市的信息，长度是多少，城市就有多少
        dictObj.close()


# 遍历json中的caseList键中的0键中的area(城市)键,died（死亡）键
def select_died():
    list1 = []
    list2 = []
    list3 = []
    dict1 = {"area": [], "died": []}
    dict2 = {}

    with open("../beautifulsoup/json/theWholeWorld.json", "r",
              encoding="utf-8") as dictObj:  # 使用open（）方法读取外部json文件，且用as重命名为dictObj
        obj3 = json.load(dictObj)  # 使用json.load读取已经拿到的文本数据，转换为dict，使用obj3存放转换后的数据
        print(len(obj3["caseList"]))  # 由于它带有很多其他信息，这里只打印众多键中的caseList（做筛选）
        for count3 in range(len(
                obj3["caseList"])):  # 使用for循环遍历每个dict字典下标,len(obj3["caseList"])，使用obj3对象中caseList键的长度来遍历，而不是使用obj3对象的长度
            print(obj3["caseList"][count3]["area"] + "\t死亡\t" + obj3["caseList"][count3]["died"])
            # 1.我们获取到了文本对象obj3  2.将他的caseList键长度为循环结束条件 3.循环内打印每个caseList中0-34键中area键的值
            list1.append(obj3["caseList"][count3]["died"])  # 使用列表接收每一次遍历的结果，这里设置列表是因为我们可视化数据的键：值的值需要用列表，这更有助于数据可视化
            list2.append(obj3["caseList"][count3]["area"])
        dictObj.close()

        obj4 = open("../beautifulsoup/json/diedTopFive.json", 'w', encoding="utf-8")  # 新开一个open对象，用来进行json的存储

        dict1["died"] = list1  # 指定died键 = 列表，这样的字典结构就是：键1：列表1，这里的列表就是值，达到Echarsa可视化数据的列表格式
        dict1["area"] = list2  # 指定area键 = 列表，这样的字典结构就是：键2：列表2，这里的列表就是值，以达到Rchars可视化数据的列表格式
        json.dump(dict1, obj4, indent=5)  # 使用dump（要写入的json文本dict1，open()读取的文本对象obj3）将所有的键值对写入json文件
        list3 = [list1, list2]
        obj4.close()

        # for k in list2:

        # json.dump(json_dict, objSubDict)

        # print(json.load(obj3["caseList"][count3]["area"]))

        # print(len(obj3))  # 中国一共对应34个省，所以计数34,这里打印obj2的长度，obj2中存储了中国个城市的信息，长度是多少，城市就有多少
        return list3


def select_died_topFive():
    dict1 = {"area": [], "died": []}
    list1 = []
    list2 = []
    aaaa = []
    all_data = select_died()  # 获取分析死亡数方法的返回值，返回值是一个二维列表，0是死亡数列表，1是地区列表
    print(all_data)
    data1 = select_died()[0]
    print("se", select_died())
    print("se[0]", data1)
    data1 = list(map(int, data1))
    print("intda", data1)
    aaa = list(
        map(int, all_data[0]))  # 将select_died返回值列表中的0下标列表转换为数值型列表，使用map（）方法，由于map（数值类型，列表）方法返回的是map对象，所以用list（）方法转换为列表
    print("listda", aaa)
    bbb = all_data[1]

    '''======================================================================================================================'''
    # 冒泡排序，从小到大排列
    print("aaa:", aaa)
    for i in range(len(aaa) - 1):  # 外循环控制遍历次数，这里取列表长度-1，因为有一个数字需要拿出来比较，循环多少次，久比较多少次
        for j in range(
                len(aaa) - 1 - i):  # 内循环控制第i个数字跟后面的所有数字比较的次数，这里减i是因为比较完一个数字就要拿下一个数字，前面是比较好的数字，不需要比较，所以外循环比较完完毕一次就少一个
            if aaa[j] < aaa[j + 1]:  # 判断判断数是否小于下一个数（被判断数），如果小于，那么交换双方的位置
                aaa[j], aaa[j + 1] = aaa[j + 1], aaa[j]
        # print(aaa)
    '''======================================================================================================================'''

    # count3 = 0  # 下标
    # data1 = select_died()[0]，data1是原始未进行大到小排序的数组，是原始下标
    # 由m存放每次遍历出来的未排序的值
    # for m in data1:
    #     # print("下标为：%d值为：%d" % (count3, m))
    #     for f in aaa:   # aaa = list(map(int, all_data[0]))，aaa代表数字化后的经过冒泡排序从小到大排序列表，为了能排序过后还能让值一一对应原来未排序的下标，这里使用了双重循环
    #         # 第一重循环外循环：是未经过排序的data1，每一次循环都用count3存储每一次下标，也就是说，未排序的下标由count3存储
    #         # 第二重循环内循环：是已经经过排序的aaa，每一次循环都将m（未排序值）与f（已排序值）进行判断相等，外循环循环一次，就会让m一个对比f多个，只要m=f匹配上，那么久输出：bbb的第count3个+未排序的值
    #         # bbb = all_data[1]，bbb是all_data的第二个值，是城市列表
    #         if m == f:
    #             # print("%s对应下标为%d" % (f, count3))
    #             # print("%s对应下标%d" % (f, count3))
    #             print("%s死亡%d" % (bbb[count3], m))
    #             dict1["area"] =
    #             break
    #     count3 += 1
    '''======================================================================================================================'''
    # 对前五进行切割
    import json
    for o in range(5):
        aaaa.append(aaa[o])
    print("aaaa", aaaa)
    count3 = 0
    for m in data1:
        print("m", m)
        for f in aaaa:
            if m == f:
                print("%s死亡%d" % (bbb[count3], m))
                list1.append(bbb[count3])
                list2.append(m)
        count3 += 1
    dict1["area"] = list1
    dict1["died"] = list2
    # aaaa = list(map(str, aaaa))
    # dict1["died"] = aaaa
    print(dict1)

    print("===================")

    f1 = open("../beautifulsoup/json/diedTrueTopFive.json", "w")
    json.dump(dict1, f1, indent=5)
    f1.close()

    # for h in data1:
    #     print("下标为：%d值为：%daaa" % (count, h))
    #     count += 1
    #     for k in bbb:
    #         if count == count1:
    #             print("%s\t的下标为\t%d" % (k, count))
    #         count1 += 1


def theWholeWorld_analyse():
    import json
    dict103 = {}
    dict104 = {}
    dict106 = {}
    dict107 = {}

    dict_list = []
    with open("../beautifulsoup/json/theWholeWorld.json", "r") as dictData:
        obj67 = json.load(dictData)
        for i in range(len(obj67["globalList"]) - 2):
            # print(len(obj67["globalList"])-2)
            # print(obj67["globalList"][i])
            # print(obj67["globalList"][i]["subList"])     # [gobList键]-[0-6键]-[subList键]-[0-45键]-[confirmed]/[country]
            for j in range(len(obj67["globalList"][i]["subList"])):
                print(
                    obj67["globalList"][i]["subList"][j]["country"] + obj67["globalList"][i]["subList"][j]["confirmed"])

                dict103["name"] = obj67["globalList"][i]["subList"][j]["country"]
                dict104["value"] = obj67["globalList"][i]["subList"][j]["confirmed"]

                print(dict103, dict104)
                dict_list.append(dict(dict103, **dict104))  # 使用字典解压合并两个字典

        print(obj67["summaryDataIn"]["confirmed"])
        dict106["name"] = obj67["message"]["inner"][0]["country_area"]
        dict107["value"] = obj67["summaryDataIn"]["confirmed"]
        dict_list.append(dict(dict106, **dict107))
        print(dict_list)

        f1 = open("../beautifulsoup/json/the_whole_world_data.json", "w")
        json.dump(dict_list, f1, indent=5)
        f1.close()

        #     dict1["name"] = obj67["globalList"][i]["subList"][j]["country"]
        #     dict1["value"] = obj67["globalList"][i]["subList"][j]["confirmed"]
        # print(dict1)
        # dict_list.append(dict1)
        # f1 = open("../beautifulsoup/json/the_whole_world_data.json", "a")
        # json.dump(dict_list, f1, indent=5)
        # print(dict_list)


def all_China_City():
    list1 = []
    list2 = []
    dict_list13 = []
    dict1 = {}
    dict306 = {}
    dict307 = {}

    with open("../beautifulsoup/json/theWholeWorld.json", "r",
              encoding="utf-8") as dictObj:  # 使用open（）方法读取外部json文件，且用as重命名为dictObj
        obj3 = json.load(dictObj)  # 使用json.load读取已经拿到的文本数据，转换为dict，使用obj3存放转换后的数据
        print(len(obj3["caseList"]))  # 由于它带有很多其他信息，这里只打印众多键中的caseList（做筛选）
        for count3 in range(len(
                obj3["caseList"])):  # 使用for循环遍历每个dict字典下标,len(obj3["caseList"])，使用obj3对象中caseList键的长度来遍历，而不是使用obj3对象的长度
            print(obj3["caseList"][count3]["area"] + "\t死亡\t" + obj3["caseList"][count3]["died"])
            # 1.我们获取到了文本对象obj3  2.将他的caseList键长度为循环结束条件 3.循环内打印每个caseList中0-34键中area键的值
            # list1.append(int(obj3["caseList"][count3]["died"]))  # 使用列表接收每一次遍历的结果，这里设置列表是因为我们可视化数据的键：值的值需要用列表，这更有助于数据可视化
            # list2.append(obj3["caseList"][count3]["area"])
            dict306["name"] = obj3["caseList"][count3]["area"]
            dict307["value"] = int(obj3["caseList"][count3]["died"])
            dict_list13.append(dict(dict306, **dict307))
        print(dict306, dict307)
        dictObj.close()

        obj4 = open("../beautifulsoup/json/index_the_Whole_world_data.json", 'w',
                    encoding="utf-8")  # 新开一个open对象，用来进行json的存储

        print(dict_list13)
        # dict1["name"] = list1  # 指定died键 = 列表，这样的字典结构就是：键1：列表1，这里的列表就是值，达到Echarsa可视化数据的列表格式
        # dict1["value"] = list2  # 指定area键 = 列表，这样的字典结构就是：键2：列表2，这里的列表就是值，以达到Rchars可视化数据的列表格式
        json.dump(dict_list13, obj4, indent=5)  # 使用dump（要写入的json文本dict1，open()读取的文本对象obj3）将所有的键值对写入json文件
        list3 = [list1, list2]
        obj4.close()


# ergodicArea，遍历caselist中area省份中的city城市
# 百度地图数据源，数据结构为json，具体结构为列表--->字典--->键（str）:值（int）
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
                    print(
                        erg["caseList"][i]["subList"][j]["city"] + "\t" + erg["caseList"][i]["subList"][j]["confirmed"])
                # for k in list1:
                #     if erg["caseList"][i]["subList"][j]["city"] == k:
                #         continue
                #     else:
                #         print(erg["caseList"][i]["subList"][j]["city"] + "\t" + erg["caseList"][i]["subList"][j][
                #             "confirmed"])
                #         break
                dict1["name"] = erg["caseList"][i]["subList"][j]["city"]
                dict3["value"] = erg["caseList"][i]["subList"][j]["confirmed"]
                # print(dict3)
                # print(dict1)
                list7.append(dict(dict1, **dict3))
                list3.append(dict(dict1))
                list6.append(dict(dict3))

        save1 = open("../beautifulsoup/json/mapcity1.json", "w", encoding="utf-8")
        save2 = open("../beautifulsoup/json/mapcity2.json", 'w', encoding="utf-8")
        save3 = open("../beautifulsoup/json/mapcity3.json", 'w', encoding="utf-8")
        print(list3)
        print(list6)
        print(list7)

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


# /***********************************************************************************/
# /*舍弃*/
# /***********************************************************************************/


# def getHeatMapData():
#     list1 = []
#     dict1 = {}
#     dict2 = {}
#     dict3 = {}
#     list6 = []
#     list7 = []
#     list8 = []
#     coord = open("./json/coord.txt", "r", encoding="utf-8")
#     # list1 = coord.read()
#     # print(list1)
#     count = 0
#     allValue = 0
#     leftValue = 0
#     rightValue = 0
#     for i in coord:
#         # 1. 表达式: X.*?Y（“.“表示任意字符，“？”表示匹配0个或多个）
#         # 示例: Xabab
#         # 结果: XababcdcY
#         # 2. 表达式: X.*?(?=Y)
#         # 示例: XabadY
#         # 结果:  Xabad
#         # 表达式: (?<=X).*?(?=Y)
#         # 示例: XababY
#         # 结果: abab
#
#
#         city = re.findall('(?<=").*?(?=")', i)
#         # value = re.findall('(?<=\[).*?(?=\])', i)
#         # print(re.findall('^,', value))
#         allValue = re.findall('(?<=\[).*?(?=\])', i)
#         # print(allValue)
#         leftValue = re.findall('(?<=\[).*?(?=\,)', i)
#         rightValue = re.findall('(?<=,).*(?=\])', i)
#         # dict1 = {"lng":,"lat":,"count":}
#         # print(leftValue)
#         # print(rightValue)
#     with open("./json/mapcity3.json", "r", encoding="utf-8") as Map1:
#         map1 = json.load(Map1)
#         count1 = 0
#         for q in map1:
#             print(map1[count1]["value"])
#             list7.append(map1[count1]["value"])
#             count1 += 1
#         for j in range(len(allValue)):
#             dict1["lng"] = leftValue[j]
#             dict2["lat"] = rightValue[j]
#             dict3["count"] = list7[j]
#             save = open("../beautifulsoup/json/coord.json", "w", encoding="utf-8")
#             list6.append(dict(dict1, **dict2, **dict3))
#             json.dump(list6, save, indent=5)
#             print(list6)


# /***********************************************************************************/
# /*舍弃*/
# /***********************************************************************************/


# list8 = [list6,list7]
#         print(list6)
# print(list7)


# print(j)
# dict1["lng"] = leftValue[j]
# dict1["lat"] = rightValue[j]
# print(dict1)


# print(re.findall('(?<=").*?(?=")', i))
# print(re.findall('\[.*?\]', i))
# print(re.findall('(?<=\[).*?(?=\])', i))
#


# list1 = sorted(leftValue + rightValue)
# print("right", city)
# print("left", leftValue)
# print("right", rightValue)
# print("all", list1)

# print("right", allValue)


# list1.append("{" + "\"" + f"{coord.readline()}" + "\"" + "}")
# print(value)
# print(city)
# dict1 = {}
# count += 1

# print(list1)

# save = open("./json/coord.json", "w", encoding="utf-8")
# json.dump(list1, save, indent=5)
# with open("../beautifulsoup/json/coord.json") as cpp:
#     coord13 = json.loads(cpp)
#     print(coord13)


# /***********************************************************************************/
# /*舍弃*/
# /***********************************************************************************/


# def Global_died_data():
#     # city
#     with open("../beautifulsoup/json/theWholeWorld.json", "r",
#               encoding="utf-8") as dictObj:  # 使用open（）方法读取外部json文件，将as重命名为dictObj
#         obj1 = json.load(dictObj)  # 使用json.load读取已经拿到的文本数据，将dictObj文本内容转换为dict，使用obj1存储
#         for i in range(len(obj1["caseList"])):
#             print(obj1["caseList"])
#             for j in range(len(obj1["caseList"][i]["subList"])):
#                 city = obj1["caseList"][i]["subList"][j]["city"]
#                 # print(obj1["caseList"][i]["subList"][j])
#                 print(obj1["caseList"][i]["subList"][j]["city"])

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
                    print(
                        erg["caseList"][i]["subList"][j]["city"] + "\t" + erg["caseList"][i]["subList"][j]["confirmed"])
                # for k in list1:
                #     if erg["caseList"][i]["subList"][j]["city"] == k:
                #         continue
                #     else:
                #         print(erg["caseList"][i]["subList"][j]["city"] + "\t" + erg["caseList"][i]["subList"][j][
                #             "confirmed"])
                #         break

                # list10.append(erg["caseList"][i]["subList"][j]["city"])
                # list11.append(erg["caseList"][i]["subList"][j]["confirmed"])
                dict1["name"] = erg["caseList"][i]["subList"][j]["city"]
                dict3["value"] = erg["caseList"][i]["subList"][j]["confirmed"]
                # print(list10)
                # print(list11)
                list7.append(dict(dict1, **dict3))
                print(list7)
                # print(list7)
                # list3.append(dict(dict1))
                # list6.append(dict(dict3))

        save1 = open("../beautifulsoup/json/mapcity1.json", "w", encoding="utf-8")
        save2 = open("../beautifulsoup/json/mapcity2.json", 'w', encoding="utf-8")
        save3 = open("../beautifulsoup/json/mapcity3.json", 'w', encoding="utf-8")
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


def worldTop():
    value = []
    value1 = []
    index = []
    dict3 = {}
    aaaa = []
    list1 = []
    list2 = []
    with open("../beautifulsoup/json/the_whole_world_data.json", "r",
              encoding="utf-8") as dictObj:  # 使用open（）方法读取外部json文件，且用as重命名为dictObj
        erg = json.load(dictObj)
        print(erg)
        for i in range(len(erg)):
            print(erg[i])
            value.append(erg[i]["value"])
            value1.append(erg[i]["value"])
            index.append(erg[i]["name"])
        print(value)
        print(index)
        value = list(map(int, value))
        value1 = list(map(int, value1))
        for i in range(len(value) - 1):  # 外循环控制遍历次数，这里取列表长度-1，因为有一个数字需要拿出来比较，循环多少次，久比较多少次
            for j in range(
                    len(
                        value) - 1 - i):  # 内循环控制第i个数字跟后面的所有数字比较的次数，这里减i是因为比较完一个数字就要拿下一个数字，前面是比较好的数字，不需要比较，所以外循环比较完完毕一次就少一个
                if value[j] < value[j + 1]:  # 判断判断数是否小于下一个数（被判断数），如果小于，那么交换双方的位置
                    value[j], value[j + 1] = value[j + 1], value[j]
            print(value)
        for p in range(6):
            aaaa.append(value[p])
        print("aaaa", aaaa)

        count3 = 0
        for m in value1:
            print("m", m)
            for f in aaaa:
                if m == f:
                    print("%s感染%d" % (index[count3], m))
                    list1.append(index[count3])
                    list2.append(m)
            count3 += 1
        dict3["area"] = list1
        dict3["died"] = list2
        print(dict3)
        obj = open("../beautifulsoup/json/worldTop6.json", "w")
        json.dump(dict3, obj, indent=5)
        obj.close()


def SevenContinents():
    list1 = []
    list2 = []
    dict1 = {}
    with open("../beautifulsoup/json/thewholeworld.json", "r",
              encoding="utf-8") as dictObj:  # 使用open（）方法读取外部json文件，且用as重命名为dictObj
        erg = json.load(dictObj)
        print(erg)
        for i in range(len(erg["globalList"])-2):
            print(erg["globalList"][i])
            print(erg["globalList"][i]["confirmed"])
            list1.append(erg["globalList"][i]["confirmed"])
            list2.append(erg["globalList"][i]["area"])
    dict1["area"] = list2
    dict1["died"] = list1
    print(dict1)
    obj = open("../beautifulsoup/json/sevenContinents.json", "w")
    json.dump(dict1, obj, indent=5)
    obj.close()

if __name__ == "__main__":
    # select_died_topFive()
    # select_died()
    # select_dangerousAreas()
    # select_China_all()
    theWholeWorld_analyse()
    # all_China_City()
    # ergodicArea()
    # worldTop()
    # # Global_died_data()
    # # getHeatMapData()
    # SevenContinents()
