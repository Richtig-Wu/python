# -*- coding: utf-8 -*-

# import keyword
#
# print keyword.kwlist

#id相同代表同一个对象有两个名字
#a = 12345
#b = a
#print id(a)
#print id(b)

#python的数据类型
#int str list set dict tuple

# 序列通用操作
# 索引
# 切片
# 序列相加
# 重复
# 检查成员
# 长度/最大值/最小值

#str字符串
# '' , "" , """ """

# a = 'hello python'
# print len(a)


# 循环语句
# while
# continue 跳出当前循环，不会结束
# break 没有break，条件为true会一直进行

# i = 1
# d = []
# while i<10:
#     i += 1
#     if i%2 > 0 :
#         continue
#     d.append(i)
#     print d



#for迭代语句
# a = (1,2,3,4,5,6,7)

# print xrange(10,20)

# print [i for i in range(10)]
#步长
# print range(10,30,2)

#input 语句
# number = input('正确数字是什么\n')
# x = 7
# if int(number) == x:
#     print('yes')
# else:
#     print('no')

# 函数基本语法
# def fun():
    # pass

# 函数的参数
# 必备参数
# 关键字参数
# 默认参数
# 不定参数

# def func1(a,b,c):
#     return a,b,c
# print func1(1,2,3)

# 关键数参数
# def func1(a,b,c):
#     return a,b,c
# print func1(c = 100 ,b = 50 , a = 20)

# 默认参数
# def func1(a = 1 , b = 2 , c = 3):
#     return a,b,c
# print func1(a = 8)

#  不定长参数
# def fun3(*args):
#     s = 0
#     for i in args:
#         s += i
#     return s
# print fun3(1,2,3,4,5,6)

# def fun4(**arg):
#     for i in arg.items():
#         print i
# print fun4(name = 'zhang' , age = 20 , sex = 'boy')

# def fun1(a,b,c = 1 ,*d , **e):
#     print (a,b,c)     #必备和默认参数
#     print d           #元祖
#     print e           #字典
# fun1(1,2,3,4,5,6,7,x=1,y=2,z=3)


# 全局变量和局部变量
# x = 2
# def func1():
#     x = 3
#     x = x+1
#     return x
# print func1()
# print x

# 内嵌函数和闭包
# def fun1():
#     print('fun1')
#     def fun2():
#         print('fun2')
#     fun2()
# print fun1()

# def fun1(x):
#     def fun2(y):
#         return x*y
#     return fun2  #没括号是函数对象
# print fun1(5)(6)

# b = fun1(4)
# print b(6)

# lambda表达式 匿名函数
# def fun(x):
#     return x * x
# print fun(5)

# a = lambda x : x*x
# print a(5)

# filter()过滤器
# print list(filter(None,[1,2,False,True]))

# 过滤能被3整除的数
# print list(filter(lambda x:x%3==0 ,range(10)))

# map 多次调用
# a = lambda x : x*x
# print list(map(a,range(5)))

# 递归 ：
# def fun2(m):
#     if m == 1 or m == 0:
#         return 1
#     else:
#         return fun2(m-1)*m
# print fun2(4)



# def fun1(D,d):
#     if d == 1:
#         return D
#     else:
#         return fun1(D-2,d-1)
# print fun1(20,3)

#斐波拉契数列
# 1,1,2,3,5,8,13...
d = []
def fibs(n):
    if n == 0 or n == 1:
        return 1
    else :
        return fibs(n-1) + fibs(n-2)
# print fibs(10)
for i in range(3):
     d.append(fibs(i))


print d
