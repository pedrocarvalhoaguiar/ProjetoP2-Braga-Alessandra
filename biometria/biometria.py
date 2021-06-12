import random
import os
import json
from bancodedados.paths import BIO

class Biometria():

    @staticmethod
    def criar(nomeArquivo):
        lista = {}
        bio = [[random.randint(1, 256) for i in range(1, 255)] for x in range(1, 256)]
        with open(f'{BIO}{nomeArquivo}.json', 'w', encoding='UTF-8') as arquivo:
            for i, line in enumerate(bio, 1):
                lista[i] = line
            json.dump(lista, arquivo, indent=4)   
        resultado = Biometria.gerarCodigo(nomeArquivo)
        os.rename(f'{BIO}{nomeArquivo}.json', f'{BIO}{resultado}.json')
        return resultado      

    @staticmethod
    def leArquivo(nomeArquivo, path=BIO):
        caminho = path + nomeArquivo + '.json' if path != BIO else BIO + nomeArquivo + '.json'
        listaDeLinhas = []
        with open(f'{caminho}', 'r', encoding='UTF-8') as arquivo:
            listaDeLinhas = json.load(arquivo)
            listaLinhasSomadas = []
            for k in listaDeLinhas.keys():
                linha = listaDeLinhas[k]
                soma = sum(linha)
                listaLinhasSomadas.append(soma)  
        return set(listaLinhasSomadas)

    @staticmethod
    def gerarCodigo(nomeArquivo, path=BIO):
        listaLinhasSomadas = Biometria.leArquivo(nomeArquivo, path)
        valorLinhas = []
        for k in listaLinhasSomadas:
            valorLinhas.append(k)
        somaTotal = sum(valorLinhas)
        return somaTotal