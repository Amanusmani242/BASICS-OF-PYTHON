#add a static method to greet the user hello.

class Hello:
    @staticmethod
    def greet():
      print("hello")

obj = Hello()
print(obj.greet())
