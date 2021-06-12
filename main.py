from controller import Controlador
from model import *
if __name__ == '__main__':
    controlador = Controlador()
    vacina = Vacina('CoronaVac', '123', 4)
    pessoa1 = PessoaCPF('za', 1, cpf='123')
    pessoa1.vacinar(vacina)
    pessoa2 = PessoaCPF('z33', 1, cpf='131')

    controlador.gerenciador.gerPessoas.cadastrarPessoa(pessoa1)
    controlador.gerenciador.gerPessoas.cadastrarPessoa(pessoa2)