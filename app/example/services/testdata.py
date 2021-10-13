#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@Author  : JUNE
@Time    : 2021-06-02 16:23
@describe:

"""

from faker import Faker
import json


class TestData(object):
    def __init__(self):
        self.fake = Faker(locale='zh_CN')

    def get_address(self):
        """
        模拟生成地址
        :return:
        """
        return self.fake.address()

    def get_job(self):
        """
        模拟生成工作
        :return:
        """
        return self.fake.job()

    def get_free_email(self):
        """
        模拟生成邮箱
        :return:
        """
        return self.fake.free_email()

    def get_phone_number(self):
        """
        模拟生成手机号
        :return:
        """
        return self.fake.phone_number()

    def get_name_male(self):
        """
        模拟生成姓名
        :return:
        """
        return self.fake.name_male()

    def get_profile(self):
        """
        模拟生成完整资料
        :return:
        """
        return {
            "name": self.fake.name_male(),
            "phone": self.fake.phone_number(),
            "mail": self.fake.free_email(),
            "job": self.fake.job(),
            "address": self.fake.address()
        }
