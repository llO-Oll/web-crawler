# -*- coding:utf-8 -*-
from utils.configs import APP_ID, API_KEY, SECRET_KEY
from aip import AipNlp


class BaiduModel:
    def __init__(self, maxSummaryLen=300, APP_ID=APP_ID, API_KEY=API_KEY, SECRET_KEY=SECRET_KEY):
        self.maxSummaryLen = maxSummaryLen
        self.APP_ID = APP_ID
        self.API_KEY = API_KEY
        self.SECRET_KEY = SECRET_KEY
        self.client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

    def getSummary(self, text):
        if text == None:
            raise ValueError("text must not be None!")
        return self.client.newsSummary(text, self.maxSummaryLen)

    def load_Txt(self, path, encoding='utf-8'):
        with open(path, 'r', encoding=encoding) as f:
            title = f.readline()
            time = f.readline()
            organization = f.readline()
            text = f.read()
        return title, time, organization, text