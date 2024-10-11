class Bicicleta:
  def __init__(self, cor, modelo, ano, valor, breke=True):
    self.cor = cor
    self.modelo = modelo
    self.ano = ano
    self.valor = valor
    self.breke = breke

  def buzinar(self):
    print("Buzinou")

  def parar(self):
    self.breke = False
    print("Bike parou")

  def pedalar(self):
    self.rodar = True
    print(f"A bicileta {self.modelo} está rodando!.")

  # def __str__(self):
  #   return f"Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}"

  def __str__(self):
    return f"A {self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"    

# Defino a bicicleta vendida
b1 = Bicicleta('Azul', "First", 2017, 900)
# Executo a função com base na b1
Bicicleta.buzinar(b1)
# Mostro a cor da b1
print(b1.cor)
# Mostro a bicicleta correta
print(b1)

Bicicleta.pedalar(b1)
