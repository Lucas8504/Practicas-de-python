from ManejoArchivos import ManejoDeArchivos
#with open("prueba.txt", "r", encoding="utf8") as archivo:

with ManejoDeArchivos("prueba.txt") as archivo:
    print(archivo.read())