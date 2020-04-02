# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 上午11:41
# @Author  : iGolden
# @Software: PyCharm
import requests


class HTTP:
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
