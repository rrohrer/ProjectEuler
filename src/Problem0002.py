#add the even values less than 4 million of the fib sequence

current = 1
previous = 0
total = 0

while current <= 4000000:
  if current % 2 == 0:
    total += current;
  temp = current
  current = current + previous
  previous = temp

print total
