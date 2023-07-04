a_string = "Hello world!"
print(len(a_string))  # prints 12

print(a_string.count("l"))  # prints 3

print(a_string[3:7])  # prints "lo w" (prints from index 3 to 6)


print(a_string[3:7:2])  # prints "l " (prints from index 3 to 6, step 2)

print(a_string[::-1]) # prints "!dlrow olleh" (prints from last to first)

print(a_string.lower())  # prints "hello world!"

print(a_string.upper())  # prints "HELLO WORLD!"


print(a_string.startswith("Hello"))  # prints True
print(a_string.endswith("random"))  # prints False


print(a_string.split(" "))  # prints ["Hello", "world!"]