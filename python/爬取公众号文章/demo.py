import wechatsogou

"""
Werkzeug最新版本没有contrib
pip install Werkzeug==0.14.1

"""

# 如 设置超时
ws_api = wechatsogou.WechatSogouAPI(timeout=1)

# 获取特定公众号信息
#print(ws_api.get_gzh_info('CSDN'))

# 搜索公众号
#print(*ws_api.search_gzh('python'))

# 搜索微信文章
#print(*ws_api.search_article('编程'))

# 解析最近文章页
# print(ws_api.get_gzh_article_by_history('CSDN'))

# 解析 首页热门 页
from wechatsogou import WechatSogouAPI, WechatSogouConst
#print(ws_api.get_gzh_article_by_hot(WechatSogouConst.hot_index.food))

# 获取关键字联想词
print(ws_api.get_sugg('python'))



