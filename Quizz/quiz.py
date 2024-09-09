class Quiz():
	disciplina : str
	aluno : str
	__acertos : int
	__erros : int
	
	def __init__(self, disciplina : str, aluno : str, acertos : int, erros : int):
		self.disciplina = disciplina
		self.aluno = aluno
		self.__acertos = acertos
		self.__erros = erros
	
	
	def calcular_pontos(self):
		return self.__acertos - self.__erros
	
	def get_acertos (self):
		return self.__acertos

	def get_erros (self):
		return self.__erros
		
	def __str__(self):
		return f'Disciplina: {self.disciplina}\nAluno: {self.aluno}\nAcertos: {self.__acertos}\nErros: {self.__erros}\nPontos: {self.calcular_pontos()}'
		
