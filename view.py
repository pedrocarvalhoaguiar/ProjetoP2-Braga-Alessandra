from time import sleep
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()

class Interface():
    
    def linhaDupla(self):
        print("====================================\n")
    def linhaAster(self):
        print("************************************")

    def menuPrincipal(self):
        print("************************************")
        print('***         BEM VINDO            ***')
        print("************************************\n")
        print('[1] - Cadastrar por Biometria')
        print('[2] - Cadastrar por CPF')
        print('[3] - Cadastrar Vacinas')
        print('[4] - Pesquisar Cadastro/Vacina')
        print('[5] - Sair')
        op = self.leOpMenuPrincipal()
        return op

    def menuBusca(self):
        print("\n************************************")
        print("***      OPÇÕES DE PESQUISA      ***")
        print("************************************")
        print('[1] - Pesquisar por Biometria')
        print('[2] - Pesquisar por CPF')
        print('[3] - Exibir estoque de vacinas')
        print('[4] - Exibir cadastrados')
        print('[5] - Voltar ao menu principal')
        print('[6] - Sair')
        op = self.leOpMenuPrincipal()
        return op

    def menuCadastrado(self):
        self.linhaAster()
        print("***      ESCOLHA UMA OPÇÃO      ***")
        self.linhaAster()
        print('[1] - Vacinar')
        print('[2] - Alterar cadastro')
        print('[3] - Excluir cadastro')
        print('[4] - Voltar ao menu anterior')
        print('[5] - Sair')
        op = self.leOpMenuPrincipal()
        return op

    def receberInfoBIO(self):
        print("************************************")
        print("***     CADASTRO DE BIOMETRIA    ***")
        print("************************************")
        nome = input("Digite o nome: ")
        idade = input("Digite a idade: ")
        return nome, idade

    def receberInfoCPF(self):
        print("************************************")
        print("***       CADASTRO DE CPF       ***")
        print("************************************")
        nome = input("Digite o nome: ")
        idade = input("Digite a idade: ")
        cpf = input("Digite o número de CPF: ")
        return nome, idade, cpf

    def receberInfoVacina(self):
        print("************************************")
        print("***       CADASTRA VACINA        ***")
        print("************************************")
        fabricante = input("Informe o fabricante: ")
        lote = input("Informe o lote: ")
        quantidade = input("Digite a quantidade: ")
        return fabricante, lote, quantidade

    def lerBiometria(self):
        print("************************************")
        print("***    PESQUISA POR BIOMETRIA    ***")
        print("************************************\n")
        print(">>> SELECIONE O ARQUIVO DA BIOMETRIA")
        caminhoArquivo = filedialog.askopenfilename()
        return caminhoArquivo

    def lerCPF(self):
        self.linhaAster()
        print("***    PESQUISA POR CPF    ***")
        self.linhaAster()
        cpf = input('Informe o CPF: ')
        sleep(1)
        return cpf

    def leOpMenuPrincipal(self):
        op = input('\n>>> Digite uma opção válida: ')
        return op

    def procurando(self):
        print(">>> Procurando no sistema...\n")
        sleep(1)

    def carregando(self):

        print(">>> Carregando lista...\n")
        sleep(1)

    def opcaoInvalida(self):
        print('\n| >>>     OPÇÃO INVÁLIDA!      <<< |')
        self.linhaDupla()

    def bioInvalida(self):
        print('\n| >>>   BIOMETRIA INVÁLIDA!    <<< |')
        self.linhaDupla()

    def cpfInvalido(self):
        print('\n| >>>     CPF INVÁLIDO!        <<< |')
        self.linhaDupla()

    def usuNaoEncontrado(self):
        print('| >>>  USUÁRIO NÃO ENCONTRADO! <<< |')
        self.linhaDupla()

    def saindodosistema(self):
        print(">>> Saindo do sistema...\n")
        self.linhaDupla()
        sleep(1)

    def adicionandobiometria(self):
        print(">>> ADICIONANDO BIOMETRIA...")
        sleep(1)

    def lendobiometria(self):
        print(">>> LENDO BIOMETRIA...")
        sleep(1)

    def cadastrosucesso(self):
        print(">>> CADASTRADO EFETUADO COM SUCESSO!")
        self.linhaDupla()
        sleep(1)

    def cadastrando(self):
        print(">>> CADASTRANDO...")
        sleep(1)

    def tituloMostrarVacina(self, qnt):
        self.linhaAster()
        print(f"***  {qnt}     VACINA(S) EM ESTOQUE      ***")
        self.linhaAster()

    def mostrarVacina(self, vacina):
        print(f'{vacina}')
        print('|')

    def estoqueVazio(self):
        print('| >>>   ESTOQUE VAZIO    <<< |')
        self.linhaDupla()

    def pessoaVacinada(self):
        self.linhaDupla()
        print('| >>>    USUÁRIO JÁ VACINADO   <<< |')
        self.linhaDupla()

    def vacinadoComSucesso(self):
        print('\n >>> Vacinado com sucesso!')
        self.linhaDupla()

    def semMoradores(self, tipo):
        print(f'| >>>  NÃO HÁ CADASTROS POR {tipo}! <<< |')
        self.linhaDupla()

    def mostrarMoradores(self, arvoreMoradores, tipo, qnt):
        print(f'| >>> {qnt} morador(es) cadastrado(s) por {tipo}')
        for morador in arvoreMoradores:
            print(f'{morador}')
            self.linhaDupla()

    def mostrarCadastrado(self, morador):
        print(f'\n{morador}')
        self.linhaDupla()

    def refazerCadastro(self, morador):
        self.linhaAster()
        print("***       ALTERAR CADASTRO       ***")
        self.linhaAster()
        print(f'{morador}\n')
        print('[1] - Recadastrar com BIOMETRIA')
        print('[2] - Recadastrar com CPF')
        print('[3] - Não recadastrar\n')
        op = self.leOpMenuPrincipal()
        return op
    
    def excluidoComSucesso(self, morador):
        self.linhaAster()
        print("***   DADOS DO CADASTRADO  ***")
        self.linhaAster()
        print(f'{morador}')
        print('| >>>   EXCLUIDO COM SUCESSO!  <<< |')
        self.linhaDupla()


    def alteradoComSucesso(self):
        print('| >>>DADOS ALTERADOS COM SUCESSO!<<< |')
        self.linhaDupla()