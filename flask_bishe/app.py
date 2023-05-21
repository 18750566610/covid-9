from flask import Flask, render_template, jsonify

import utils

app = Flask(__name__)  # 创建flask实例，这个实例的名字叫做app


# 主页面
@app.route('/')  # 装饰器指定路由，路由名叫做 “ / ”，也就是说，指定网络的资源路径地址，通过这个地址就能访问对应的页面
def hello_world():  # 定义一个hello_world函数
    # 使用request获取请求参数，？后面的都是参数
    return render_template("yezi.html")


# 地图页面
@app.route('/login_in')
def login():
    return render_template("login.html")


# 全球疫情信息
@app.route('/theWholeWorld')
def world():
    return render_template("theWholeWorld.html")


# 详情页面
@app.route('/table')
def table():
    return render_template("index.html")

@app.route("/c2")
def get_c2_data():
    res = []
    for tup in utils.get_c2_data():
        # [{'name': '上海', 'value': 318}, {'name': '云南', 'value': 162}]
        res.append({"name": tup[0], "value": int(tup[1])})
    return jsonify({"data": res})


@app.route("/l1")
def get_l1_data():
    data = utils.get_l1_data()
    day, confirm_add, suspect_add = [], [], []
    for a, b, c in data:
        day.append(a.strftime("%m-%d"))  # a是datatime类型
        confirm_add.append(b)
        suspect_add.append(c)
    return jsonify({"day": day, "confirm_add": confirm_add, "suspect_add": suspect_add})


@app.route("/l2")
def get_l2_data():
    data = utils.get_l2_data()
    # end_update_time, province, city, county, address, type
    details = []
    risk = []
    end_update_time = data[0][0]
    for a, b, c, d, e, f in data:
        risk.append(f)
        details.append(f"{b}\t{c}\t{d}\t{e}")
    return jsonify({"update_time": end_update_tmime, "details": details, "risk": risk})


@app.route("/r1")
def get_r1_data():
    data = utils.get_r1_data()
    city = []
    confirm = []
    for k, v in data:
        city.append(k)
        confirm.append(int(v))
    return jsonify({"city": city, "confirm": confirm})


if __name__ == '__main__':  # main方法中调用run（）函数，这样就能对外提供web服务
    app.run()
