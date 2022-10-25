#create a class programmer for storing information of few programmers in microsoft.
class Programmer:
    def __init__(self,aname , asalary, arole): #constructor
        self.name = aname       # obj.name
        self.salary = asalary   # obj.salary
        self.role = arole       # obj.role
                                #basically self will bi replaced with obj
obj = Programmer("aman",20000,"manager")
print(obj.name)
print(obj.salary)
print(obj.role)