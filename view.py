from time import sleep
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()

class Interface():
    def inicializaInterface(self):
        print("\nInicializando Sistema...")
        sleep(1)

    def menuPrincipal(self):
        sleep(1)
        print("\n---- BEM VINDO ----\n")
        print('[1] - Cadastrar por Biometria')
        print('[2] - Cadastrar por CPF')
        print('[3] - Cadastrar vacinas')
        print('[4] - Buscar cadastro')
        print('[5] - Sair')
        op = self.leOpMenuPrincipal()
        return op

    def menuBusca(self):
        sleep(1)
        print("---- MENU DE BUSCA ----\n")
        print('[1] - Buscar por Biometria')
        print('[2] - Buscar por CPF')
        print('[3] - Mostrar estoque de vacinas')
        print('[4] - Mostrar todos moradores cadastrados')
        print('[5] - Voltar ao menu principal')
        print('[6] - Sair')
        op = self.leOpMenuPrincipal()
        return op

    def menuCadastrado(self):
        print("\n---- MENU DO MORADOR ----\n")
        print('[1] - Vacinar morador')
        print('[2] - Alterar cadastro')
        print('[3] - Excluir cadastro')
        print('[4] - Voltar ao menu principal')
        print('[5] - Sair')
        op = self.leOpMenuPrincipal()
        return op

    def receberInfoBIO(self):
        print("\n---- CADASTRO DE MORADORES DE RUA ----\n")
        nome = input("Digite o nome: ")
        idade = input("Digite a idade: ")
        return nome, idade

    def receberInfoCPF(self):
        print("\n---- CADASTRO DE MORADORES ----\n")
        nome = input("Digite o nome: ")
        idade = input("Digite a idade: ")
        cpf = input("Digite o número de CPF: ")
        return nome, idade, cpf

    def receberInfoVacina(self):
        print("\n---- CADASTRO DE VACINAS ----\n")
        fabricante = input("Informe o fabricante: ")
        lote = input("Informe o lote: ")
        quantidade = input("Digite a quantidade: ")
        return fabricante, lote, quantidade

    def lerBiometria(self):
        print("---- BUSCA MORADORES DE RUA ----\n")
        caminhoArquivo = filedialog.askopenfilename()
        return caminhoArquivo

    def lerCPF(self):
        print("\n---- BUSCA MORADORES ----\n")
        cpf = input('Informe o CPF: ')
        sleep(1)
        return cpf

    def leOpMenuPrincipal(self):
        op = input('\nDigite uma opção válida: ')
        return op

    def procurando(self):
        print("\nProcurando no sistema...")
        sleep(1)

    def carregando(self):
        print("\nCarregando lista...\n")
        sleep(1)

    def opcaoInvalida(self):
        print("*---------------*")
        print('Opção inválida!')
        print("*---------------*\n")

    def bioInvalida(self):
        print("*---------------*")
        print('Biometria inválida!')
        print("*---------------*\n")

    def cpfInvalido(self):
        print("*---------------*")
        print('CPF inválida!')
        print("*---------------*\n")

    def usuNaoEncontrado(self):
        print('Usuário não encontrado!')

    def saindodosistema(self):
        print("Saindo do sistema...\n")
        sleep(2)

    def adicionandobiometria(self):
        print("Adicione biometria...\n")
        sleep(1)

    def lendobiometria(self):
        print("Lendo biometria...\n")
        sleep(1)

    def cadastrosucesso(self):
        print("Cadastrado com sucesso!\n")
        sleep(1)

    def cadastrando(self):
        print("Cadastrando...\n")
        sleep(1)

    def mostrarVacina(self, vacina):
        print("----- VACINA EM ESTOQUE -----\n")
        print(f'{vacina}\n')
        print("---------------")

    def estoqueVazio(self):
        print("*---------------*")
        print("Estoque Vazio")
        print("*---------------*")

    def pessoaVacinada(self):
        print("*---------------*")
        print('Você já está vacinado!')
        print("*---------------*\n")

    def vacinadoComSucesso(self):
        print("*---------------*")
        print('Vacinado com sucesso!')
        print("*---------------*\n")

    def semMoradores(self, tipo):
        print("*---------------*")
        print(f'Não há moradores cadastrados por {tipo}!')
        print("*---------------*\n")

    def mostrarMoradores(self, arvoreMoradores, tipo, qnt):
        print(f'{qnt} morador(es) cadastrado(s) por {tipo}')
        for morador in arvoreMoradores:
            print(f'{morador}')
            print("*---------------*\n")

    def mostrarCadastrado(self, morador):
        print(f'\n{morador}')
        print("*---------------*")

    def refazerCadastro(self, morador):
        print("\n----- RECADASTRAMENTO -----")
        print('------ DADOS DO MORADOR -----\n')
        print(f'{morador}\n')
        print('[1] - Recadastrar com BIOMETRIA')
        print('[2] - Recadastrar com CPF')
        print('[3] - Não recadastrar\n')
        op = self.leOpMenuPrincipal()
        return op
    
    def excluidoComSucesso(self, morador):
        print('\n------ DADOS DO MORADOR -----')
        print(f'{morador}')
        print('---- Excluído com sucesso! ----')