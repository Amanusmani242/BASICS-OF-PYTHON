#write a class Calculator capable of finding square,cube and squareroot of a number.
import math
class Calculator:
    def __init__(self,num):
        self.num = num

    def square(self):
        return self.num * self.num

    def cube(self):
        return self.num * self.num * self.num

    def squareRoot(self):
        return math.sqrt(self.num)

obj = Calculator(2)
print(obj.num)
print(obj.square())
print(obj.cube())
print(obj.squareRoot())