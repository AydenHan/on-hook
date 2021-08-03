#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File : Data_Json.py
@Note : 数据处理类
'''

import os,json

class JsonHandle(object):
    def __init__(self):
        pass

    @staticmethod
    def createJson(path):
        data = {
            'plan': [
               {'id':"御魂、觉醒、御灵",
                'node': [
                    'challenge.png',
                    'defeat.png',
                    'victory.png',
                    'award.png'
                ]}
            ]
        }

        with open(path, 'w', encoding='utf-8') as cfg:
            json.dump(data, cfg, indent=2)

    @classmethod
    def getJson(cls, path):
        if not os.path.exists(path):
            cls.createJson(path)
        with open(path, 'r', encoding='utf-8') as cfg:
            info = json.load(cfg)
        return info

    # @staticmethod
    # def alterJson(self, ori_data, new_item):
    #     info = ori_data
    #     info['memo_num'] += 1

    @staticmethod
    def updateJson(path, data):
        with open(path, 'w', encoding='utf-8') as cfg:
            json.dump(data, cfg, indent=2)



