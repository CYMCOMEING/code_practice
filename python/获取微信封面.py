import requests
from bs4 import BeautifulSoup
import re


def WxHeadPic(url):
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
    html = requests.get(url, headers=headers)
    pattern = re.compile('var msg_cdn_url = "(.*)"')
    return pattern.findall(html.text)

if __name__ == "__main__":
    print(WxHeadPic('https://mp.weixin.qq.com/s?__biz=MzA3ODg3OTk4OA==&mid=2651112911&idx=1&sn=dc230518a1efc6b77f69d2154a450596&chksm=844c6854b33be1428fc4928b520c68bc5999f23c0b0b357f14b4fe5b7e63e0ca087de818b610&mpshare=1&scene=23&srcid=0121IAKdFs0ZkrkRSfKNUc1u&sharer_sharetime=1611194973383&sharer_shareid=f9c8b5cead88a183a7ef43f8d3854e9a#rd'))