BIO = './bancodedados/biometrias/'
VACCPF = './bancodedados/pessoas/cpf/pessoas.json'
VACBIO = './bancodedados/pessoas/biometria/pessoas.json'
VACI = './bancodedados/vacinas/vacinas.json'
from os.path import basename
def nameFromPath(path):
    nomeArquivo = basename(path)
    nomeArquivo = nomeArquivo.replace('.json', '')
    return nomeArquivo

def caminhoFromPath(path):
    nome = nameFromPath(path)
    caminho = path.replace(f'{nome}.json', '')
    return caminho