import math
#primality test that uses trial division and abuses the fact that
#primes have the form 6k +/- i where i (-1,4)
#definately not the fastes, but it's deterministic
def is_prime(n):
  if n <= 3:
    if n <= 1:
      return False
    return True

  #check div by two or div by 3
  if n % 2 == 0 or n % 3 == 0:
    return False

  #check all 6k +/- 1
  for x in range(5, int(math.sqrt(n) + 1), 6):
    if n % x == 0 or n % (x + 2) == 0:
      return False
  return True

#start counting prime numbers until N is found
counter = 1;
x = 3
while True:
  if is_prime(x):
    counter += 1
    if counter == 10001:
      print x
      exit()
  x += 2
