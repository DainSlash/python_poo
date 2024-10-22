from typing import List

class Quiz():
	__acertos : int
	__erros : int
	
	def __init__(self, acertos : int, erros : int):
		self.__acertos = acertos
		self.__erros = erros
	
	
	def calcular_pontos(self):
		return self.__acertos - self.__erros
	
	def get_acertos (self):
		return self.__acertos

	def get_erros (self):
		return self.__erros
		
	def __str__(self):
		return f'Acertos: {self.__acertos}\nErros: {self.__erros}\nPontos: {self.calcular_pontos()}\n\n'

	
class Quiz2A(Quiz):
	def calcular_pontos(self):
		return self.get_acertos() - (self.get_erros()*4)
		
class Quiz3A(Quiz):
	def calcular_pontos(self):
		return self.get_acertos() - (self.get_erros()*2)
		
		
class Aluno():
	__matricula : str
	__nome : str
	__quizes : List[Quiz]
	
	def __init__(self, matricula : str, nome : str, quizes : List[Quiz]):
		self.__matricula = matricula 
		self.__nome = nome
		self.__quizes = quizes
	
	def get_matricula(self):
		return self.__matricula
	
	
	def __str__(self):
		
		total = 0		
		for quiz in self.__quizes:
			total += quiz.calcular_pontos()

		return f'Matricula: {self.__matricula}\nNome: {self.__nome}\nTotal pontos: {total}\n\n'
		
class Disciplina():
	__nome : str
	__professor : str
	__ano : int
	__semestre : int
	__alunos : List[Aluno] = []
		
		
	def __init__(self, nome : str, professor : str, ano : int, semestre : int):
		self.__nome = nome 
		self.__professor = professor 
		self.__ano = ano
		self.__semestre = semestre 
	
	def add_aluno(self, a : Aluno):
		
		alredy_hass = False
		
		for aluno in self.__alunos:
			if(a.get_matricula() == aluno.get_matricula()):
				alredy_hass = True
		
		if(alredy_hass):
			raise Exception("Já tem um aluno com essa matricula {a.get_matricula()}")

		self.__alunos.append(a)
	
	def __str__(self):
		info = f'Nome da disciplina: {self.__nome}\nNome do professor: {self.__professor}\nAno da turma: {self.__ano}\nSemestre: {self.__semestre}\n\n'
		
		for aluno in self.__alunos:
			info += aluno.__str__()
		
		return info
	
