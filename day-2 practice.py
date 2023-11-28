""""
class Student:
    def __init__(self,name ,age ,marks):
        
        self.name = name
        self.age = age
        self.marks = marks




st1= Student('ankit',22 ,95)

st2= Student('Bimant',27,90)

print (st1.name)
print(st1.age)
print(st1.marks)

print (st2.name)
print(st2.age)
print(st2.marks)

"""

class StudentMarks:

    def set_marks(self,M_marks ,S_marks):
        self.M_marks = M_marks
        self.S_marks = S_marks

    def get_totalmarks (self):
        tot = self.M_marks+self.S_marks
        return tot

st1 = StudentMarks()
st1.set_marks(90,95)
print (st1.get_totalmarks())



