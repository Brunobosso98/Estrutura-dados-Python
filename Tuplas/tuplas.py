# Tuplas são imutáveis, listas não
# Ao declarar tuplas igual uma lista, utilizar "," no final.
frutas = ("laranja", "pera", "uva,")
print (frutas[0])

letra = tuple("python")

numeros = tuple([1, 2, 3, 4])

pais = ("Brasil",)

matriz = (
  (1, "a", 2),
  ("b", 3, 4),
  (3, 5, "c")
)

print (matriz[0][1])
