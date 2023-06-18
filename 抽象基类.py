# 抽象基类作用：1.判断类型 2.对于类中方法的限制


class Company:
    def __init__(self,employlist):
        self.employee = employlist

    def __len__(self):
        return len(self.employee) 
  
com = Company(['zhouhou', 'wangwu'])
# 要求程序员中在这个类中实现了__len__
# print(hasattr(com,'__len__'))

# 类型判断
from collections.abc import Sized
# print(isinstance(com,Sized))


# 抽象基类不能实例化
# 如果继承了抽象基类，必须实现其中的内部方法
# s = Sized()

# class Test(Sized):
#     def __len__(self):
#         pass

# t = Test()


# print(type(com))


import abc
class CacheBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self,key):
        pass
    
    @abc.abstractmethod
    def set(self,key,value):
        pass


class RedisCache(CacheBase):
    def get(self, key):
        pass
    def set(self,key,value):
        pass

r = RedisCache()

