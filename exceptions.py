#the try block will generate an error because x is not defined
try:
  print(x)
except:
 print("Something went wrong")

#the else block is executed since there is no error in the try block

try:
 print("hello world")
except:
 print("Something went wrong"),
else:
 print("nothing went wrong")

#the finally block gets executed irregardles there is an error or not
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")