phone_book = {}
phone_book["John"] = 123243435
phone_book["Jack"] = 343243242
phone_book["Jill"] = 4234324345

for name, phone in phone_book.items():
    print("Phone number of %s is %d" %(name, phone))

# Removing a value
del phone_book["Jack"]
# or
phone_book.pop("Jack")