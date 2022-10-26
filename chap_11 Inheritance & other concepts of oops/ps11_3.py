#create a class Employee and add salary and increament properties to it.
#write a method salaryAfterIncrement method with a @property decorator
# with a setter which changes the value of increament passed on the salary.

class Employee:
    def __init__(self,salary,increament)-> None:
        self.salary = salary
        self.increament = increament

    @property
    def salaryAfterIncreament(self):
        return self.salary * (1 + self.increament)
    @salaryAfterIncreament.setter

    def salaryAfterIncreament(self,value):
        self.salary =  self.salary * (1 + self.increament)



emp1 = Employee(12000,0.1)
print(emp1.salaryAfterIncreament)
emp1.salaryAfterIncreament = 11000
print(emp1.salaryAfterIncreament)