from abc import ABC, abstractmethod

class Funcionario(ABC):
    nome : str
    cpf : str
    __senha : int
    
    def __init__(self, nome : str, cpf : str, senha : int) -> None:
        self.nome = nome
        self.cpf = cpf
        self.__senha = senha

    def get_senha(self) -> int:
        return self.__senha

    def __str__(self) -> str:
        return f'Nome: {self.nome}\nCPF: {self.cpf}\n\n'
    
    @abstractmethod
    def autenticar(self, user : str, senha : int) -> bool:
        pass

class Gerente(Funcionario):
    def autenticar(self, user: str, senha: int) -> bool:        
        return (self.cpf == user and self.get_senha() == senha)

    def cancelar_operacao(self, user: str, senha: int) -> str:
        if(self.autenticar(user, senha)):
            return '\noperação cancelada\n'
        return '\nFALHA NA AUTENTICAÇÃO\n'

class Operador_Caixa(Funcionario):
    numero_caixa : int

    def __init__(self, nome: str, cpf: str, senha: int, numero_caixa : int) -> None:
        super().__init__(nome, cpf, senha)
        self.numero_caixa = numero_caixa

    def autenticar(self, user: str, senha: int) -> bool:        
        return (self.numero_caixa == user and self.get_senha() == senha)

    def __str__(self) -> str:
        return f'{super.__str__()} Numero_Caixa: {self.numero_caixa}'
    
    def registrar_produto(self, user: str, senha: int) -> str:
        if(self.autenticar(user, senha)):
            return '\nProduto registrado!\n'
        return '\nFALHA AO AUTENTICAR\n'

class Seguranca(Funcionario):
    posto : int

    def __init__(self, nome: str, cpf: str, senha: int, posto : int) -> None:
        super().__init__(nome, cpf, senha)
        self.posto = posto

    def autenticar(self, user: str, senha: int) -> bool:        
        return (self.posto == user and self.get_senha() == senha)

    def adicionar_alarme(self, user: str, senha: int) -> str:
        if(self.autenticar(user, senha)):
            return '\n\n\nUUUUUUUUUUUUUUUUUUUUUOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUOUUUUUUUUUUUUUUUUUUUUUUUOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU\n\n\n'
        return '\nFALHA AO AUTENTICAR\n'