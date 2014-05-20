def generate_n_triangle_num(n):
  return (n * (n + 1)) / 2

def count_divisors(n):
  root = int(n ** 0.5)
  return len(filter(lambda x: n % x == 0, (range(1, root)))) * 2

n = 0
while True:
  n += 1
  div_count = count_divisors(generate_n_triangle_num(n))

  if div_count >= 500:
    break

print generate_n_triangle_num(n)
