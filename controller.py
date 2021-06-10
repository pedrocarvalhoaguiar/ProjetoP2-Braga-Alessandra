from view import *
from model import *

class Controlador():

    def __init__(self):
        self.interface = Interface()
        self.gerenciador = GerenciadorPrincipal()

    def iniciar(self):
        while True:
            opcaoMenu = (self.interface.menuPrincipal())
            if (opcaoMenu == "1"):
                self.interface.cadastromoradorrua()
                self.interface.adicionandobiometria()
                self.interface.lendobiometria()
                self.interface.cadastrosucesso()
            elif opcaoMenu == "2":
                Cadmor = self.interface.cadastromoradornormal()
                self.interface.cadastrando()
                self.interface.cadastrosucesso()
            elif opcaoMenu == "3":
                Cadvacina = self.interface.cadastrovacina()
                self.interface.cadastrando()
                self.interface.cadastrosucesso()
            elif opcaoMenu == "4":
                Buscar = self.interface.buscar()
                if Buscar == "1":
                    self.interface.buscarmoradornormal()
                    self.interface.procurando()
                elif Buscar == "2":
                    self.interface.buscarmoradorderua()
                    self.interface.procurando()
                elif Buscar == "3":
                    self.interface.buscarvacinas()
                    self.interface.procurando()
                elif Buscar == "4":
                    self.interface.carregando()
                    self.interface.procurando()
                else:
                    self.interface.opcaoInvalida()
            elif opcaoMenu == "5":
                self.interface.saindodosistema()
                break
            else:
                self.interface.opcaoInvalida()

