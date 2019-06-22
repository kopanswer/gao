#  --*-- coding:utf8 --*--
"""
    用途：
        输入： 第三方库
        输出： 通用函数
"""
import random
import time
import requests
from lxml import etree

class Utility(object):
    def __init__(self):
        pass

    def fetch_html(self, url, timeout=20, retry=1000):
        """
        特性
            响应时间：   调整网页的默认最大响应时间为 timeout = 20 秒
            抓取失败：   再次发起抓取，最多重复 retry = 100 次
            伪装爬虫：   两次抓取之间间隔时间随机
        输入
            url         网络地址
            retry=100   最多重复 100 次
            timeout=20  最长响应时间 20 秒
        输出
            若成功抓取 html 文本，返回页面 response
            否最终失败，返回空值 ""
        """
        while retry > 0:
            response = requests.get(url, timeout=timeout)
            if response.status_code == 200:
                return response.text
            retry -= 1
            interval = random.uniform(1, 10)
            time.sleep(interval)
        return ""

    def parse_html(self, html):
        """
        输入
            html:   html 文本
        输出
            dom:    xpath 解析对象
        """
        dom = etree.HTML(html)
        return dom

    def read_tbody(self, tbody, trnumber=15):
        records = []
        for i in range(1,trnumber+1,1):
            print type(tbody)
            print len(tbody)
            import pdb;pdb.set_trace()
            for t in tbody:
                print t
            # tr = tbody.xpath('//tr')[i]
            # records.append(self.read_tr(tr))
        return records

    def read_tr(self, tr):
        record = {}
        record["bureau"] = tr.xpath('//td')[1].xpath('data-form-value')[0]
        record["office"] = tr.xpath('//td')[2].xpath('data-form-value')[0]
        record["jobname"] = tr.xpath('//td')[3].xpath('data-form-value')[0]
        record["jobcode"] = tr.xpath('//td')[4].xpath('data-form-value')[0]
        record["candidates"] = tr.xpath('//td')[5].xpath('data-form-value')[0]
        record["applicants"] = tr.xpath('//td')[6].xpath('data-form-value')[0]
        record["qualifieds"] = tr.xpath('//td')[7].xpath('data-form-value')[0]
        self.show_tr(record)
        return record

    def show_tr(self, tr):
        for k, v in tr.items():
            print k, ":", v



util_func = Utility()