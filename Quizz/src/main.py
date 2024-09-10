from quiz import *


if __name__ == '__main__':
	quizz1 = Quiz(10,5)
	quizz2 = Quiz(11,5)
	quizz3 = Quiz(12,5)


	quizzes : List[Quiz] = []
	quizzes.append(quizz1)
	quizzes.append(quizz2)
	quizzes.append(quizz3)
	 
	aluno1 = Aluno(1, 'Felipe1', quizzes)
	aluno2 = Aluno(2, 'Felipe2', quizzes)
	aluno3 = Aluno(2, 'Felipe3', quizzes)
	
	alunos : List[Aluno] = []
	alunos.append(aluno1)
	alunos.append(aluno2)
	alunos.append(aluno3)
			
	disciplina = Disciplina('Matematica', 'FELIPAO', 500, 3)
	
	for aluno in alunos:
		disciplina.add_aluno(aluno)
	
	print(disciplina)
	
	
