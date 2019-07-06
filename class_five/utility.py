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
            interval = random.uniform(1, 10)
            try:
                response = requests.get(url, headers={'Connection': 'close'}, timeout=timeout)
                if response.status_code == 200:
                # 200 代表 HTTP 请求被正确的响应了
                    return response.text
                retry -= 1
                time.sleep(interval)
            except Exception as e:
            #  Exception可以将所有的异常包括在内；将异常赋予变量e
                time.sleep(interval)
                print ("url:%s, fetch error: %s") % (url, str(e))
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

    def generate_md5(self, key):
        import hashlib
        hm = hashlib.md5()
        hm.update(key)
        return hm.hexdigest()

util_func = Utility()