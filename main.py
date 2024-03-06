import xml.etree.ElementTree as ET
from piso import tipo_piso
from lista import ListaDoblementeEnlazada
from nodo import Nodo
from patrones import tipo_patrones
import graphviz

lista_pisos = ListaDoblementeEnlazada()
lista_pisos_comprados = ListaDoblementeEnlazada()

xml_file = None

while True:
    try:
        cargar_archivo = input("Ingrese la ruta del archivo: " )
        xml_file = open(cargar_archivo)
        break
    except FileNotFoundError as file_err:
        print(f"Error: El archivo {cargar_archivo} no se encuentra.")
        # Asignar un valor por defecto (puede ser None u otro valor que tenga sentido para tu aplicación)
        xml_file = None

try:
    if xml_file.readable():
        xml_data = ET.fromstring(xml_file.read())
        lst_pisos = xml_data.findall('piso')

        for piso in lst_pisos:
            nombrePiso = piso.get('nombre')

            # Obtener la lista de patrones
            lst_patrones = [tipo_patrones(patron.get('codigo'), patron.text.strip()) for patron in piso.findall('.//patrones/patron')]

            elemento = tipo_piso(
                R=int(piso.find('R').text.strip()),
                C=int(piso.find('C').text.strip()),
                F=int(piso.find('F').text.strip()),
                S=int(piso.find('S').text.strip()),
                patrones=lst_patrones  # Pasar la lista de patrones al constructor
            )

            nuevoNodo = Nodo(dato=nombrePiso, objeto=elemento)

            lista_pisos.agregar_nodo(nuevoNodo)
        lista_pisos.ordenar_alfabeticamente()
    else:
        print(False)
        print("No se encontro el archivo seleccionado intente nuevamente: ")

except Exception as err:
    print("Error", err)
finally:
    xml_file.close()

def imprimir_menu():
    print("Bienvenido a nuestra tienda PISOS DE GUATEMALA, selecciona la opcion que deceas")
    print("-------------------------------------------------------------------------------")
    print("Opcion 1: Comprar un piso")
    print("Opcion 2: Modificar piso")
    print("Opcion 3: Salir")

def comprar_piso(piso_seleccionado):

    # Buscar el piso seleccionado en la lista
    nodo_piso = lista_pisos.buscar_nodo(piso_seleccionado)

    if nodo_piso:
        # Mostrar detalles del piso seleccionado
        print(f"\nDetalles del Piso '{piso_seleccionado}':")
        print(f"Dimensiones: {nodo_piso.objeto.R}x{nodo_piso.objeto.C}")

         # Mostrar patrones disponibles
        print("Patrones Disponibles:")
        
        for patron in nodo_piso.objeto.patrones:
            print(f"  - Código: {patron.codigo}, Patron: {patron.contenido}")
        
        codigo_seleccionado = input("Ingrese el codigo del patron: ")
        patron_seleccionado = next((patron for patron in nodo_piso.objeto.patrones if patron.codigo == codigo_seleccionado), None)

        if patron_seleccionado:
            # Ahora, patron_seleccionado contiene el objeto tipo_patrones correspondiente
            mostrar_patron_grafico(nodo_piso, patron_seleccionado)
        else:
            print(f"No se encontró el patrón con código '{codigo_seleccionado}'. Inténtalo de nuevo.")

        agregar_piso_comprado(codigo_seleccionado, nodo_piso)

    else:
        print(f"No se encontró el piso '{piso_seleccionado}'. Inténtalo de nuevo.")
    

def mostrar_patron_grafico(piso_actual, patron_elegido):
    # Crear un gráfico Graphviz
    dot = graphviz.Digraph(comment='Patrón del Piso', format='png', graph_attr={'rankdir': 'TB'})

    # Obtener las dimensiones de la matriz RxC
    R = piso_actual.objeto.R
    C = piso_actual.objeto.C

    # Crear nodos para cada celda de la matriz
    for i in range(R):
        for j in range(C):
            # Obtener el valor de la celda (B o N) desde el patrón elegido
            valor_celda = patron_elegido.contenido[i * C + j]

            # Agregar nodo al gráfico
            dot.node(f'{i}_{j}', label='', shape='square', style='filled', fillcolor='white' if valor_celda == 'B' else 'black', pos=f'{j},{-i}')

            # Agregar conexiones entre nodos para formar la matriz
            if i > 0:  # Cambiando la condición a i > 0
                dot.edge(f'{i-1}_{j}', f'{i}_{j}')  # Conexión vertical


    # Guardar y visualizar el gráfico
    dot.render('patron_piso', format='png', cleanup=True)
    dot.view('patron_piso')

def agregar_piso_comprado(codigo_patron, piso_comprado):
    # Verifica que piso_comprado sea un objeto tipo_piso
    if isinstance(piso_comprado.objeto, tipo_piso):
        new_piso = Nodo(codigo_patron, piso_comprado)
        lista_pisos_comprados.agregar_nodo(new_piso)
        lista_pisos_comprados.ordenar_alfabeticamente()
    else:
        print("Error: El piso_comprado no contiene un objeto tipo_piso.")

def mostrar_piso_comprado():
    print("----------Detalles del piso----------")

    recorrer_lista = lista_pisos_comprados.cabeza

    while recorrer_lista:
        piso_actual = recorrer_lista.objeto
        print(f'Piso: {piso_actual.dato}')
        print(f'Dimensiones: {piso_actual.objeto.R}*{piso_actual.objeto.C}')
        print(f'Costo volteo: {piso_actual.objeto.F}')
        print(f'Costo intercambio: {piso_actual.objeto.S}')
        print(f'Patron elegido: {recorrer_lista.dato}')
        print("Patrones disponibles")
        for patron in piso_actual.objeto.patrones:
            print(f"  - Código: {patron.codigo}, Patron: {patron.contenido}")
        recorrer_lista = recorrer_lista.siguiente
        print('\n')


while True:

    imprimir_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        # Opción para mostrar la lista de pisos
        print("Lista de Pisos Disponibles:")
        actual = lista_pisos.cabeza
        while actual:
            print(f"  - {actual.dato}")
            actual = actual.siguiente

        # Pedir al usuario que seleccione un piso
        piso_seleccionado = input("Ingrese el nombre del piso que desea comprar: ")
        comprar_piso(piso_seleccionado)
        

    elif opcion == "2":
        
        if (lista_pisos_comprados.cabeza == None):
            print("No hay pisos comprados.")
        else:
            mostrar_piso_comprado()
            piso_editar = input("Ingrese el piso que desea editar: ")
            comprar_piso(piso_seleccionado)

    elif opcion == "3":
        print("Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Inténtalo de nuevo.")

