#create a class pets from class animal and further create class Dog from pets.add
#method bark to class Dog

class Animal:
     pass
class Pets(Animal):
     pass
class Dog(Pets):
    def bark(self):
        print("bhao bhao")

obj3 = Dog()
print(obj3.bark())