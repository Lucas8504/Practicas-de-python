from excepciones.NumerosIgualesexcepcion import NumerosIgualesExcepcion

resultado = None
try:
    a = int(input("Primer numero: "))
    b = int(input("segundo numero: "))
    if a == b:
        raise NumerosIgualesExcepcion("Numeros iguales XD")
    resultado = a/b

except ZeroDivisionError as ze:
    print(f"Tenemos un error: {ze}")
except TypeError as te:
    print(f"Tenemos un error: {te}")
except Exception as e:
    print(f"Tenemos un error: {e}")

else:
    print("no hay error")
finally:
    print("yo soy el bloque finally y siempre me ejecuto")

print(f"Resultado = {resultado}")
print("cotinuamos...")