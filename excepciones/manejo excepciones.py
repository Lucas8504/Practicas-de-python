resultado = None
a = "10"
b = 0

try:
   resultado = a/b
except ZeroDivisionError as ze:
    print(f"Tenemos un error: {ze}")
except TypeError as te:
    print(f"Tenemos un error: {te}")

print(f"Resultado = {resultado}")
print("cotinuamos...")