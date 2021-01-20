import requests

import json
comments = requests.get('https://mp.weixin.qq.com/s?__biz=MzIyMjg2ODExMA==&mid=2247483972&idx=1&sn=e21bde4f6178f2e609915bee27cdf212&chksm=e827a5a5df502cb346174a767e70c90184a3c6b94c7181300c72928efdf4c5b8bad11d415b26&mpshare=1&scene=23&srcid=&sharer_sharetime=1592640538943&sharer_shareid=f9c8b5cead88a183a7ef43f8d3854e9a#rd')
comments.encoding = 'utf-8'
print(comments.text.strip('var msg_cdn_url='))