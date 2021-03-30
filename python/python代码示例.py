

# 字典值获取
# dict8 = {'a':1, 'b':2, 'c':3}
# print(dict8.get('d',0))
# print(dict8['d'])

# 判断字典key是否存在
# dic = {'a':1, "b":2,"c":3}
# print("b" in dic.keys())
# print("d" in dic.keys())

# 获取列表中出现次数最多的元素
# from collections import Counter
# list9 = [1, 2, 3, 4, 2, 3, 2]
# print("方法一===============")
# print(max(list9, key=list9.count))
# print("方法二===============")
# print(Counter(list9).most_common(1))

# 变量类型、地址和内存占用量
# import sys
# var10 = "abcd"
# print("变量类型:", type(var10))
# print("变量地址: ", id(var10))
# print("变量内存占用量:", sys.getsizeof(var10))

# 中文提取
# import re
# str12 = "学python，大家一起来2321学习，—#￥#4"
# pattern = re.compile(u"[\u4e00-\u9fa5]+")  # 中文的正则表达式匹配方式
# result = re.findall(pattern, str12)
# for word in result:
#     print(word)

# 将两个列表合并成字典，或者是直接对两个列表的数值进行操作
# keys = ["a", 'b', 'c']
# values = [1, 2, 3, 4]
# dict16 = dict(zip(keys, values))
# print(dict16)
# for i, j in zip(keys, values):
#     print((i, j))

# 字符串的反转
# 可以采用切片处理，或者利用Python内置的reversed函数来实现
# str17 = "学python"
# print(str17[::-1])
# print(''.join(reversed(str17)))
