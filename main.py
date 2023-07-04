primes = [2, 3, 5, 7]
for prime in primes:
  print(prime)

for x in range(5):
  print(x)  # prints 0, 1, 2, 3, 4

for x in range(3, 6):
  print(x)  # prints 3, 4, 5

for x in range(3, 8, 2):
  print(x)  # prints 3, 5, 7


# prints 0, 1, 2, 3, 4
count = 0
while count < 5:
  print(count)
  count += 1
else:
  print("count reached value %d" % count)