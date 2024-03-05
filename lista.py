
class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_nodo(self, nuevo_nodo):
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual

    def ordenar_alfabeticamente(self):
        actual = self.cabeza

        while actual:
            siguiente = actual.siguiente

            while siguiente:
                if actual < siguiente:
                    actual.dato, siguiente.dato = siguiente.dato, actual.dato
                    actual.objeto, siguiente.objeto = siguiente.objeto, actual.objeto

                siguiente = siguiente.siguiente  # Añadir esta línea para avanzar al siguiente nodo

            actual = actual.siguiente   

    def buscar_nodo(self, dato):
        actual = self.cabeza
        while actual:
            if actual.dato == dato:
                return actual
            actual = actual.siguiente
        return None


    def imprimir_lista(self):
        actual = self.cabeza
        while actual:
            print(f"Nombre: {actual.dato}, Datos del piso:{actual.objeto}")
            actual = actual.siguiente 