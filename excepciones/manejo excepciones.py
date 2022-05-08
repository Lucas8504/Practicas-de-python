resultado = None
a = 10
b = 0

try:
   resultado = a/b
except Exception as e:
    print(f"Tenemos un error: {e}")

print(f"Resultado = {resultado}")
print("cotinuamos...")