class TreeNode():
    
    def __init__(self, chave, valor=None):
        self.left = None
        self.right = None
        self.chave = chave
        self.valor = valor

    def getChave(self):
        return self.chave

    def getValor(self):
        return self.valor

    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right

    def isLeaf(self):
        if not self.left and not self.right:
            return True
        return False

    def __str__(self):
        return str(self.valor)

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        if self.left:
            yield from self.left
        yield self
        if self.right:
            yield from self.right