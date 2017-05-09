-- find the largest palindrome of the product of two 3 digit numbers
palindrome :: Int -> Bool
palindrome x = show x == (reverse $ show x)

palProducts = [x*y | x <- [100..999], y <- [100..999], palindrome (x*y)]

problem4 = maximum palProducts