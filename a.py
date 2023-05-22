lista = [15, "nombre", 3.1415, True]
print("lista[0]")

usuario = ["usuarioTest1", "pass123","correo@correo.cl"]

numeros = [10,50,100,255,1000]
numeros.append(1000)
print(numeros)

extra=[75,350,999]
numeros.extend(extra)
print(numeros)

numeros.insert(6,5000)
print(numeros)

numeros.remove(50)
print(numeros)

numeros.pop()
print(numeros)
numeros.pop(3)
print(numeros)

numeros.reverse()
print(numeros)
