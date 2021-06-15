from view import *
from model import *

class Controlador():

    def __init__(self):
        self.interface = Interface()
        self.gerenciador = GerenciadorPrincipal()

    def menuPrincipal(self):
        while True:
            opcaoMenu = (self.interface.menuPrincipal())
            if (opcaoMenu == "1"):
                self.cadastroBIO()
            elif opcaoMenu == "2":
                self.cadastroCPF()
            elif opcaoMenu == "3":
                self.cadastroVacina()
            elif opcaoMenu == "4":
                self.menuBusca()
            elif opcaoMenu == "5":
                self.interface.saindodosistema()
                break
            else:
                self.interface.opcaoInvalida()

    def menuBusca(self):
        while True:
            buscarSec = self.interface.menuBusca()
            if buscarSec == "1":
                self.buscarBiometria()
            elif buscarSec == "2":
                self.buscarCPF()
            elif buscarSec == "3":
                self.mostrarEstoque()
            elif buscarSec == "4":
                self.mostrarCadastrados()
            elif buscarSec == "5":
                self.menuPrincipal()
            elif buscarSec =="6":
                self.interface.saindodosistema()
                quit()
            else:
                self.interface.opcaoInvalida()

    def menuCadastrado(self, pessoa):
        while True:
            self.interface.mostrarCadastrado(pessoa)
            opTer = self.interface.menuCadastrado()
            if opTer == '1':
                self.vacinarPessoa(pessoa)
            elif opTer == '2':
                self.alterarPessoa(pessoa)
            elif opTer == '3':
                self.excluirCadastro(pessoa)
                self.menuBusca()
            elif opTer == '4':
                self.menuBusca()
            elif opTer == '5':
                self.interface.saindodosistema()
                quit()
            else:
                self.interface.opcaoInvalida()

    def cadastroBIO(self, novaPessoa=None):
        bio = self.gerenciador.gerBiometria.cadastrarBiometria()
        nome, idade = self.interface.receberInfoBIO()
        pessoaBio = PessoaBiometria(nome, idade, biom=str(bio))
        self.interface.adicionandobiometria()
        self.interface.lendobiometria()
        if not novaPessoa:
            self.gerenciador.cadastrarPessoa(pessoaBio)
            self.interface.cadastrosucesso()
        else:
            return pessoaBio

    def cadastroCPF(self, novaPessoa=None):
        nome, idade, cpf = self.interface.receberInfoCPF()
        pessoaCPF = PessoaCPF(nome, idade, cpf=cpf)
        try:
            if not novaPessoa:
                self.gerenciador.cadastrarPessoa(pessoaCPF)
                self.interface.cadastrando()
                self.interface.cadastrosucesso()
            else:
                return pessoaCPF
        except ValueError:
            self.interface.cpfInvalido()

    def cadastroVacina(self):
        fabricante, lote, quantidade = self.interface.receberInfoVacina()
        vacina = Vacina(fabricante, lote, int(quantidade))
        self.gerenciador.cadastrarVacina(vacina)
        self.interface.cadastrando()
        self.interface.cadastrosucesso()

    def buscarBiometria(self):
        self.interface.procurando()
        pathBio = self.interface.lerBiometria()
        try:
            pessoaB = self.gerenciador.retornarPessoaBio(pathBio)
            if pessoaB:
                self.menuCadastrado(pessoaB)
            else:
                self.interface.bioInvalida()
                self.menuBusca()
        except IndexError:
            self.interface.semMoradores('BIOMETRIA')
            self.menuBusca()

    def buscarCPF(self):
        self.interface.procurando()
        cpf = self.interface.lerCPF()
        try:
            pessoaC = self.gerenciador.retornarPessoa(cpf,"cpf")
            self.menuCadastrado(pessoaC)
        except ValueError:
            self.interface.cpfInvalido()
            self.menuBusca()
        except IndexError:
            self.interface.semMoradores('CPF')
            self.menuBusca()
        
    def mostrarEstoque(self):
        self.interface.procurando()
        vacinas = self.gerenciador.retornarArvoreVacinas()
        if vacinas.isEmpty():
            self.interface.estoqueVazio()
        else:
            self.interface.tituloMostrarVacina()
            for vacina in vacinas:
                if vacina.getValor().temVacina():
                    self.interface.mostrarVacina(vacina.getValor())
            self.interface.linhaDupla()
            self.menuBusca()

    def mostrarCadastrados(self):
        self.interface.carregando()
        moradoresCPF = self.gerenciador.retornarArvoreCPF()
        moradoresBio = self.gerenciador.retornarArvoreBio()
        try:
            self.interface.mostrarMoradores(moradoresCPF, 'CPF', moradoresCPF.getSize())
        except (IndexError, AttributeError):
            self.interface.semMoradores('CPF')
        try:
            self.interface.mostrarMoradores(moradoresBio, 'BIOMETRIA', moradoresBio.getSize())
        except (IndexError, AttributeError):
            self.interface.semMoradores('BIOMETRIA')

    def vacinarPessoa(self, pessoa):
        if pessoa.isVac():
            self.interface.pessoaVacinada()
            self.menuCadastrado(pessoa)
        else:
            fab = pessoa.getNomeVacina()
            vacina = self.gerenciador.retornarVacinaValida(fab)
            if vacina:
                self.gerenciador.vacinarPessoa(pessoa, vacina)
                self.interface.vacinadoComSucesso()
            else:
                self.interface.estoqueVazio()
                self.menuCadastrado(pessoa)

    def alterarPessoa(self, pessoa):
        while True:
            op = self.interface.refazerCadastro(pessoa)
            if op == '1':
                novaPessoa = self.cadastroBIO(novaPessoa=True)
                novaPessoa.setDose(pessoa.getDose()), novaPessoa.setVacina(pessoa.getNomeVacina()) 
                self.gerenciador.cadastrarPessoa(novaPessoa)
                self.gerenciador.excluirCadastro(pessoa)
                self.interface.alteradoComSucesso()
                self.menuCadastrado(pessoa)
            elif op == '2':
                novaPessoa = self.cadastroCPF(novaPessoa=True)
                novaPessoa.setDose(pessoa.getDose()), novaPessoa.setVacina(pessoa.getNomeVacina()) 
                self.gerenciador.cadastrarPessoa(novaPessoa)
                self.gerenciador.excluirCadastro(pessoa)
                self.interface.alteradoComSucesso()
                self.menuCadastrado(pessoa)
            elif op == '3':
                self.menuCadastrado(pessoa)
            else:
                self.interface.opcaoInvalida()

    def excluirCadastro(self, pessoa):
        self.gerenciador.excluirCadastro(pessoa)
        self.interface.excluidoComSucesso(pessoa)
