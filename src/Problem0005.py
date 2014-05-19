import fractions
def lcm(x, y):
  return (x*y) / fractions.gcd(x,y)

print reduce(lcm, list(range(1,20)))
