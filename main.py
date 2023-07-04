class MyClass:
  variable = "blah"

  def __init__(self, number):
    self.number = number

  def func(self):
    print("This is a message inside the class.")

my_object = MyClass(100)

print(my_object.variable)
print(my_object.number)
my_object.func()