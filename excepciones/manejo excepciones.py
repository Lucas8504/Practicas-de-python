resultado = None
try:
    a = int(input("Primer numero: "))
    b = int(input("segundo numero: "))
    resultado = a/b

except ZeroDivisionError as ze:
    print(f"Tenemos un error: {ze}")
except TypeError as te:
    print(f"Tenemos un error: {te}")
except Exception as e:
    print(f"Tenemos un error: {e}")

print(f"Resultado = {resultado}")
print("cotinuamos...")