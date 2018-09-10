# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 09:34:27 2018

@author: Administrator
"""

import json

# json decode: str -> dict
jonsStr = """{"translateResult":[[{"tgt":"你好","src":"hello"}]],"errorCode":0,"type":"en2zh-CHS",
"smartResult":{"entries":["","n. 表示问候，惊奇或唤起注意时的用语","int. 喂；哈罗","n. (Hello)人名；(法)埃洛"],"type":1}}"""
jsonLoads=json.loads(jonsStr)
print(jsonLoads['translateResult'][0][0]['tgt'])

