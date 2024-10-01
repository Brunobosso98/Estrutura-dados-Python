# Union(), une dois elementos
a = {1 ,2}
b = {3 ,4}
print(a.union(b))

# Intersection(), retorna o elemento igual
a1 = {1 ,2}
b1 = {2 ,3}
print(a1.intersection(b1))

# Difference(), retorna o que não esta no outro elemento
a2 = {1 ,2, 4}
b2 = {2 ,3, 6}
print(a2.difference(b2))

# Symmetruc_differente(), retorna os elementos não incluidos nas duas variáveis
a3 = {1 ,2, 4}
b3 = {2 ,3, 6}
print(a3.symmetric_difference(b3))

# Issubset(), retorna um valor booleano (truthy se o elemento estiver inteiro dentro do outro)
a4 = {1 ,2, 4}
b4 = {1 ,2, 4, 6}
print(a4.issubset(b4))
print(b4.issubset(a4))

# Issuperset(), o contrário de Issubset()
a5 = {1 ,2, 4}
b5 = {1 ,2, 4, 6}
print(a5.issuperset(b5))
print(b5.issuperset(a5))

# isdisjoint(), retorna um valor booleano (truthy se algum elemento estiver nas duas variáveis)
a6 = {1 ,2, 3, 4, 5}
b6 = {6 ,7, 8, 9}
c6 = {1 ,0}
print(a6.isdisjoint(b6))
print(a6.isdisjoint(c6))

# add(), adiciona e não repete
sorteio = {1, 23}

sorteio.add(25)
sorteio.add(23)
print(sorteio)

# Clear()
# Copy()
# Discard(), descarta algum valor especifico
# Pop (), retira o primeiro valor
# Remove(), igual discard, mas não retorna o valor removido e da erro ao tentar remover algo inexistente
# len(), retorna o tamanho do conjunto

# in(), verifica se algum valor está dentro do elemento
numeros1 = {1, 2, 3, 4, 5, 6, 7, 8}
print(1 in numeros1)
print(9 in numeros1)