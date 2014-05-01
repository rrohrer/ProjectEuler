#multiples of 3 and 5
#sum all multiples of 3 and 5 below 1000
total = 0

for x in range(3, 1000):
  if x % 3 == 0 or x % 5 == 0:
    total += x

print total
