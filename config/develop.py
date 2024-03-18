# !/usr/bin/env python
# encoding: utf-8

"""
@author: kylegao
@contact: kylegao000@gmail.com
@site: 
@software: PyCharm
@file: develop.py
@time: 18/03/2024 13:00
"""


class DevelopConfig(object):
    ##
    # Flask Config
    ##
    MODE = "develop"
    HOST = '0.0.0.0'
    PORT = 5000
    DEBUG = False

    ##
    # DataBase Config
    ##
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1qaz2wsx@127.0.0.1:3306/movie'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_POOL_SIZE = 300