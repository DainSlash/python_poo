from frota import *
from operar_carro import *
import pickle
import pickletools

if __name__ == "__main__":
	
	carros = {}

	try:
		with open("carros.pkl","rb") as arquivo:	
			carros = pickle.load(arquivo)
			carros = [carro for carro in carros.values()]
			
	except:
		'''-=-=-=-=-=-=-=- CARRO 1 -=--=-=-=-=-=-'''
		print('Cadastre o primeiro carro')
		nm_modelo = input('Digite o modelo: ')
		nm_marca = input('Digite a marca: ')
		nm_cor = input('Digite a cor: ')

		#kms = float(input('Digite com quantos Kms: '))
		kms = float(0.0)
		qtd_tanque = float(input('Digite quantos Litros tem no tanque: '))
		consumo_medio = float(input('Digite o consumo Médio por KM do carro: '))
		carros[0] = Carro(nm_modelo, nm_marca, nm_cor, kms, qtd_tanque, consumo_medio, motor = False)
	
		'''-=-=-=-=-=-=-=- CARRO 2 -=--=-=-=-=-=-'''
		print('\nCadastre o segundo carro')
		nm_modelo = input('Digite o modelo: ')
		nm_marca = input('Digite a marca: ')
		nm_cor = input('Digite a cor: ')

		#kms = float(input('Digite com quantos Kms: '))
		kms = float(0.0)
		qtd_tanque = float(input('Digite quantos Litros tem no tanque: '))
		consumo_medio = float(input('Digite o consumo Médio por KM do carro: '))
		carros[1] = Carro(nm_modelo, nm_marca, nm_cor, kms, qtd_tanque, consumo_medio, motor = False)

		try:
			with open("carros.pkl","wb") as arquivo:
				pickle.dump(carros, arquivo)
		except Exception as e:
			print(e)

	
	

	while carros[0].get_odometro() < 600 and carros[0].get_odometro() < 600:
		try:
			carro = int(input('Escolha um carro 1 ou 2: '))
			operar_carro(carros[carro-1])
		except Exception as e:
		    print("Erro!")
		    print(e)

	try:
		carros[0].desligar()
		carros[1].desligar()
	except Exception as e:
		pass
	
	print('\n\n-=-=-=-=\nCarro 1: ')
	print(carros[0])
	print('-=-=-=-=\nCarro 2: ')
	print(carros[1])

