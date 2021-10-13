#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@Author  : JUNE
@Time    : 2018/1/5 15:06

"""


# from lib.logger import AppLogger
from flask_environments import Environments


class InitApp(object):
    def __init__(self, app):
        self.app = app

    def init_all(self):
        self.init_config()

    def init_config(self):
        env = Environments(self.app)
        env.from_object('config')
        # env.from_pyfile('config.py')







