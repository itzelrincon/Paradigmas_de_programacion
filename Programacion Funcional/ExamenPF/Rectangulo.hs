rectangulo :: (Int,Int) -> (Int,Int) -> (Int,Int)
rectangulo (x,y) (z,a) | x * y >= z * a = (x,y)
rectangulo (x,y) (z,a) | otherwise = (z,a)
