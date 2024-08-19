from frota import *

def operar_carro(carro : Carro):
	try:
		print('\n')
		print('1- Ligar motor')
		print('2- Desligar motor')
		print('3- Acelerar')

		op = 0
		while op not in (1,2,3):
			op = int(input("Digite as opcoes[1-3]: "))

		if op == 1:
			carro.ligar()
		elif op == 2:
			carro.desligar()
		elif op == 3:
			v = float(input("Informe a velocidade: "))
			t = float(input("Informe o tempo: "))
			carro.acelerar(v, t)

		print('\nInfos atuais do carro\n')
		print(carro)
	except Exception as e:
		print("Erro!")
		print(e)
