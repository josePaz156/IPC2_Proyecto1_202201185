import xml.etree.ElementTree as ET



try:
    xml_file = open('pisos.xml')
    if xml_file.readable():
        xml_data = ET.fromstring(xml_file.read())
        lst_pisos = xml_data.findall('piso')
        for piso in lst_pisos:
            i=1
            print('piso '+ str(i))
            print(f'Filas: {piso.find('R').text}')
            print(f'Columnas: {piso.find('C').text}')
            print(f'Voltear: {piso.find('F').text}')
            print(f'Cambiar: {piso.find('S').text}')     
            print('')
            i=i+1
    else: 
        print(False)    
except Exception as err:    
    print("Error", err)
finally:
    xml_file.close()