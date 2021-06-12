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
                self.moradorderua()
            elif opcaoMenu == "2":
                self.moradornormal()
            elif opcaoMenu == "3":
                self.vacina()
            elif opcaoMenu == "4":
                self.buscar()
            elif opcaoMenu == "5":
                self.interface.saindodosistema()
                break
            else:
                self.interface.opcaoInvalida()

    def moradorderua(self):
        nome, idade = self.interface.cadastromoradorrua()
        self.interface.adicionandobiometria()
        self.interface.lendobiometria()
        self.interface.cadastrosucesso()

    def moradornormal(self):
        nome, idade, endereco, cpf = self.interface.cadastromoradornormal()
        self.interface.cadastrando()
        self.interface.cadastrosucesso()

    def vacina(self):
        nome, fabricante, lote, validade = self.interface.cadastrovacina()
        self.interface.cadastrando()
        self.interface.cadastrosucesso()

    def buscar(self):
        Buscar = self.interface.buscar()
        if Buscar == "1":
            CPF = self.interface.buscarmoradornormal()
            self.interface.procurando()
        elif Buscar == "2":
            biometria = self.interface.buscarmoradorderua()
            self.interface.procurando()
        elif Buscar == "3":
            nome = self.interface.buscarvacinas()
            self.interface.procurando()
        elif Buscar == "4":
            self.interface.carregando()
            self.interface.procurando()
        else:
            self.interface.opcaoInvalida()


