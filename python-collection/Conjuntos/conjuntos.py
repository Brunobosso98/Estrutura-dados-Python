# Coleçaõ de objetos que não possui itens repetidos
print (set([1, 2, 3, 1, 3, 4]))
print (set("Abacaxi"))
set(("palio", "gol", "civic", "civic"))
print ({"Python", "Java", "Python"})

# Acessando os dados "excluídos"
numeros = {1, 2, 3, 2}
numeros = list(numeros)
print(numeros[0])

carros = {"gol", "civic", "corsa", "gol"}
for carro in carros:
  print(carro)
