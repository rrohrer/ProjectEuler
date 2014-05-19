sum_of_sqares = sum(map(lambda x: x ** 2,list(range(1,101))))
sum_squared = sum(list(range(1,101))) ** 2

print sum_squared - sum_of_sqares
