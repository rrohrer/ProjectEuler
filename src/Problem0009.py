
#n > m
def gen_triple(n, m):
  return [n * n - m * m, 2 * n * m, n * n + m * m]

for n in range(2, 1000):
  for m in range(1, n):
    triple = gen_triple(n, m)
    if sum(triple) == 1000:
      print reduce(lambda x, y: x*y, triple)
