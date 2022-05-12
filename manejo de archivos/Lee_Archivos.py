archivo = open("prueba.txt", "r", encoding="utf8")
#print(archivo.read())

#leer algunos caracteres
#print(archivo.read(5))

#leer lineas completas
#print(archivo.readline())
#print(archivo.readline())

#iterar el archivo
#for linea in archivo:
#    print(linea)

# leer
#print(archivo.readlines())

# acceder a una lista de la linea
#print(archivo.readlines()[0])

# abrimos un archivo
# a - anexar imformacion
archivo2 = open("copia.txt", "a")
archivo2.write(archivo.read())

archivo.close()
archivo2.close()