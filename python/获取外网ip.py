import requests
import re

def getIP():
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
    response = requests.get('http://www.baidu.com/s?wd=ip',headers=headers)
    html = response.text
    ret = re.search(r'<span class="c-gap-right">本机IP:&nbsp;(.*?)</span>', html)
    if ret:
        print(ret.group(1))


getIP()
