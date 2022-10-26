#write a class Complex to represent Complex numbers, along with obverload operators + and *
# adds and multiply them.

class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

   # def __mul__(self, other):
    #    return self.a * other.b

cmp1 = Complex(1,4)
cmp2 = Complex(11,3)
c3 = cmp1+cmp2
print(c3.a + c3.b)