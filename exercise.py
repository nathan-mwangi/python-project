#how to find the largest number in a list
numbers=[2,34,57,78,55,994,43,9]
print("the largest number is",max(numbers))

#getting repeated elements in a list
list2=["cheese","tomato","potato","tomato","ram","ram"]
repeated_veg=set()
non_repeated_veg=set()
for item in list2:
    if list2.count  (item)>1:
        repeated_veg.add(item)
        print("my repeated items are",repeated_veg)
    else:
        non_repeated_veg.add(item)
print("the non_repeated items are",non_repeated_veg)



#dictionaries
mydict={"brand":"Ford","model":"mustang","year":2016}
print("my old dictionary is",mydict)
delete_keys=["brand","model",]


for key in delete_keys:
    del mydict[key]
print("my new dictionary is",mydict)















# how to add items in a tuple
my_fruits=('banana','apples','oranges','grapes','tomatoes')
print(my_fruits)
my_fruits=list(my_fruits)
print(my_fruits)
my_fruits.append('peaches')
print(my_fruits)
my_fruits=tuple(my_fruits)
print(my_fruits)



#how to delete a list of keys from  a dictionary

thisdict={
    "person":"king`ori",
    "contact":"012384784",
    "email":"king`ori@gmail.com",
}

thisdict.pop("email")
print(thisdict)

thisdict={
    "person":"king`ori",
    "contact":"012384784",
    "email":"king`ori@gmail"
}

x=thisdict.values()
print(x)

