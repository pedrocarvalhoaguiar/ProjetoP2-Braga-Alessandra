from controller import Controlador
from model import *
if __name__ == '__main__':
    controlador = Controlador()
    pessoa1 = PessoaCPF('za', 1, cpf='123')
    pessoa2 = PessoaCPF('z33', 1, cpf='131')

    controlador.gerenciador.gerPessoas.cadastrarPessoa(pessoa1)
    controlador.gerenciador.gerPessoas.cadastrarPessoa(pessoa2)