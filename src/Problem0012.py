def generate_n_triangle_num(n):
  return sum((range(1, n+1)))

def count_divisors(n):
  return len(filter(lambda x: n % x == 0, (range(1, n + 1))))

n = 0
while True:
  n += 1
  div_count = count_divisors(generate_n_triangle_num(n))
  print div_count
  if div_count >= 500:
    break

print generate_n_triangle_num(n)
