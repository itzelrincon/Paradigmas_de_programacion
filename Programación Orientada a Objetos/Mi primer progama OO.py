class Persona()

	def_init_(self, nombre, edad):
		self.nombre = nombre
		self.edad = edad

	def mostrar(self, msg)
		return msg

class Empleado(Persona)
	
	def_init_(self,sueldoB):
		Persona._init_(self,nombre,edad):
		
		self.sueldoB = sueldoB

	def mostrar(self,msg)
		return msg		

	def salario(self, calular):
		return calular
		pass
