from time import sleep

class Interface():
    def inicializaInterface(self):
        print("\nInicializando Sistema...")
        sleep(1)

    def menuPrincipal(self):
        print("\n---- BEM VINDO ----\n")
        print('[1] - Cadastro de moradores de rua')
        print('[2] - Cadastro de moradores')
        print('[3] - Cadastro de vacinas')
        print('[4] - Buscar')
        print('[5] - Sair')
        op = self.leOpMenuPrincipal()
        return op

    def cadastromoradorrua(self):
        print("\n---- CADASTRO DE MORADORES DE RUA ----\n")
        nome = input("Digite o nome: ")
        idade = input("Digite a idade: ")
        return nome, idade

    def adicionandobiometria(self):
        print("\nAdicione biometria...\n")
        sleep(2)

    def lendobiometria(self):
        print("\nLendo biometria...\n")
        sleep(2)

    def cadastrosucesso(self):
        print("\nCadastrado com sucesso!\n")
        sleep(1)

    def cadastromoradornormal(self):
        print("\n---- CADASTRO DE MORADORES ----\n")
        nome = input("Digite o nome: ")
        idade = input("Digite a idade: ")
        endereco = input("Digite o endereço: ")
        CPF = input("Digite o número de CPF: ")
        return nome, idade, CPF, endereco

    def cadastrando(self):
        print("\nCadastrando...")
        sleep(2)

    def cadastrovacina(self):
        print("\n---- CADASTRO DE VACINAS ----\n")
        nome = input("Digite o nome: ")
        fabricante = input("Informe o fabricante: ")
        lote = input("Informe o lote: ")
        validade = input("Digite a data de validade: ")
        return fabricante, lote, validade, nome

    def buscar(self):
        print("\n---- MENU DE BUSCA ----\n")
        print('[1] - Buscar morador normal')
        print('[2] - Buscar morador de rua')
        print('[3] - Buscar vacina')
        print('[4] - Mostrar todos moradores cadastrados')
        sleep(1)
        op = self.leOpMenuPrincipal()
        return op

    def buscarmoradornormal(self):
        print("\n---- BUSCA MORADORES ----\n")
        int(input('Informe o CPF: '))
        sleep(1)

    def procurando(self):
        print("\nProcurando no sistema...")
        sleep(2)

    def buscarmoradorderua(self):
        print("\n---- BUSCA MORADORES DE RUA ----\n")
        int(input('Informe a biometria: '))
        sleep(1)

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

    def Biometria(self):
        Bio = int(input("Digite o código de biometria: "))
        return Bio

    def leOpMenuPrincipal(self):
        op = (input('Digite uma opção válida: '))
        return op

    def opcaoInvalida(self):
        print("\n*---------------*")
        print('\nOpção inválida!')
        print("\n*---------------*\n")

    def usuNaoEncontrado(self):
        print('Usuário não encontrado!')

    def saindodosistema(self):
        print("\nSaindo do sistema...")
        sleep(2)
        return

