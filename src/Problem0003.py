import math

#works for small problemsm, not bigger
def trial_devide_prime_factors(n):
  #do the case for 2s
  while n % 2 == 0:
    print 2
    n /= 2

  #do the rest of the numbers
  for i in range(3, int(math.sqrt(n)), 2):
    while n % i == 0:
      print i
      n /= i

  #remainder is a prime greater than 2
  if n > 2:
    print n

trial_devide_prime_factors(600851475143)
