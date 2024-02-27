import xml.etree.ElementTree as ET
from piso import tipo_piso
from lista import ListaDoblementeEnlazada
from nodo import Nodo
from patrones import tipo_patrones
import graphviz

lista_pisos = ListaDoblementeEnlazada()

cargar_archivo = input("Ingrese la ruta del archivo: " )

try:
    xml_file = open(cargar_archivo)
    if xml_file.readable():
        xml_data = ET.fromstring(xml_file.read())
        lst_pisos = xml_data.findall('piso')

        for piso in lst_pisos:
            nombrePiso = piso.get('nombre')

            # Obtener la lista de patrones
            lst_patrones = [patron.text.strip() for patron in piso.findall('.//patrones/patron')]

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
        lista_pisos.imprimir_lista()
    else:
        print(False)
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

while True:

    imprimir_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        # Opción para mostrar la lista de pisos
        lista_pisos.imprimir_lista()

    elif opcion == "2":
        # Otra acción que desees realizar
        print("Realizando otra acción...")

    elif opcion == "3":
        # Opción para salir del programa
        print("Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Inténtalo de nuevo.")

