from estruturadedados.avltree import AVL
from estruturadedados.queue import Queue
from biometria.biometria import Biometria as Bio
from bancodedados.paths import *
import json
from os import listdir, remove

class GerenciadorPrincipal():
    
    def __init__(self):
        self.gerVacina = GerenciadorVacina()
        self.gerPessoas = GerenciadorPessoas()
        self.gerBiometria = GerenciadorBiometria()

    def cadastrarVacina(self, vacina):
        self.gerVacina.cadastrarVacina(vacina)

    def cadastrarPessoa(self, pessoa):
        self.gerPessoas.cadastrarPessoa(pessoa=pessoa)

    def retornarPessoa(self, chave, tipo):
        return self.gerPessoas.procurarPessoa(chave, tipo)

    def retornarBioNova(self):
        return self.gerBiometria.cadastrarBiometria()

    def vacinarPessoa(self, pessoa, vacina):
        self.gerPessoas.vacinarPessoa(pessoa, vacina)
        self.gerVacina.diminuirEstoque(vacina.getLote())

    def retornarVacinaValida(self, fab=None):
        vacina = self.gerVacina.getVacina(fab=fab)
        return vacina

    def retornarPessoaBio(self, path):
        nomeBio = self.gerBiometria.compararBiometria(path)
        if nomeBio:
            pessoaB = self.retornarPessoa(nomeBio, 'bio')
            return pessoaB
        return False

    def excluirCadastro(self, pessoa):
        self.gerPessoas.excluirPessoa(pessoa)
        try:
            self.gerBiometria.excluirBiometria(pessoa.getBiometria())
        except:
            pass

    def retornarArvoreVacinas(self):
        return self.gerVacina.arvoreVacinas

    def retornarArvoreCPF(self):
        return self.gerPessoas.arvorePessoasCPF

    def retornarArvoreBio(self):
        return self.gerPessoas.arvorePessoasBiometria

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
        pArvore.getValor().setDose(1) 
        pArvore.getValor().setVacina(vacina.fabricante)
        with open(f'{caminho}', 'r+', encoding='UTF-8') as nomeArquivo:
            listaPessoas = json.load(nomeArquivo)
            p = listaPessoas[chave]
            p['vacina'] = vacina.getFabricante()
            p['dose'] += 1
            nomeArquivo.seek(0)
            json.dump(listaPessoas, nomeArquivo, indent=4, ensure_ascii=False)

    def excluirPessoa(self, pessoa):
        arvore, chave, caminho = self._chooseArvore(pessoa=pessoa)
        arvore.delete(chave)
        with open(f'{caminho}', 'r+', encoding='UTF-8') as nomeArquivo:
            listaPessoas = json.load(nomeArquivo)
            listaPessoas.pop(chave)
        with open(f'{caminho}', 'w', encoding='UTF-8') as nomeArquivo:
            json.dump(listaPessoas, nomeArquivo, indent=4, ensure_ascii=False)

    def procurarPessoa(self, chave, tipo):
        arvore = self._chooseArvore(tipo=tipo)
        pessoa = arvore.search(chave)
        return pessoa.getValor()

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
            chave = pessoa.getCpf() if arvore == self.arvorePessoasCPF else pessoa.getBiometria()
            path = VACCPF if arvore == self.arvorePessoasCPF else VACBIO
            return arvore, chave, path

class Pessoa:

    def __init__(self, nome, idade, dose=0, vacina=None):
        self.nome = nome
        self.idade = idade
        self.dose = dose
        self.vacina = self.setVacina(vacina)

    def isVac(self):
        if self.dose > 1:
            return True
        return False

    def getNomeVacina(self):
        if self.vacina == 'N/A':
            return self.vacina
        return self.vacina

    def setVacina(self, valor):
        if valor == None:
            return 'N/A'
        else:
            return valor

    def getDose(self):
        return self.dose

    def setDose(self, valor):
        self.dose += valor

    def __repr__(self):
        return f'| NOME:{self.nome} \n| IDADE: {self.idade}\n| DOSE VACINA: {self.dose}'

class PessoaCPF(Pessoa):

    def __init__(self, nome, idade, dose=0, vacina=None, cpf=0):
        super().__init__(nome, idade, dose, vacina)
        self.cpf = cpf   

    def getCpf(self):
        return self.cpf

    def lineRegistry(self):
        return {'nome': self.nome, 'idade': self.idade, 'vacina': self.getNomeVacina(), 'dose': self.dose, 'cpf': self.cpf}

class PessoaBiometria(Pessoa):
    def __init__(self, nome, idade, dose=0, vacina=None, biom=0):
        super().__init__(nome, idade, dose, vacina)
        self.biometria = biom

    def getBiometria(self):
        return self.biometria

    def associarBiometria(self, biometria):
        self.biometria = biometria

    def lineRegistry(self):
        return {'nome': self.nome, 'idade': self.idade, 'vacina': self.getNomeVacina(), 'dose': self.dose, 'biometria': self.biometria}

class GerenciadorBiometria():

    def __init__(self):
        self.arvoreBiometrias = AVL()
        self._carregarArvore()

    def cadastrarBiometria(self):
        biometria = Bio.criar('_')
        self.arvoreBiometrias.insert(str(biometria))
        return biometria

    def compararBiometria(self, path):
        nome = nameFromPath(path)
        caminho = caminhoFromPath(path)
        biometriaBD = self._procurarBiometria(nome)
        if biometriaBD:
            biometriaTeste = Bio.leArquivo(nome, path=caminho)
            biometriaBD = Bio.leArquivo(biometriaBD.getChave())
            arvoreTeste = self._carregarArvoreTeste(biometriaTeste)
            arvoreBD = self._carregarArvoreTeste(biometriaBD)
            if self._igual(arvoreBD.getRoot(), arvoreTeste.getRoot()):
                return nome
        return False

    def _pegarNomes(self):
        nomes = [".".join(f.split(".")[:-1]) for f in listdir(path=BIO) if f.endswith('.json')]
        return nomes

    def excluirBiometria(self, nome):
        remove(f'{BIO}{nome}.json')
        self.arvoreBiometrias.delete(nome)

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
            if pos1.getChave() != pos2.getChave():
                return False
            fila1.pop()
            fila2.pop()
            count +=1
            if count > 40:
                return True
            if pos1.getLeft() and pos2.getLeft():
                fila1.push(pos1.getLeft())
                fila2.push(pos2.getLeft())
            elif pos1.getLeft() or pos2.getLeft():
                return False
            if pos1.getRight() and pos2.getRight():
                fila1.push(pos1.getRight())
                fila2.push(pos2.getRight())
            elif pos1.getRight() or pos2.getRight():
                return False
        return True

class GerenciadorVacina():

    def __init__(self):
        self.arvoreVacinas = AVL()
        self.estoque = 0
        self._carregarArvore()

    def _carregarArvore(self):
        try:
            with open(f'{VACI}', 'r', encoding='UTF-8') as nomeArquivo:
                listaVacinas = json.load(nomeArquivo)
                for k, v in listaVacinas.items():
                    if v['quantidade'] == 0:
                        continue
                    vacina = Vacina(v['fabricante'], v['lote'], v['quantidade'])
                    self.setEstoque(v['quantidade'])
                    self.arvoreVacinas.insert(k, valor=vacina)
        except:
            with open(f'{VACI}', 'w', encoding='UTF-8') as nomeArquivo:
                data = {}
                json.dump(data, nomeArquivo, indent=4, ensure_ascii=False)
    
    def cadastrarVacina(self, vacina):
        self.arvoreVacinas.insert(vacina.getLote(), valor=vacina)
        self.setEstoque(vacina.quantidade)
        with open(f'{VACI}', 'r+', encoding='UTF-8') as nomeArquivo:
            listaVacinas = json.load(nomeArquivo)
            listaVacinas[f'{vacina.getLote()}'] = vacina.lineRegistry()
            nomeArquivo.seek(0)
            json.dump(listaVacinas, nomeArquivo, indent=4, ensure_ascii=False)

    def diminuirEstoque(self, lote):
        vacina = self.arvoreVacinas.search(lote)
        vacina.getValor().setQuantidade(1)
        self.setEstoque(1)
        if not vacina.valor.temVacina():
            self.arvoreVacinas.delete(lote)
        with open(f'{VACI}', 'r+', encoding='UTF-8') as nomeArquivo:
            listaVacinas = json.load(nomeArquivo)
            vacina = listaVacinas[lote]
            vacina['quantidade'] -= 1
            nomeArquivo.seek(0)
            json.dump(listaVacinas, nomeArquivo, indent=4, ensure_ascii=False)

    def getVacina(self, fab=None):
        if self.arvoreVacinas.isEmpty():
            return None
        if fab == 'N/A':
            return self.arvoreVacinas.getRoot().getValor()
        for node in self.arvoreVacinas:            
            if node.getValor().getFabricante() == fab and node.getValor().temVacina():
                return node.getValor()

    def retornarEstoque(self):
        return self.estoque

    def setEstoque(self, qnt):
        if qnt > 0:
            self.estoque += qnt
        elif qnt < 0:
            self.estoque -= qnt
        else:
            self.estoque = 0

class Vacina:

    def __init__(self, fab, lote, quantidade=0):
        self.fabricante = fab
        self.lote = lote
        self.quantidade = quantidade
    
    def setQuantidade(self, qnt):
        if qnt > 0:
            self.quantidade += qnt
        elif qnt < 0:
            self.quantidade -= qnt
        else:
            self.quantidade = 0

    def temVacina(self):
        if self.quantidade == 0:
            return False
        return True

    def getLote(self):
        return self.lote

    def getFabricante(self):
        return self.fabricante

    def lineRegistry(self):
        return {'fabricante': self.fabricante, 'lote': self.lote, 'quantidade': self.quantidade}

    def __repr__(self):
        return f'| Fabricante: {self.fabricante}\n| quantidade: {self.quantidade}\n| lote: {self.lote}'

