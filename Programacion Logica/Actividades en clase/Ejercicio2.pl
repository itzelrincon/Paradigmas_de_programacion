padre(juan, juanjr).
padre(juan, lili).
padre(juan, itzel).
madre(mariana, juanjr).
madre(mariana, lili).
madre(mariana, itzel).

hermano(A, B, C) :- padre(D, A), padre(D, B), padre(D, C), madre(E, A), madre(E, B), madre(A, C).
