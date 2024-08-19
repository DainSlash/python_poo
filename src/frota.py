class Carro:
	modelo : str
	marca : str
	cor : str
	odometro : 0.0
	tanque : 0.0
	consumo_medio : 0.0
	motor_on : False

	def __init__(self, modelo : str, marca : str, cor : str,
		               odometro : float, tanque : float, consumo_medio: float, motor : bool):
		self.modelo = modelo
		self.marca = marca
		self.cor = cor
		self.odometro = odometro
		self.tanque = tanque
		self.consumo_medio = consumo_medio
		self.motor_on = motor

	def ligar(self):
		if not self.motor_on and self.tanque>0:
			self.motor_on = True
		else:
			raise Exception("Erro: Motor já ligado!")

	def acelerar(self, velocidade : float, tempo : float):
		if self.motor_on:
			kms = velocidade * tempo
			self.tanque = self.tanque-(kms/self.consumo_medio)
			if self.tanque < 0:
				 kms = kms+(self.tanque*self.consumo_medio)
				 self.tanque = 0
				 self.desligar()
				 					 
			self.odometro += kms
		else:
			raise Exception("Erro: Não é possível acelerar! Motor desligado!")

	def desligar(self):
		if self.motor_on:
			self.motor_on = False
		else:
			raise Exception("Erro: Motor já desligado!")

	def __str__(self):
		info = (f'Carro {self.modelo}, marca {self.marca}, '
				f'cor {self.cor}\n{self.odometro} Km, '
				f'Tanque {self.tanque} '
				f'motor {self.motor_on}')
		return info





