# class Pessoa:
#   def __init__(self, nome=None, idade=None):
#     self.nome = nome
#     self.idade = idade

#   def criar_data_nascimento(self, ano, mes, dia, nome):
#     idade = 2022 - ano
#     return Pessoa(nome, idade)

# p = Pessoa("Gui", 28)
# print(p.nome, p.idade)

# p = Pessoa(),criar_data_nascimento(2001, 11, 23, "Bruno")
# print(p2.nome, p2.idade)

class Pessoa:
  def __init__(self, nome=None, idade=None):
    self.nome = nome
    self.idade = idade

  @classmethod
  def criar_data_nascimento(cls, ano, mes, dia, nome):
    idade = 2022 - ano
    return cls(nome, idade)

  @staticmethod
  def maior_idade(idade):
    return idade >= 18

p = Pessoa.criar_data_nascimento(2001, 11, 23, "Bruno")
print(p.nome, p.idade)

print(Pessoa.maior_idade(17))
print(Pessoa.maior_idade(28))