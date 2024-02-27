from lista import ListaDoblementeEnlazada

class Nodo:
    def __init__(self, dato, objeto):
        self.dato = dato
        self.objeto = objeto
        self.siguiente = None
        self.anterior = None
        self.lista_patrones = ListaDoblementeEnlazada()

    def __lt__(self, other):
        return self.dato < other.dato
    
    def __str__(self):
        return f"Dato: {self.dato}, Objeto: {self.objeto}"