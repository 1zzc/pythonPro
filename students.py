class Student:
    def __init__(self,student_list):
        self.students = student_list

      # item是索引，从0开始
    def __getitem__(self,item):
        return self.students[item]
    

s = Student(['大哥','xiaodi','wangwu'])




for item in s:
    print(item)
        
        