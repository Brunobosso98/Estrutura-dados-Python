# Append
lista = []
lista.append("Python", "corno")
print(lista)

# Clear *limpa lista
# Copy *copia uma lista em outra variável 
copy = ['Aoba']
copy2 = copy.copy()
copy.append('Chama')
print (copy)
print (copy2)

# Count *retorna o numero de vezes que o objeto foi passado
# Extends
copy.extend(copy2)
print (copy)

# Index *retorna a posição do elemento
# Pop *retira o último elemento da lista
# Remove *igual o pop, porém utilizando string
# Reverse *espelha a lista
# Sort *ordena a lista
  #sort(reverse=True) *espelha a lista
  #sort(key=lambda x: len(x)) *ordena por quantia de caracteres
  #sort(key=lambda x: len(x), rever=True) *ordena por quantia de caracteres espelhada
# Len *ver quantia de elementos
# Sorted *igual o sort, mas é uma função