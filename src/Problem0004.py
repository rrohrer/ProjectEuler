def is_number_palindrome(n):
  s = str(n)
  x = int(s[::-1])
  return x == n

pal_list = []
for x in range(999,99, -1):
  for y in range(999, 99, -1):
    if is_number_palindrome(x * y):
      pal_list.append(x*y)

print max(pal_list)
