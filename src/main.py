from frota import *
from operar_carro import *

if __name__ == "__main__":
	print('Cadastre o primeiro carro')
	nm_modelo = input('Digite o modelo: ')
	nm_marca = input('Digite a marca: ')
	nm_cor = input('Digite a cor: ')

	#kms = float(input('Digite com quantos Kms: '))
	kms = float(0.0)
	qtd_tanque = float(input('Digite quantos Litros tem no tanque: '))
	consumo_medio = float(input('Digite o consumo Médio por KM do carro: '))
	carro1 = Carro(nm_modelo, nm_marca, nm_cor, kms, qtd_tanque, consumo_medio, motor = False)

	print('\nCadastre o segundo carro')
	nm_modelo = input('Digite o modelo: ')
	nm_marca = input('Digite a marca: ')
	nm_cor = input('Digite a cor: ')

	#kms = float(input('Digite com quantos Kms: '))
	kms = float(0.0)
	qtd_tanque = float(input('Digite quantos Litros tem no tanque: '))
	consumo_medio = float(input('Digite o consumo Médio por KM do carro: '))
	carro2 = Carro(nm_modelo, nm_marca, nm_cor, kms, qtd_tanque, consumo_medio, motor = False)

	'''
	Controlando o carro até eles atingirem 600 Km
	'''
	while carro1.odometro < 600 and carro2.odometro < 600:
		try:
			carro = int(input('Escolha um carro 1 ou 2: '))
			if carro == 1:
				operar_carro(carro1)
			elif carro == 2:
				operar_carro(carro2)
		except Exception as e:
		    print("Erro!")
		    print(e)

	try:
		carro1.desligar()
		carro2.desligar()
	except Exception as e:
		pass
	
	print('\n\n-=-=-=-=\nCarro 1: ')
	print(carro1)
	print('-=-=-=-=\nCarro 2: ')
	print(carro2)

