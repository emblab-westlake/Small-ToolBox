# -*- coding: utf-8 -*-
'''
Author: zhangguoqing
Date: 2020-02-06 11:27:32
LastEditTime: 2021-06-25 22:35:48
'''


def normalizition(data):
    min_value = data.min()
    max_value = data.max()
    ranges = max_value - min_value
    norm_data = zeros(shape(data))
    m = data.shape()
    norm_data = data - tile(min_value, (m, 1))
    norm_data = norm_data/tile(ranges, (m, 1))
    return norm_data, ranges, min_value
       
