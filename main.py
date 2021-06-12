from controller import Controlador
from model import *
if __name__ == '__main__':
    c = Controlador()
    vacina = Vacina('CoronaVac', '123', 4)
    pessoa1 = PessoaCPF('za', 1, cpf='123')
    pessoa1.vacinar(vacina)
    pessoa2 = PessoaCPF('z33', 1, cpf='131')

    c.gerenciador.cadastrarPessoa(pessoa1)
    c.gerenciador.gerPessoas.cadastrarPessoa(pessoa2)