class TreeNode():
    
    def __init__(self, chave, valor=None):
        self.left = None
        self.right = None
        self.chave = chave
        self.valor = valor

    def isLeaf(self):
        if not self.left and not self.right:
            return True
        return False

    def __str__(self):
        return str(self.chave)

    def __repr__(self):
        return self.__str__()
