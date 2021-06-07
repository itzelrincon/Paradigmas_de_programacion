print("MENÚ\n 1. Suma. \n 2. Resta. \n 3. Multiplicación. \n 4. División.\n\n ¿Qué opción desea realizar?\n")

op = (input())

def suma(x,y):
	total = x + y
	return total

def resta(x,y):
	total = x - y
	return total

def mult(x,y):
	total = x * y
	return total

def div(x,y):
	total = x / y
	return total

def opcion():
	self.op = input()

if op == '1':
	a = int(input("\nIngresa un número: "))
	b = int(input("Ingresa otro número: "))
	print("\nLa suma es: ", suma(a,b))
elif op == '2':
	a = int(input("\nIngresa un número: "))
	b = int(input("Ingresa otro número: "))
	print("\nLa resta es: ", resta(a,b))
elif op == '3':
	a = int(input("\nIngresa un número: "))
	b = int(input("Ingresa otro número: "))
	print("\nLa multiplicación es: ", mult(a,b))
elif op == '4':
	a = int(input("\nIngresa un número: "))
	b = int(input("Ingresa otro número: "))
	print("\nLa división es: ", div(a,b))
else:
	print("\nOpción no válida")
