x = 2
print(x == 2) # prints True
print(x == 3) # prints False
print(x < 3)  # prints True


name = "John"
age = 23
if name == "John" and age == 23:
  print("Your name is John, and you're also 23 years old.")

if name == "John" or name == "Rick":
  print("Your name is either John or Rick.")

if name in ["John", "Rick"]:
  print("Your name is either John or Rick.")


x = [1, 2, 3]
y = [1, 2, 3]
print(x == y) # prints True
print(x is y) # prints False  (Unlike ==, "is" compares instances)