# -*- coding:utf8 -*-
import re

# 1 读文件
def read_file(file_path, file_name, method="rb"):
    with open(file_path + file_name, method) as fs:
        html = "".join(fs.readlines())
    return html


# 2 数据预处理
def data_process(html):
    title_rule = '<.*?text-decoration:none">(.*?)</ a>'
    time_rule = 'judgedate="(.*?)"><div class="label">'
    titles = data_parser(re.compile(title_rule, re.S).findall(html), tp="title")
    times = data_parser(re.compile(time_rule, re.S).findall(html), tp="time")
    # 组装
    return [(titles[i], times[i]) for i in range(len(times))]

def data_parser(results, tp="title"):
    if tp == "title":
        return [item.decode("utf8") for item in results]
    if tp == "times":
        return results

def show(results):
    for result in results:
        print result

# 3 展示

if __name__ == "__main__":
    html = read_file("../data/wenshu/", "data.html")
    results = data_process(html)
    show(results)