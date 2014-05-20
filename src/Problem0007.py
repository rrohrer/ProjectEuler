from prime_utils import is_prime

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
