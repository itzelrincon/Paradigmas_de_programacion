hombre(jose).
hombre(raul).
hombre(juan).
hombre(juanjr).
mujer(maria).
mujer(perla).
mujer(mariana).
mujer(lili).
mujer(itzel).

padres(jose, juan).
padres(perla, juan).
padres(juan, juanjr).
padres(juan, lili).
padres(juan, itzel).
padres(raul, mariana).
padres(maria, mariana).
padres(mariana, juanjr).
padres(mariana, lili).
padres(mariana, itzel).

esposos(jose, perla).
esposos(raul, maria).
esposos(juan, mariana).

padre(X,Y):-hombre(X), padres(X,Y).
madre(X,Y):-mujer(X), padres(X,Y).
hermanos(X,Y):-padres(Z,X), padres(Z,Y).
hermana(X,Y):-hermanos(X,Y), mujer(X).
esposo(X,Y):-esposos(X,Y), hombre(X).
esposa(X,Y):-esposos(X,Y), mujer(X).
suegro(X,Y):-padre(X,Z), esposos(Y,Z).
suegra(X,Y):-madre(X,Z), esposos(Y,Z).
yerno(X,Y):-suegro(Y,X), suegra(Y,X), hombre(X).
nuera(X,Y):-suegro(Y,X), suegra(Y,X), mujer(X).
abuelo(X,Y):-padres(Z,Y), padre(X,Z).
abuela(X,Y):-padres(Z,Y), madre(X,Z).
nieto(X,Y):-padres(Y,Z), padres(Z,X), hombre(x).
nieta(X,Y):-padres(Y,Z), padres(Z,X), mujer(x).
hijo(X,Y):-padres(Y,X), hombre(X).
hija(X,Y):-padres(Y,X), mujer(X).
