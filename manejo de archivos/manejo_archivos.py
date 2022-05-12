try:
    archivo = open("prueba.txt", "w", encoding="utf8")
    archivo.write("Agregamos info al archivo\n")
    archivo.write("Adios")
except Exception as e:
    print(e)
finally:
    archivo.close()
    print("fin del archivo") # ya no puede editar el archivo
    # arcivo.write("nueva info)
