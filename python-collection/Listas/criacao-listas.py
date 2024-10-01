frutas = ["Laranja", "Maça", "Uva"]
fruta = list("python")

# Fatiamento de lista
print(fruta[2:])
print(fruta[:2])
print(fruta[1:3])

print(fruta[0])
print(frutas)

# Listas aninhadas
matriz = [
  [1, "a", 2],
  ["b", 3, 4],
  [3, 5, "c"]
]

print (matriz[0][1])

# Iterar listas
carros = ["Gol", "Civic", "Opala"]

for carro in carros:
  print(carro)
  
# Função Enumerate
for indice, carro in enumerate(carros):
  print(f"{indice}: {carro}")

# Compreensão
numeros = [1, 30, 43, 54, 2, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
quadrado = [numero ** 2 for numero in numeros]
print(pares)
print(quadrado)