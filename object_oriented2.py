class student:
    student_name=''
    student_age=0
    student_marks=0
    def __init__(self,name,age):
        self.student_name=name
        self.student_age=age
        print('constructor called')


    def display_student_details(self):
    print("student:", self.student_name,"age:",self.student_age)




student1=student(name:)