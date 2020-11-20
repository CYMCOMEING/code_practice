import random
 
# 生成16位字符串
def random_str():
  seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  sa = []
  for i in range(16):
    sa.append(random.choice(seed))
  salt = "".join(sa)
  print(salt)
  return salt
 
# 去除重复激活码
def Removal():
  for i in range(200):
    for j in range(i+1,200):
      if L[i] == L[j]:
        print("重复的激活码：", L[i])
        L[i] = '-1'
 
 
if __name__ =="__main__":
  L = []
  for i in range(200):
    L.append(random_str()) #生成两百个激活码
  L[0] = L[1] #校验L[0]=L[1]时，是否删除重复
  Removal()
  i = 0
  while i < len(L):
    if L[i] == '-1':
      print("删除重复元素", L[i])
      L.remove(L[i])
      i -= 1
    else:
      i +=1
