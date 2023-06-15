
# 魔法方法可以更改实例对象的类型

class Student:
    def __init__(self,student_list):
        self.students = student_list



    # 遇到迭代的需求，先找类里面是否有__iter__(),再找__getitem__()
      # item是索引，从0开始
    def __getitem__(self,item):
        return self.students[item]
    
    def __len__(self):
        return len(self.students)
    

s = Student(['大哥','xiaodi','wangwu'])

print(type(s))
s1 = s[:2]
# 此时遇到了迭代的需求，变成了list
print(type(s1))

print(len(s1))
print(len(s))
for item in s:
    print(item)
        
        