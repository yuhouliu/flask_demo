# -*-coding: utf-8-*-

# make_response 返回json数据给前端
# jsonify 直接返回json数据
from flask import Flask, make_response, json, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False   # 将json默认ascii码形式关掉

@app.route('/index')
def index():
    data = {
        'name':"张三"
    }
    # response = make_response(json.dumps(data, ensure_ascii=False))  # json.dumps 将字典转换成json字符串
    # response.mimetype = 'application/json'  # 格式修改， text/html -> application/json
    # return response
    return jsonify(data)



if __name__ == '__main__':
    app.run()