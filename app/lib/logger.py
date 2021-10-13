#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import logging
from logging.handlers import RotatingFileHandler
import os
import time
from flask import Flask
# from .. main import app

app_init = Flask(__name__)
LEVEL = 'INFO'

logger = logging.getLogger('logger')
# logger = app.logger

log_path = os.path.join(os.getcwd(), 'logs')
if not os.path.exists(log_path):
    os.mkdir(log_path)
log_file = os.path.join(log_path, 'system-%s.log') % str(time.strftime("%Y-%m-%d"))
logging_format = logging.Formatter(
    '%(levelname)s [%(asctime)s][%(module)s.py - line:%(lineno)d] %(message)s')

console_handler = logging.StreamHandler()
console_handler.setFormatter(logging_format)

file_handler = RotatingFileHandler(
    log_file,
    # maxBytes=2*1024*1024,
    # backupCount=20,
    encoding='UTF-8'
)
# file_handler = logging.FileHandler(log_file, encoding='UTF-8')
file_handler.setFormatter(logging_format)

logger.addHandler(console_handler)
logger.addHandler(file_handler)
logger.setLevel(LEVEL)


