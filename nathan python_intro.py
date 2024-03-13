#pyhon comment -single line comment
"""
this is a sample multiline comment in python
"""




#variables
student_name ="Jonathan"#data type is string
student_age=20 #data type is integer
student_fee=100.0 #data type is float
student_marks=100
is_male =True #data type is boolean




#outputting the values in the variables
print(student_name)
print(student_age)
print(is_male)



student_name ="Jonathan"
student_name =("Allan")
print(student_name)




STUDENT_NAME ="Ryan"
student_name ="ben"
print(STUDENT_NAME)

#variable naming in python
book_price=20.0 #valid variable name
_book_price=20.0 #valid variable name
#*book_price=10.0
#123_book_price=0
book_price_123=40


x=y=z=10 #assigning one value to multilple variables
x,y,z=30,40,50 #multiple values different variables
#casting In pytyhon
firstname="nathan"
secondname=252535
lastname=firstname+" "+str(secondname)
print("my lastname is "+lastname)



price=1
qty=8
total=price*qty
myanswer1="the total is:"+str(total)+"kenya shillings"
print(myanswer1)

firstname="nathan"
secondname=("kimani")
thirdname=firstname+" "+str(secondname)
print("my thirdname is "+thirdname)


#logical operator
age=20
nationality=("rwanda")

if nationality=="kenyan" and age>=35:
    print("you can be president")

else:
    print("you are not president")




y=500
x=3

ans=y%x
print(ans)
if ans==0:
    print("y is an even number")
else:
   print("y is an odd number")


   #loops
   #the while loop---testing the break key words in loops
   x=1
   while x<=5:
       if x==3:
           break
       print(x)
       x+=1


i= 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)






