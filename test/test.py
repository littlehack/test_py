import requests
from urllib.parse import urlparse
from lxml import etree
import re

"""
1.同级域名下的链接
2.跨域下的链接
3.从js文件中提取到的链接
"""

url = "https://www.sina.com.cn/"

url2 = urlparse(url)
# 获取域名
domain = url2.netloc
# 获取下级目录
path = url2.path


# 获取所有的链接
def getlinks(url):
    s = requests.session()
    html = etree.HTML(s.get(url, verify=False).text)
    result = html.xpath("//@src|//@href")
    return result


def check():
    # 同域名下链接
    data1 = []
    data2 = []
    for i in getlinks(url):
        if domain in i:
            data1.append(i)
        else:
            # 子域名或者非同级链接
            data2.append(i)
    return data2


print(check())
