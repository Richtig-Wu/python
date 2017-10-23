#conding=utf-8

import keyword

print keyword.kwlist

#id相同代表同一个对象有两个名字
a = 12345
b = a
print id(a)
print id(b)

#python的数据类型
int str list set dict tuple

# 序列通用操作
# 索引
# 切片
# 序列相加
# 重复
# 检查成员
# 长度/最大值/最小值

#str字符串
'' , "" , """ """

a = 'hello python'
 print len(a)
