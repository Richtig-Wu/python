# -*- coding: utf-8 -*-

# 类
# class classname(object):
#     pass
#
# class Fruite(object):
#     def __init__(self,name,color,weight):
#         self.name = name
#         self.color = color
#         self.weight = weight
#
# fr = Fruite('aaa','red',90)
# print fr.name
# print fr.color
# print fr.weight

#
# a = '12'
# print isinstance(a,int)
# print help(int)



# 类的属性和实例化属性
# 类名.属性名

# class Fruites(object):
#     kind = 'kind'
#     list1 = []
#     def __init__(self,name,color,weight=90):
#         self.name = name
#         self.color = color
#         self.weight = weight
#         self.list2 = []
#         self.show  = [] #被重新初始化
#     def show(self):
#         print('show show........')
# fr1 = Fruites('aaa','red')
# fr2 = Fruites('bbb','yellow')
# fr1.list1.append('mmmm')
# fr2.list2.append('aaaa')
#
# print fr1.list1

# fr1 = Fruites('banana','yellow')
# print fr1.show()
# print fr1.kind
# print fr1.__dict__ #查看属性
# print fr1.show

#隐藏属性
# class Fruites(object):
#     kind = 'kind'
#     list1 = []
#     def __init__(self,name,color,weight=90):
#         self.name = name
#         self._color = color
#         self.__weight = weight
#
#
# fr1 = Fruites('banana','yellow')
# print fr1._color
# print fr1._Fruites__weight





# 继承
# class Fruites(object):
#     def __init__(self,name,color,weight=90):
#         self.name = name
#         self.color = color
#         self.weight = weight
#         self.list2 = []
#     def show(self):
#         print ('ok')
#
# # 派生类
# class Apple(Fruites):
#     def __init__(self,color, weight = 110):
#         Fruites.__init__(self,'apple',color,weight)
#     def show(self):
#         print ('aaa........')
# a1 = Apple('red')

# print a1.name
# print a1.color
# print a1.weight
# print a1.show # 子类没有调用父类



# class Fruites(object):
#     def __init__(self,name,color,weight=90):
#         self.name = name
#         self.color = color
#         self.weight = weight
#         self.list2 = []
#     def show(self):
#         print ('ok')
#
# # 派生类
# class Orange(Fruites):
#     def __init__(self,color, weight):
#         Fruites.__init__(self,'orange',color,weight)
#
# o1 = Orange('orange1','80')
# print o1.name
# print o1.color
