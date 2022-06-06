# -*-coding: utf-8-*-
# 重定向 302

from flask import Flask, redirect, url_for


app = Flask(__name__)


@app.route('/index')
def index():
    return redirect('https://www.baidu.com')


@app.route('/index2')
def index2():
    return redirect(url_for('hello'))  # 通过url_for重定向到下一个函数

@app.route('/hello')
def hello():
    return "url_for 方式重定向"



if __name__ == '__main__':
    app.run()