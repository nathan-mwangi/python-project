#parent class

class Animal:
    def __init__(self):
        pass
    def speak(self):
        print("i am an animal")

    #child class1
class Dog(Animal):
    def __init__(self):
        pass
    def speak(self):
        print("I am a dog and i bark")


# the second child class
class Cat(Animal):

    def __init__(self):
        pass


    def speak(self):
        print("I am a cat and i meow")


# creating instances of the classes

dog1=Dog()
dog1.speak()


cat1=Cat()
cat1.speak()