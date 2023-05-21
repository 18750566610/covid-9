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
a = 1


def insert(province, province_curedCount, province_suspectedCount, province_deadCount, province_confirmedCount, city,
           city_confirmedCount, city_suspectedCount, city_curedCount, city_deadCount, update_time):
    sql1 = f'''
        insert into test("update_time:数据最后更新时间","province:省","city:市","confirm:累计确诊","confirm_add:新增确诊",
        "confirm_now:现有确诊","heal:累计治愈","dead:累计死亡") values({province},{update_time},{province_confirmedCount},{province_suspectedCount},{province_deadCount},{province_curedCount},{city},{city_confirmedCount},{city_suspectedCount},{city_deadCount},{city_curedCount}) 
    '''


if __name__ == "__main__":
    insert(a, a, a, a, a, a, a, a)
