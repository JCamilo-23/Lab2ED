class NodoCircular:
    def __init__(self, valor):
        self.valor = valor
        self.next = None

class ListaCircular:
    def __init__(self):
        self.ultimo = None
    
    def agregar(self, valor):
        nuevo = NodoCircular(valor)
        if not self.ultimo:
            self.ultimo = nuevo
            nuevo.next = nuevo
        else:
            nuevo.next = self.ultimo.next
            self.ultimo.next = nuevo
            self.ultimo = nuevo  

    def recorrer(self):
        if not self.ultimo:
            return  
        actual = self.ultimo.next
        inicio = actual  
        while True:
            yield actual.valor
            actual = actual.next
            if actual == inicio:  
                break

    