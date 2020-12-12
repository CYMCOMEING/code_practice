
#pip install xpinyin -i http://pypi.douban.com/simple --trusted-host pypi.douban.com

from xpinyin import Pinyin
p = Pinyin()
result1 = p.get_pinyin('张无忌')
print(result1)

#带音调
result2 = p.get_pinyin('张无忌', tone_marks='marks')
print(result2)

#去掉-
s = result1.split('-')
result3 = s[0].capitalize() + ' ' + ''.join(s[1:]).capitalize()
print(result3)