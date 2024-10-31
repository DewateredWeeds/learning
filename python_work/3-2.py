from itertools import count
from operator import index


s = input("给定一个字符串:")
print("第一个字符:",s[0])
print("前三个字符:",s[0:3])
print("后三个字符:",s[-3:-1]) #waitting for modding
print("字符串的总长度:",len(s))
print("字符'o'在字符串中第一个位置的索引值:",s.index("o"))
print("字符'o'出现的总次数:",s.count('o'))
