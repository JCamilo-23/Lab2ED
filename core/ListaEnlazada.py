class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.next = None

class ListaEnlazada:
    def __init__(self):
        self.head = None

    def agregar(self, valor):
        nuevo = Nodo(valor)
        if not self.head:
            self.head = nuevo
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo

    def recorrer(self):
        actual = self.head
        while actual:
            yield actual.valor
            actual = actual.next
    
    def obtener(self, posicion):
        actual = self.head  # Cambio realizado aquí
        indice = 0
        while actual:
            if indice == posicion:
                return actual.valor
            actual = actual.next
            indice += 1
        return None

    