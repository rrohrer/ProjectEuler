def collatz_series(n):
  current = n
  yield current
  while current != 1:
    if current % 2 == 0:
      current = current / 2
    else:
      current = 3 * current + 1
    yield current

max_len = 0
max_number = 0

cached_lengths = {}

for n in range(1, 1000000):
  l = 0
  for x in collatz_series(n):
    if x in cached_lengths:
      l += cached_lengths[x]
      break
    l += 1

  cached_lengths[n] = l
  if l > max_len:
    max_len = l
    max_number = n

print max_number
