module PEPrimes where

intSqrt :: Int -> Int
intSqrt = floor . sqrt . fromIntegral

prime :: Int -> Bool
prime 2 = True
prime x = if even x then False else computePrime 3
    where
        computePrime p | p <= intSqrt x = if rem x p == 0 then False else computePrime (p+2)
        computePrime _ = True

factorize :: Int -> [Int]
factorize x = doFactorize x 2
    where
        doFactorize 1 _ = []
        doFactorize y s | prime s && rem y s == 0 = s : doFactorize (div y s) s
        doFactorize y s = doFactorize y (s+1)