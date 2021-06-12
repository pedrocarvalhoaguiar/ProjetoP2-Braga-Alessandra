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
        print("\n---- BEM VINDO ----\n")
        print('[1] - Cadastrar por biometria')
        print('[2] - Cadastro por CPF')
        print('[3] - Receber vacinas')
        print('[4] - Buscar cadastro')
        print('[5] - Sair')
        op = self.leOpMenuPrincipal()
        return op

    def menuBusca(self):
        print("\n---- MENU DE BUSCA ----\n")
        print('[1] - Buscar por Biometria')
        print('[2] - Buscar por CPF')
        print('[3] - Mostrar estoque de vacinas')
        print('[4] - Mostrar todos moradores cadastrados')
        print('[5] - Voltar ao menu principal')
        print('[6] - Sair')
        sleep(1)
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

    def buscarmoradorderua(self):
        print("\n---- BUSCA MORADORES DE RUA ----\n")
        caminhoArquivo = filedialog.askopenfilename()
        sleep(1)
        return caminhoArquivo

    def receberCPF(self):
        print("\n---- BUSCA MORADORES ----\n")
        cpf = input('Informe o CPF: ')
        sleep(1)
        return cpf

    def leOpMenuPrincipal(self):
        op = input('Digite uma opção válida: ')
        return op

    def procurando(self):
        print("\nProcurando no sistema...")
        sleep(2)

    def buscarvacinas(self):
        print("\n---- BUSCA VACINAS ----\n")
        int(input('Informe o nome: '))
        sleep(1)

    def carregando(self):
        print("\nCarregando lista...\n")
        sleep(1)

    def CPF(self):
        CPF = int(input("Digite o CPF: "))
        return CPF

    def opcaoInvalida(self):
        print("\n*---------------*")
        print('\nOpção inválida!')
        print("\n*---------------*\n")

    def usuNaoEncontrado(self):
        print('Usuário não encontrado!')

    def saindodosistema(self):
        print("\nSaindo do sistema...")
        sleep(2)

    def adicionandobiometria(self):
        print("\nAdicione biometria...\n")
        sleep(2)

    def lendobiometria(self):
        print("\nLendo biometria...\n")
        sleep(2)

    def cadastrosucesso(self):
        print("\nCadastrado com sucesso!\n")
        sleep(1)

    def cadastrando(self):
        print("\nCadastrando...")
        sleep(2)