from Funcinario import * 

if __name__ == '__main__':
    gerente = Gerente('Felipe', '99999999999', 58)

    if(gerente.autenticar('99999999999', 58)):
        print('AUTENTICADO')

    caixa = Operador_Caixa('GuilhermeCarrega', '99999999999', 13, 13)
        
    if(caixa.autenticar(13, 13)):
        print('AUTENTICADO')

    seguranca = Seguranca('Rafael', '99999999999', 22, 22)

    if(seguranca.autenticar(22, 22)):
        print('AUTENTICADO')




    print(gerente.cancelar_operacao('99999999999', 58))
    print(caixa.registrar_produto(13, 13))
    print(seguranca.adicionar_alarme(22, 22))
