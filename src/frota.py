class Carro:
	modelo : str
	marca : str
	cor : str
	consumo_medio : 0.0
	tanque : 0.0
	__odometro : 0.0
	__motor_on : False

	def __init__(self, modelo : str, marca : str, cor : str,
		               odometro : float, tanque : float, consumo_medio: float, motor : bool):
		self.modelo = modelo
		self.marca = marca
		self.cor = cor
		self.__odometro = odometro
		self.tanque = tanque
		self.consumo_medio = consumo_medio
		self.__motor_on = motor

	def get_odometro(self):
		return self.__odometro

	def get_motor(self):
		return self.__motor_on

	def ligar(self):
		if not self.__motor_on and self.tanque>0:
			self.__motor_on = True
		else:
			raise Exception("Erro: Motor já ligado!")

	def acelerar(self, velocidade : float, tempo : float):
		if self.__motor_on:
			kms = velocidade * tempo
			self.tanque = self.tanque-(kms/self.consumo_medio)
			if self.tanque < 0:
				 kms = kms+(self.tanque*self.consumo_medio)
				 self.tanque = 0
				 self.desligar()
				 					 
			self.__odometro += kms
		else:
			raise Exception("Erro: Não é possível acelerar! Motor desligado!")

	def desligar(self):
		if self.__motor_on:
			self.__motor_on = False
		else:
			raise Exception("Erro: Motor já desligado!")

	def __str__(self):
		info = (f'Carro {self.modelo}, marca {self.marca}, '
				f'cor {self.cor}\n{self.__odometro} Km, '
				f'Tanque {self.tanque} '
				f'motor {self.__motor_on}')
		return info





