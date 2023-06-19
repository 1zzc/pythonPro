class A:
    # 类变量
    b = 1
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
t = A(2,3)
# 实例对象访问实例变量和类变量
print(t.b,t.x,t.y)


# 类访问类属性
print('类访问类属性:',A.b)

# 会报错
# print(A.x)

A.b = 98765
print(t.b,A.b)


# t.b = 998

# print(t.b,A.b)