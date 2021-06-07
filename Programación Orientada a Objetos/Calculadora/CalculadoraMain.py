from Calculadora import *
import array

print("+--------------------------+")
print("|        CALCULADORA       |")
print("+--------------------------+")

'''print("\n")'''

n = int(input("Cantidad de números a operar: "))
SumaT = 0
RestaT = 0
Mult = 1

if n == 2:
	a = int(input(" Ingresa un número: "))
	b = int(input(" Ingresa otro número: "))
	def Cal(a,b):
		x = Calculadora(a,b)
		suma = x.suma()
		resta = x.resta()
		mult = x.mult()
		div = x.div()
		mod = x.mod()
		return suma, resta, mult, div, mod

	Operaciones = Cal(a,b)
#print("+--------------------------+")
	print("|    Suma: " + str(Operaciones[0]) + "               |")
#print("+--------------------------+")
	print("|    Resta: " + str(Operaciones[1]) + "              |")
#print("+--------------------------+")
	print("|    Multiplicación: " + str(Operaciones[2]) + "     |")
#print("+--------------------------+")
	print("|    División: " + str(Operaciones[3]) + "         |")
#print("+--------------------------+")
	print("|    Residuo: " + str(Operaciones[4]) + "            |")
	
else:
	while n > 0:
		num = int(input("Ingresa un número: "))
		SumaT = SumaT + num
		RestaT = RestaT - num
		Mult = Mult * num
		n = n - 1	
		if n == 0:
			print("\n")
			print("Suma: " + str(SumaT))
			print("Resta: " + str(RestaT))
			print("Multiplicación: " + str(Mult))
			break

#ask = input("¿Desea ingresar otro número? S/N \n")

# if ask == "S":
# 	i = 0
# 	Nums = [i]
# 	while ask in "S":
# 		c = int(input("Ingresa otro número:"))
# 		i = 0
# 		Nums[i] = c
# 		i = i + 1
# 		ask = input("¿Desea ingresar otro número? S/N \n")

# def Cal(a,b):
# 	x = Calculadora(a,b)
# 	for l in range(0,len(Nums)):
# 		SumaVarios = x.SumaVarios() + i
# 		i = i + 1
# 		return SumaVarios
# print(SumaVarios)	
