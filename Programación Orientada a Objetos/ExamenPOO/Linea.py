class Linea:

	def __init__(self, p1, p2):
		self.p1 = p1.getPunto()
		self.p2 = p2.getPunto();

	@classmethod
	def linea(cls):
		self.l1 = [0,0]
		self.l2 = [0,0]

	@property
	def l1(self):
		return self._l1
	@l1.setter	
	def l1 (self,l2):
		self.l1 = l1

	@property
	def l2(self):
		return self.l2
	@l2.setter
	def l2 (self,l2):
		self.l2 = l2
		
	def mueve_derecha(self):
		self.l1[0] = self.l1[0] + a
		self.l2[0] = self.l2[0] + a

	def mueve_izquierda(self):
		self.l1[0] = self.l1[0] - (a)
		self.l2[0] = self.l2[0] - (a)

	def mueve_arriba(self):
		self.l1[1] = self.l1[1] + a
		self.l2[1] = self.l2[1] + a

	def mueve_abajo(self):
		self.l1[1] = self.l1[1] - (a)
		self.l2[1] = self.l2[1] - (a)
