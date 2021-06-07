class Rectangulo:
	
	def __init__(self, a, b, c, d):
		self.a = a
		self.b = b
		self.c = c
		self.d = d
		self.base = 0
		self.altura = 0
		self.area_vertices()

	def __init__(self, base, altura):
		self.a = (0,0)
		self.base = base
		self.altura = altura

	def area_baseAltura(self):
		area = self.base * self.altura
		return area

	def area_vertices(self):
		self.base = b(0) - a(0)
		self.altura = c(1) - a(1)
		area = self.base * self.altura
		return area
	
	def dibujar(self):
	  	for i in range(self.base):
	        for i in range(self.altura):
	            print ("*", end='')
	        print("")
