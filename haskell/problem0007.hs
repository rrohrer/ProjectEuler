import PEPrimes

primesList = [x | x <- [2..], prime x]

problem7 = last $ take 10001 primesList