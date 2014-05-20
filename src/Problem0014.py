def collatz_series(n):
  current = n
  while current != 1:
    if current % 2 == 0:
      current = current / 2
    else:
      current = 3 * current + 1
    yield current

max_len = 0
max_number = 0

for n in range(1, 10000000):
  l = len([x for x in collatz_series(n)])
  if l > max_len:
    max_len = l
    max_number = n

print max_number
