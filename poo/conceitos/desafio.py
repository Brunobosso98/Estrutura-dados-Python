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
    print("Bora de pedal")

  # def __str__(self):
  #   return f"Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}"

  def __str__(self):
    return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"    

b1 = Bicicleta('Azul', "First", 2017, 900)
Bicicleta.buzinar(b1)
print(b1.cor)
print(b1)