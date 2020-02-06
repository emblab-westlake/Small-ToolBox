# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 11:29:06 2020

@author: zhangguoqing

E-mail: zhangguoqing84@westlake.edu.cn


"""

def normalizition(data):
    min_value = data.min()
    max_value = data.max()
    ranges = max_value - min_value
    norm_data = zeros(shape(data))
    m = data.shape[]
    norm_data = data - tile(min_value, (m, 1))
    norm_data = norm_data/tile(ranges, (m, 1))
    return norm_data, ranges, min_value
       
