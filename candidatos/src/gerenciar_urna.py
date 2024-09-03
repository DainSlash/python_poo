from common import *
from eleicao import Urna

def iniciar_urna(eleitores, candidatos):
	print("Iniciando Urna")
	print("==============")
	secao = int(input("Número da secao: "))
	zona = int(input("Número da zona: "))

	nome_mes = input("Nome do Mesario: ")
	rg_mes = input("RG do Mesario: ")
	cpf_mes = input("CPF do Mesario: ")

	mesario = Pessoa(nome_mes, rg_mes, cpf_mes)
	urna = Urna(mesario, secao, zona, candidatos, eleitores)
	print(urna)
	return urna

def votar(urna : Urna):
	titulo = int(input("Digite o titulo do eleitor: "))
	eleitor = urna.get_eleitor(titulo=1)

	if not eleitor:
		raise Exception("Eleitor não é desta Urna")

	print(eleitor)
	print("Pode votar!")
	print("===========")
	voto = int(input("Digite o numero do candidato: "))
	urna.registrar_voto(eleitor, voto)

