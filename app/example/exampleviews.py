#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@Author  : JUNE
@Time    : 2021-06-02 16:21
@describe:

"""
from flask import make_response, jsonify, Blueprint, abort
import json
from flask import request
from flask import Flask

from .. lib.logger import logger
from .. lib.tojson import AlchemyEncoder
from .services.testdata import TestData


example = Blueprint('example', __name__, url_prefix='/example')
app = Flask(__name__, instance_relative_config=True)


@example.route('/getaddress', methods=['POST', 'GET'])
def get_address():
    try:
        params = request.get_data()
        logger.info(params.decode('utf-8'))
        info = TestData()
        results = info.get_address()
        response = make_response(json.dumps({'code': 0, 'data': results}))
        return response
    except Exception as e:
        logger.error(e)
        logger.error('发生了错误，error: {}'.format(e))
        abort(500)


@example.route('/getjob', methods=['POST', 'GET'])
def get_job():
    try:
        params = request.get_data()
        logger.info(params.decode('utf-8'))
        info = TestData()
        results = info.get_job()
        response = make_response(json.dumps({'code': 0, 'data': results}))
        return response
    except Exception as e:
        logger.error(e)
        logger.error('发生了错误，error: {}'.format(e))
        abort(500)


@example.route('/getfreeemail', methods=['POST', 'GET'])
def get_free_email():
    try:
        params = request.get_data()
        logger.info(params.decode('utf-8'))
        info = TestData()
        results = info.get_free_email()
        response = make_response(json.dumps({'code': 0, 'data': results}, cls=AlchemyEncoder))
        return response
    except Exception as e:
        logger.error(e)
        logger.error('发生了错误，error: {}'.format(e))
        abort(500)


@example.route('/getphonenumber', methods=['POST', 'GET'])
def get_phone_number():
    try:
        params = request.get_data()
        logger.info(params.decode('utf-8'))
        info = TestData()
        results = info.get_phone_number()
        response = make_response(json.dumps({'code': 0, 'data': results}, cls=AlchemyEncoder))
        return response
    except Exception as e:
        logger.error(e)
        logger.error('发生了错误，error: {}'.format(e))
        abort(500)


@example.route('/getnamemale', methods=['POST', 'GET'])
def get_name_male():
    try:
        params = request.get_data()
        logger.info(params.decode('utf-8'))
        info = TestData()
        results = info.get_name_male()
        response = make_response(json.dumps({'code': 0, 'data': results}, cls=AlchemyEncoder))
        return response
    except Exception as e:
        logger.error(e)
        logger.error('发生了错误，error: {}'.format(e))
        abort(500)


@example.route('/getprofile', methods=['POST', 'GET'])
def get_profile():
    try:
        params = request.get_data()
        logger.info(params.decode('utf-8'))
        info = TestData()
        results = info.get_profile()
        response = make_response(json.dumps({'code': 0, 'data': results}, cls=AlchemyEncoder))
        return response
    except Exception as e:
        logger.error(e)
        logger.error('发生了错误，error: {}'.format(e))
        abort(500)


