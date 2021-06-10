BIO = './bancodedados/biometrias/'
USU = './bancodedados/usuarios/'
VACCPF = './bancodedados/pessoas/cpf/'
VACBIO = './bancodedados/pessoas/biometria/'
VACI = './bancodedados/vacinas/'
from os.path import basename
def nameFromPath(path):
    nomeArquivo = basename(path)
    nomeArquivo = nomeArquivo.replace('.json', '')
    return nomeArquivo

def caminhoFromPath(path):
    nome = nameFromPath(path)
    caminho = path.replace(f'{nome}.json', '')
    return caminho