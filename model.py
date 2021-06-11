from estruturadedados.avltree import AVL
from estruturadedados.queue import Queue
from biometria.biometria import Biometria as Bio
from bancodedados.paths import *
from os import listdir


class GerenciadorPrincipal():
    
    def __init__(self):
        self.gerVacina = GerenciadorVacina()
        self.gerUsuario = GerenciadorUsuario()
        self.gerPessoas = GerenciadorPessoas()
        self.gerBiometria = GerenciadorBiometria()
        self.carregarDados()

    def carregarDados(self):
        self.gerBiometria.carregarArvore()
        self.gerUsuario.carregarArvore()
        self.gerVacina.carregarArvore()
        self.gerPessoas.carregarArvore()

    def salvarVacina(self):
        pass

    def procurarPessoaCPF(self, chave, nome, novoNome):
        pass

    def obterListaVacinadosCPF(self):
        self.gerPessoas.obterListaPessoasCPF()

class GerenciadorPessoas():
    
    def __init__(self):
        self.arvorePessoasCPF = AVL()
        self.arvorePessoasBiometria = AVL()

    def carregarPessoasCPF(self):
        pass

    def carregarPessoasBiometria(self):
        pass

    def associarBiometria(self, vacinado, biometria):
        vacinado.associarBio(biometria)

class GerenciadorBiometria():

    def __init__(self):
        self.arvoreBiometrias = AVL()
        self.biometria = Bio()
        self.__carregarArvore()

    def cadastrarBiometria(self):
        biometria = self.biometria.criar('_')
        self.arvoreBiometrias.insert(biometria)
        return  biometria

    def pegarNomes(self):
        nomes = [".".join(f.split(".")[:-1]) for f in listdir(path=BIO) if f.endswith('.json')]
        return nomes

    def criarBiometria(self):
        return self.biometria.criar()

    def __carregarArvore(self):
        nomes = self.pegarNomes()
        self.arvoreBiometrias.inserirLista(nomes)

    def compararBiometria(self, path):
        nome = nameFromPath(path)
        caminho = caminhoFromPath(path)
        biometriaBD = self._procurarBiometria(nome)
        if biometriaBD:
            biometriaTeste = self.biometria.leArquivo(nome, path=caminho)
            biometriaBD = self.biometria.leArquivo(biometriaBD.chave)
            arvoreTeste = self._carregarArvore(biometriaTeste)
            arvoreBD = self._carregarArvore(biometriaBD)
            return print(self._igual(arvoreBD.root, arvoreTeste.root))
        return print(False)

    def _carregarArvore(self, lista):
        arvore = AVL()
        arvore.inserirLista(lista)
        return arvore

    def _procurarBiometria(self, chave):
        try:
            biometria = self.arvoreBiometrias.search(chave)
        except:
            return False
        return biometria

    def _igual(self, p1, p2):
        if p1 == None and p2 == None:
            return True
        if p1 == None or p2 == None:
            return False
        fila1 = Queue()
        fila2 = Queue()
        fila1.push(p1)
        fila2.push(p2)
        count = 0
        while not fila1.isEmpty() and not fila2.isEmpty():
            pos1 = fila1.first.valor
            pos2 = fila2.first.valor
            if pos1.chave != pos2.chave:
                return False
            fila1.pop()
            fila2.pop()
            count +=1
            if count > 40:
                return True
            if pos1.left and pos2.left:
                fila1.push(pos1.left)
                fila2.push(pos2.left)
            elif pos1.left or pos2.right:
                return False
            if pos1.right and pos2.right:
                fila1.push(pos1.right)
                fila2.push(pos2.right)
            elif pos1.right or pos2.right:
                return False
        return True

class Pessoa():
    pass 

class PessoaCPF(Pessoa):
    pass

class PessoaDeRua(Pessoa):
    pass

class GerenciadorUsuario():
    pass

class Usuario(Pessoa):
    pass

class GerenciadorVacina():
    pass    

class Vacina():

    pass
