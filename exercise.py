#how to find the largest number in a list
numbers=[2,34,57,78,55,994,43,9]
print("the largest number is",max(numbers))



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

