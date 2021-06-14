from .treenode import TreeNode
from .queue import Queue

class AVL():
    
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, chave, node='root', valor=None):
        node = self.root if node == 'root' else node
        newNode1 = TreeNode(chave, valor)
        if self.isEmpty():
            self.root = newNode1
            node = self.root
            self.size +=1
        elif chave > node.chave:
            if node.right == None:
                node.right = newNode1
                self.size += 1
            else:
                self.insert(chave, node.right, valor)
        elif chave < node.chave:
            if node.left == None:
                node.left = newNode1
                self.size += 1
            else:
                self.insert(chave, node.left, valor)
        else:
            raise ValueError('chave já está na lista')
        self._checkBalance(node)        

    def inOrder(self, node='root', chave=False):
        node = self.root if node == 'root' else node
        if self.isEmpty():
            raise IndexError('Árvore vazia')
        if node.left:
            self.inOrder(node.left, chave)
        if chave:
            print(node.chave)
        else:
            print(node.valor)
        if node.right:
            self.inOrder(node.right, chave)

    def search(self, chave, node='root'):
        node = self.root if node == 'root' else node
        if self.isEmpty():
            raise IndexError('Árvore vazia')
        while node:
            if chave == node.chave:
                return node
            if chave < node.chave:
                node = node.left
            elif chave > node.chave:
                node = node.right
        raise ValueError('Node não está na árvore')

    def delete(self, chave, node='root'):
        root = False
        node = self.root if node == 'root' else node
        if node == self.root:
            root = True 
        if self.isEmpty():
            raise IndexError('Árvore vazia')
        elif node == None:
            raise ValueError('Node não está na árvore')
        elif chave < node.chave:
            node.left = self.delete(chave, node.left)
        elif chave > node.chave:
            node.right = self.delete(chave, node.right)
        elif node.chave == chave:
            if node.isLeaf():
                node = None
                self.size -= 1
            elif node.left == None:
                node = node.right
                if root:
                    self.root = node
                self.size -= 1
                return node
            elif node.right == None:
                node = node.left
                if root:
                    self.root = node
                self.size -= 1
                return node
            elif node.right and node.left:                
                nMax = self._getMax(node.left)
                node.chave = nMax.chave
                node.valor = nMax.valor
                node.left = self.delete(nMax.chave, node.left)
                if root:
                    self.root = node
                return node
        self._checkBalance(node)
        return node

    def inserirLista(self, lista):
        for i in lista:
            self.insert(i)

    def _checkBalance(self, node):
        bf = self._balanceFactor(node)
        if bf > 1 and self._balanceFactor(node.left) == 1:
            self._rightRotate(node)
            return
        if bf < -1 and self._balanceFactor(node.right) == -1:
            self._leftRotate(node)
            return
        if bf > 1 and self._balanceFactor(node.left) == -1:
            node.left = self._leftRotate(node.left, double=True)
            self._rightRotate(node)
            return
        if bf < -1 and self._balanceFactor(node.right) == 1:
            node.right = self._rightRotate(node.right, double=True)
            self._leftRotate(node)
            return 

    def _balanceFactor(self, node='root'):
        node = self.root if node == 'root' else node
        if node == None:
            return -1
        return (self._getHeight(node.left) - self._getHeight(node.right))

    def _leftRotate(self, node, double=False):
        root = False
        if node == self.root:
            root = True
        y = node
        alfa = node.left
        z = node.right
        beta = node.right.left
        omega = node.right.right
        newNode = TreeNode(z.chave, z.valor)
        newNode.right = omega
        newNode.left = y
        newNode.left.left = alfa
        newNode.left.right = beta
        if root:
            self.root = newNode
        elif not double:            
            newNode = self._balanceRotation(node, newNode)
            return
        return newNode

    def _rightRotate(self, node, double=False):
        root = False
        if node == self.root:
            root = True
        y = node.left
        if node.left == None:
            alfa = None
        else:
            alfa = node.left.left
        beta = node.left.right
        pi = node.right
        newNode = TreeNode(y.chave, y.valor)
        newNode.right = node
        newNode.right.right = pi
        newNode.right.left = beta
        newNode.left = alfa
        if root:
            self.root = newNode
        elif not double:            
            self._balanceRotation(node, newNode)
            return
        return newNode

    def _balanceRotation(self, node, newNode, root='root'):
        nodeAtual = self.root if root == 'root' else root
        chave = node.chave
        if chave == nodeAtual.right.chave:
            nodeAtual.right = newNode
            return
        elif chave == nodeAtual.left.chave:
            nodeAtual.left = newNode
            return
        elif newNode.chave > nodeAtual.chave:
            self._balanceRotation(node, newNode, nodeAtual.right)
        elif newNode.chave < nodeAtual.chave:
            self._balanceRotation(node, newNode, nodeAtual.left)

    def _getMin(self, node='root'):
        node = self.root if node == 'root' else node
        if node == None:
            raise ValueError('Nó inválido')
        while node:
            if node.left == None:
                return node
            node = node.left            

    def _getMax(self, node='root'):
        node = self.root if node == 'root' else node
        if node == None:
            raise ValueError('Nó inválido')
        while node:
            if node.right == None:
                return node
            node = node.right 

    def isEmpty(self):
        if self.root == None:
            return True
        return False

    def _getHeight(self, node='root'):
        node = self.root if node == 'root' else node
        if node == None:
            return -1
        left = self._getHeight(node.left)
        right = self._getHeight(node.right)
        return max(left, right) + 1

    def __iter__(self):
        if self.root.left:
            yield from self.root.left
        yield self.root
        if self.root.right:
            yield from self.root.right
