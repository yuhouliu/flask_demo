# -*-coding: utf-8-*-

from flask import Flask
from werkzeug.routing import BaseConverter   # 自定义转换器的父类


app = Flask(__name__)

# 自定义转换器类
class RegexConverter(BaseConverter):
    '''自定义转换器类'''
    def __init__(self, url_map, regex):
        super(RegexConverter, self).__init__(url_map)   # 调用父类的初始化方法
        self.regex = regex

    def to_python(self, value):
        # 父类的方法 功能已经实现好了
        print('to_python方法被调用')
        return value


@app.route('/hello', methods=['GET', 'POST'], endpoint='hello')   # methods请求的类型
def helloworld():
    return '<h1>hello world<h1>'


@app.route('/hi', endpoint='hi')
def hi():
    return '<h1>Hi boy<h1>'


# 变量规则:
#变量转换器 string、int、float、path
# string 接收任何不包含斜杠的文本
# int 接收正整数
# float 接收正浮点型
# path 接收包含斜杠的文本
@app.route('/index/<string:id>')     # <>用于向前端url传递参数，
def index(id):
    if id == '1':
        return 'python'
    if id == '2':
        return 'django'
    if id == '3':
        return 'flask'
    return 'no match'


# 将自定义转换器添加到flask应用中
app.url_map.converters['re'] = RegexConverter    # {'re': RegexConverter}


# 自定义转换器
@app.route('/index2/<re("\d\d"):value>')    # <re("\d\d")> re是自定义转换器括号里面是匹配的内容
def index2(value):
    print(value)
    return '自定义转换器'


if __name__ == '__main__':
    app.run()