import os
 
# 使用os.environ获取环境变量字典，environ是在os.py中定义的一个dict environ = {} 
env_dist = os.environ 
 
# 打印所有环境变量，遍历字典
for key in env_dist:
    print(key + ' : ' + env_dist[key])
