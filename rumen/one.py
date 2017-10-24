# -*- coding: utf-8 -*-
# a = 1
# b = 2
# c = 3
# print "%s %s %s" %(a,b,c)
# print '%(x)s %(z)s %(v)s' %({'x':b,'z':a,'v':c})

# print "#".join([a,b,c])

# print "{2} {1} {0}".format(a,b,c)
# print "{n1} {n2} {n3}".format(n1=a,n2=b,n3=c)

# ls = [1,2,3,4]
# ls.append(5)
# print ls

# 求字符串长度 len()
# a = 'hello python'
# print a[-2]

# 切片
# a = [0,1,2,3,4,5,6,7,8,9,10]
# print a [:2]
# print a [2:4]
# print a [:] # 获取所有
# print a [::2] # 步长 没间隔多少输出值
# print a [:-5] # 输出从0开始到倒数第5个的值
# print a [-5:] # 输出从后面起到倒数第5个的所有值


# 字符串操作方法
# s = '123'
s = 'hello world'
# print s.capitalize() # 字符串首字母转换成大写
# print s.count('l')   # 返回选定字符串出现的次数
# print s.endswith('o')# 字符串是否以o为结尾
# print s.startswith('o') # 字符串是否以o为开头
# print s.find('r') # 返回字符串中出现r从左边数起只获取第一个的索引值
# print s.rfind('r') #从右边起只获取第一个出现r的索引值
# print s.index('l') # 返回从左边起第一个出现l的索引值
# print s.isalpha() # 判断字符串是否全为字母的（空格不算字母）
# print s.isdigit()  # 判断字符串是否全为数字的（空格不算字母）
print s.islower()
