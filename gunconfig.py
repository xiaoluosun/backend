#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@Author  : JUNE
@Time    : 2018/1/5 18:38
@describe:

"""

# !/usr/bin/env python
# coding=utf-8

import os

# 绑定的ip以及端口号
bind = 'localhost:18000'

# 监听队列
backlog = 512

# gunicorn要切换到的目的工作目录
#chdir = '/home/test/server/bin'

# 超时
timeout = 5000

# 使用gevent模式，还可以使用sync 模式，默认的是sync模式
# worker_class = 'gevent'
#
# worker_connections = 2000

# 进程数
workers = 10

# 指定每个进程开启的线程数
threads = 2

# 日志级别，这个日志级别指的是错误日志的级别，而访问日志的级别无法设置
loglevel = 'info'

#设置gunicorn访问日志格式，错误日志无法设置
access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"'

path = os.getcwd()
# 访问日志文件的路径
accesslog = path + "/logs/access.log"

# 错误日志文件的路径
errorlog = path + "/logs/error.log"

