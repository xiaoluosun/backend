#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@Author  : JUNE
@Time    : 2018/1/5 16:02
@describe: 

"""

# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import scoped_session, sessionmaker
# from sqlalchemy.pool import NullPool
#

#
# # 创建数据库引擎
# engine = create_engine(configs[APP_ENV].DB_URI, convert_unicode=True, isolation_level="READ UNCOMMITTED", poolclass=NullPool)
#
# db_session = scoped_session(sessionmaker(autocommit=False,
#                                          autoflush=False,
#                                          bind=engine))
#
# # 所有的类都要继承自`declarative_base`这个函数生成的基类
# Base = declarative_base()
# Base.query = db_session.query_property()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from .. config import APP_ENV, configs
import os
from .. main import app
from .. lib.logger import logger

app_init = Flask(__name__)
app_init.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = configs[APP_ENV].DB_URI
app_init.config['SQLALCHEMY_DATABASE_URI'] = app.config['DB_URI']
app_init.config['SQLALCHEMY_POOL_SIZE'] = 100
db = SQLAlchemy(app_init)
