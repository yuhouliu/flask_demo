# -*-coding: utf-8-*-
# flask数据库
from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # 数据库

app = Flask(__name__)
app.secret_key = 'Secret Key'

class Config:
    '''配置参数'''
    SQLALCHEMY_DATABASE_URI = 'sqlite:///demo.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

app.config.from_object(Config)

# SQLAlchemy(app)
db = SQLAlchemy(app)


# 创建数据库模型类
class Role(db.Model):
    '''角色表'''
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32),unique=True)

class User(db.Model):
    '''用户表'''
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(128),unique=True)
    password = db.Column(db.String(128))
    role_id = db.Column(db.Integer,db.ForeignKey('role.id'))


if __name__ == '__main__':
    # 清除所有表
    db.drop_all()
    # 创建所有表
    db.create_all()
    # 创建对象，插入数据
    role1 = Role(name= 'admin')
    # session 记录到对象任务中
    db.session.add(role1)
    # 提交任务
    db.session.commit()

    role2 = Role(name= 'admin2')
    db.session.add(role2)
    db.session.commit()

    user1 = User(name='zhangsan', password='123', role_id=role1.id)
    user2 = User(name='lisi', password='321', role_id=role1.id)
    user3 = User(name='wangwu', password='321', role_id=role2.id)
    db.session.add_all([user1,user2,user3])
    db.session.commit()


    # app.run()