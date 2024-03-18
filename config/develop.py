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
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://movie:xWRPYsWrXEKHmdTj@154.9.207.208:3306/movie'
    #
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1qaz2wsx@154.9.207.208:3308/movie'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_POOL_SIZE = 300
