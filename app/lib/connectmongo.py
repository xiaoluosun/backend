#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@Author  : JUNE
@Time    : 2018/1/5 16:02
@describe:

"""

from flask import Flask
from flask_mongoengine import MongoEngine
from .. main import app

app_init = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host': app.config['MONGODB_IP'],
    'port': app.config['MONGODB_PORT'],
    'db': 'db',
    'username': 'user',
    'password': app.config['MONGODB_PASSWORD'],
    'authentication_source': 'admin',
    'alias': 'db'
}

db = MongoEngine(app)
