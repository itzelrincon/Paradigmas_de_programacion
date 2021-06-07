class Calculadora:

	def	__init__(self,a,b):
		self.a = a
		self.b = b

	def suma(self):
		suma = self.a + self.b
		return suma

	def resta(self):
		resta = self.a - self.b
		return resta

	def mult(self):
		mult = self.a * self.b
		return mult
	
	def div(self):
		div = self.a / self.b
		return div 

	def mod(self):
		mod = self.a % self.b
		return mod
