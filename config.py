#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@Author  : JUNE
@Time    : 2018/1/5 14:12
@describe: 默认配置文件

"""

# APP_ENV = "development"
# APP_ENV = "online"


class BaseConfig:
    DEBUG = False


class Development(BaseConfig):
    DEBUG = True
    # mysql
    DB_URI = "mysql://sun:111111@localhost:3306/db?charset=utf8"

    # mongodb
    MONGODB_IP = "127.0.0.1"
    MONGODB_PORT = 7888
    MONGODB_PASSWORD = 'xxxxxx'


class Production(BaseConfig):
    # mysql
    DB_URI = "mysql://sun:111111@localhost:3306/db?charset=utf8"

    # mongodb
    MONGODB_IP = "127.0.0.1"
    MONGODB_PORT = 7888
    MONGODB_PASSWORD = 'xxxxxx'

