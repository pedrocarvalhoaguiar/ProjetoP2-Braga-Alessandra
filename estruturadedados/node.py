class Node():
    
    def __init__(self, value):
        self.valor = value
        self.next = None

    def __str__(self):
        return str(self.valor)