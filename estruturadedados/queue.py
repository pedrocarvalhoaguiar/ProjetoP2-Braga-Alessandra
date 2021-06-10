from .node import Node

class Queue():

    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def isEmpty(self):
        if self.size == 0:
            return True
        return False

    def push(self, value):
        if self.isEmpty():
            self.first = self.last = Node(value)
        else:
            newNode = Node(value)
            self.last.next = newNode
            self.last = newNode
        self.size += 1
    
    def pop(self):
        if self.isEmpty():
            raise ValueError('Fila vazia')
        else:
            pop = self.first.valor
            self.first = self.first.next
            self.size -= 1
            return pop

    def __str__(self):
        if self.isEmpty():
            raise ValueError('Fila vazia')
        else:
            s = ''
            aux = self.first
            while aux:
                s += f'{str(aux)}, '
                aux = aux.next
            return '[' + s[:-2] + ']'