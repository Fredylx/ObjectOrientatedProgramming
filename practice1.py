class Computer:
	
	def __init__(self, cpu, ram):
		self.cpu = cpu
		self.ram = ram

	def config(self):
		print(“Config is “, self.cpu, self. Ram) 

com1 = Computer(‘i5’, 16)
com2 = Computer(‘Risen’, 8)

Computer.config(com1)
Computer.config(com2)
com1.config()
com2.config()

