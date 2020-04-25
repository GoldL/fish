# -*- coding: utf-8 -*-
# @Time    : 2020/4/26 上午12:16
# @Author  : iGolden
# @Software: PyCharm
from enum import Enum


class PendingStatus(Enum):
    Waiting = 1
    Success = 2
    Reject = 3
    Redraw = 4
