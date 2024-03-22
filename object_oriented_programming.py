
class student:
    student_name=""
    student_age=0
    student_marks=0
    student_age=0

    def __init__(self):#first function in this case is a constructor
        print("constructor called")

    def set_student_name(self,name):#second function takes the parameter name and sets it to the property student name
        self.student_name=name


    def display_student_name(self):#third function displays the student name
     print("Student Name:",self.student_name)


    def set_student_age(self,age):
     self.student_age=age

    def display_student_age(self):
        print("Student age:",self.student_age,self.student_name)

    def set_student_name(self,name):
      self.student_name=name




student1=student()
student1.set_student_name("nathan")
student1.display_student_name()

student1.set_student_age("20")
student1.display_student_age()