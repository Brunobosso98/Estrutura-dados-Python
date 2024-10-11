# Método construtor: sempre é executado quando uma nova instância da classe é criada. Utilizar __init__
class Cachorro:
  def __init__(self, nome, cor, acordado=True):
    self.nome = nome
    self.cor = cor
    self.acordado = acordado

# Método destrutor: é executado quando uma instância é destruída, normalmente não necessário, __del__
class Cachorro:
  def __del__(self):
    print("Destruindo instância.")

c = Cachorro()
del c