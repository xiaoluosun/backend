#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@Author  : JUNE
@Time    : 2018/8/8 14:50
@describe:

"""
from ..main import app
from apscheduler.jobstores.mongodb import MongoDBJobStore


class SchedulerConfig(object):
    JOBS = [
        # {
        #     'id': 'track_check',
        #     'replace_existing': True,
        #     'func': track_check,
        #     'trigger': {
        #         'type': 'cron',
        #         'hour': '20'
        #     }
        # }
    ]

    SCHEDULER_JOBSTORES = {
        'default': MongoDBJobStore(host=app.config['MONGODB_IP'], port=27017, database='testcenter')
    }
    SCHEDULER_EXECUTORS = {
        'default': {'type': 'threadpool', 'max_workers': 100}
    }
    SCHEDULER_JOB_DEFAULTS = {
        # 是否执行积攒的任务，只执行一次
        'coalesce': True,

        # 同时执行的实例数
        'max_instances': 300,

        # 任务超时容错
        'misfire_grace_time': 60
    }

    SCHEDULER_API_ENABLED = True
