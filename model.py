from estruturadedados.avltree import AVL
from estruturadedados.queue import Queue
from biometria.biometria import Biometria as Bio
from bancodedados.paths import *
import json
from os import listdir


class GerenciadorPrincipal():
    
    def __init__(self):
        self.gerVacina = GerenciadorVacina()
        self.gerPessoas = GerenciadorPessoas()
        self.gerBiometria = GerenciadorBiometria()

    def cadastrarVacina(self, vacina):
        self.gerVacina.cadastrarVacina(vacina)

    def cadastrarPessoa(self, pessoa):
        pass

    def retornarPessoa(self, chave, tipo):
        return self.gerPessoas.procurarPessoa(chave, tipo)

    def obterListaVacinadosCPF(self):
        self.gerPessoas.obterListaPessoasCPF()

class GerenciadorPessoas():
    
    def __init__(self):
        self.arvorePessoasCPF = AVL()
        self.arvorePessoasBiometria = AVL()
        self._carregarArvore(VACBIO)
        self._carregarArvore(VACCPF)
        

    def _carregarArvore(self, caminho):
        arvore, tipoPessoa, lastAtt = self._chooseType(caminho)
        try:
            with open(f'{caminho}', 'r') as nomeArquivo:
                listaPessoas = json.load(nomeArquivo)
                for k, v in listaPessoas.items():
                    chave = k
                    pessoa = tipoPessoa(v['nome'], v['idade'], v['dose'], v['vacina'], v[f'{lastAtt}'])
                    arvore.insert(chave, valor=pessoa)
        except:
            with open(f'{caminho}', 'w') as f:
                data = {}
                json.dump(data, f, indent=4, ensure_ascii=False)
    
    def alterarAtributo(self, pessoa, novaPessoa):
        self.excluirPessoa(pessoa)
        self.salvarPessoa(novaPessoa)
        
    def cadastrarPessoa(self, pessoa):
        arvore, chave, caminho = self._chooseArvore(pessoa=pessoa)
        arvore.insert(chave, valor=pessoa)
        with open(f'{caminho}', 'r+', encoding='UTF-8') as nomeArquivo:
            listaPessoa = json.load(nomeArquivo)
            listaPessoa[chave] = pessoa.lineRegistry()
            nomeArquivo.seek(0)
            json.dump(listaPessoa, nomeArquivo, indent=4, ensure_ascii=False)

    def vacinarPessoa(self, pessoa, vacina):
        arvore, chave, caminho = self._chooseArvore(pessoa=pessoa)
        pArvore = arvore.search(chave)
        pArvore.valor.dose += 1
        pArvore.valor.vacina = vacina
        with open(f'{caminho}', 'r+', encoding='UTF-8') as nomeArquivo:
            listaPessoas = json.load(nomeArquivo)
            p = listaPessoas[chave]
            p['vacina'] = vacina.fabricante
            p['dose'] += 1
            nomeArquivo.seek(0)
            json.dump(listaPessoas, nomeArquivo, indent=4, ensure_ascii=False)

    def excluirPessoa(self, pessoa):
        arvore, chave, caminho = self._chooseArvore(pessoa=pessoa)
        arvore.delete(chave)
        with open(f'{caminho}', 'r+', encoding='UTF-8') as nomeArquivo:
            listaPessoas = json.load(nomeArquivo)
            listaPessoas.pop(chave)
            nomeArquivo.seek(0)
            json.dump(listaPessoas, nomeArquivo, indent=4, ensure_ascii=False)

    def procurarPessoa(self, chave, tipo):
        arvore = self._chooseArvore(tipo=tipo)
        pessoa = arvore.search(chave)
        return pessoa.valor

    def _chooseType(self, caminho):
        arvore = self.arvorePessoasCPF if caminho == VACCPF else self.arvorePessoasBiometria
        tipoPessoa = PessoaCPF if caminho == VACCPF else PessoaBiometria
        lastAtt = 'cpf' if caminho == VACCPF else 'biometria'
        return arvore, tipoPessoa, lastAtt

    def _chooseArvore(self, tipo=None, pessoa=None):
        if tipo:
            arvore = self.arvorePessoasCPF if tipo == 'cpf' else self.arvorePessoasBiometria
            return arvore
        if pessoa:
            arvore = self.arvorePessoasCPF if pessoa.__class__.__name__ == 'PessoaCPF' else self.arvorePessoasBiometria
            chave = pessoa.cpf if arvore == self.arvorePessoasCPF else pessoa.biometria
            path = VACCPF if arvore == self.arvorePessoasCPF else VACBIO
            return arvore, chave, path

class Pessoa:

    def __init__(self, nome, idade, dose=0, vacina=None):
        self.nome = nome
        self.idade = idade
        self.dose = 0
        self.vacina = vacina

    def isVac(self):
        if self.dose == 2:
            return True
        return False

    @property
    def vacina(self):
        return self._vacina
    
    @vacina.setter
    def vacina(self, valor):
        if valor == None:
            self._vacinda = 'Não vacinada'
        else:
            self._vacina = valor


    def vacinar(self, vacina):
        self.dose += 1
        self.vacina = vacina

    def __repr__(self):
        return f'Nome:{self.nome}, idade: {self.idade}, dose: {self.dose}'

class PessoaCPF(Pessoa):

    def __init__(self, nome, idade, dose=0, vacina=0, cpf=0):
        super().__init__(nome, idade, dose, vacina)
        self.cpf = cpf

    def lineRegistry(self):
        return {'nome': self.nome, 'idade': self.idade, 'vacina': self.vacina, 'dose': self.dose, 'cpf': self.cpf}

class PessoaBiometria(Pessoa):
    def __init__(self, nome, idade, dose=0, vacina=0, biom=0):
        super().__init__(nome, idade, dose, vacina)
        self.biometria = biom

    def associarBiometria(self, biometria):
        self.biometria = biometria

    def lineRegistry(self):
        return {'nome': self.nome, 'idade': self.idade, 'vacina': self.vacina, 'dose': self.dose, 'biometria': self.biometria}

class GerenciadorBiometria():

    def __init__(self):
        self.arvoreBiometrias = AVL()
        self._carregarArvore()

    def cadastrarBiometria(self):
        biometria = Bio.criar('_')
        self.arvoreBiometrias.insert(biometria)
        return  biometria

    def compararBiometria(self, path):
        nome = nameFromPath(path)
        caminho = caminhoFromPath(path)
        biometriaBD = self._procurarBiometria(nome)
        if biometriaBD:
            biometriaTeste = Bio.leArquivo(nome, path=caminho)
            biometriaBD = Bio.leArquivo(biometriaBD.chave)
            arvoreTeste = self._carregarArvoreTeste(biometriaTeste)
            arvoreBD = self._carregarArvoreTeste(biometriaBD)
            return print(self._igual(arvoreBD.root, arvoreTeste.root))
        return print(False)

    def _pegarNomes(self):
        nomes = [".".join(f.split(".")[:-1]) for f in listdir(path=BIO) if f.endswith('.json')]
        return nomes

    def _carregarArvore(self):
        nomes = self._pegarNomes()
        self.arvoreBiometrias.inserirLista(nomes)

    def _carregarArvoreTeste(self, lista):
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

class GerenciadorVacina():

    def __init__(self):
        self.arvoreVacinas = AVL()
        self._carregarArvore()

    def _carregarArvore(self):
        try:
            with open(f'{VACI}', 'r', encoding='UTF-8') as nomeArquivo:
                listaVacinas = json.load(nomeArquivo)
                for k, v in listaVacinas:
                    if v['quantidade'] == 0:
                        continue
                    vacina = Vacina(v['fabricante'], v['lote'], v['quantidade'])
                    self.arvoreVacinas.insert(k, valor=vacina)
        except:
            with open(f'{VACI}', 'w', encoding='UTF-8') as nomeArquivo:
                data = {}
                json.dump(data, nomeArquivo, indent=4, ensure_ascii=False)
    
    def cadastrarVacina(self, vacina):
        self.arvoreVacinas.insert(vacina.lote, vacina)
        with open(f'{VACI}', 'r+', encoding='UTF-8') as nomeArquivo:
            listaVacinas = json.load(nomeArquivo)
            listaVacinas[f'{vacina.lote}'] = vacina.lineRegistry()
            nomeArquivo.seek(0)
            json.dump(listaVacinas, nomeArquivo, indent=4, ensure_ascii=False)

    def diminuirEstoque(self, lote):
        vacina = self.arvoreVacinas.search(lote)
        vacina.valor.quantidade -= 1
        if not vacina.temVacina():
            self.arvoreVacinas.delete(lote)
        with open(f'{VACI}', 'r+', encoding='UTF-8') as nomeArquivo:
            listaVacinas = json.load(nomeArquivo)
            vacina = listaVacinas['lote']
            vacina['quantidade'] -=1
            nomeArquivo.seek(0)
            json.dump(listaVacinas, nomeArquivo, indent=4, ensure_ascii=False)

class Vacina:

    def __init__(self, fab, lote, quantidade=0):
        self.fabricante = fab
        self.lote = lote
        self.quantidade = quantidade
    
    def temVacina(self):
        if self.quantidade == 0:
            return False
        return True

    @property
    def fabricantes(self):
        return self._fabricantes

    @property
    def lote(self):
        return self._lote

    @property
    def quantidade(self):
        return self._quantidade

    def lineRegistry(self):
        return {'fabricante': self.fabricante, 'lote': self.lote, 'quantidade': self.quantidade}

    def __repr__(self):
        return f'Fabricante: {self.fabricante}, quantidade: {self.quantidade}, lote: {self.lote}'

