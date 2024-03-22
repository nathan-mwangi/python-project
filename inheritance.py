
#the parent class

class person:
    age = ""
    name=""

    def __init__(self,name,age):
        self.name = name
        self.age=age

    def printperson(self):
       print("the details of the person are:",self.age,self.name)

#child class
class student(person):
   uniform=""

   def __init__(self,name,age,uniform):
       super().__init__(name,age)
       self.uniform=uniform
   def printstudent(self):
    print("the details of the student are:",self.uniform,self.name,self.age)


student1=student("John",40,"khaki")
student1.printperson()

student2=student("John",40, "khaki")
student2.printstudent()