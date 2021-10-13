#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@Author  : JUNE
@Time    : 2018/1/5 14:12

"""


from flask_script import Manager, Server
from flask_script.commands import ShowUrls, Clean
from app.main import app

manager = Manager(app)

manager.add_command('clean', Clean())
manager.add_command('url', ShowUrls())
manager.add_command('server', Server(host=app.config.get('HOST', '127.0.0.1'),
                                     port=app.config.get('PORT', 5000),
                                     threaded=True))

if __name__ == '__main__':
    manager.run()

