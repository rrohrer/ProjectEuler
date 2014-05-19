x = 20
while True:
  found = True
  for y in range(1, 21):
    if x % y != 0:
      found = False
      break;
  if found:
    print x
    break;
  x += 1
