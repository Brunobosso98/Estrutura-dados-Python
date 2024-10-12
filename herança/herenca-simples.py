class Veiculo:
  def __init__(self, cor, placa, numero_rodas):
    self.cor = cor
    self.placa = placa
    self.numero_rodas = numero_rodas

  def ligar_motor(self):
    print("Ligando o brabo")

  def __str__(self):
    return f"A {self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"   

class Motocicleta(Veiculo):
  pass

class Carro(Veiculo):
  pass

class Caminhao(Veiculo):
  def __init__(self, cor, placa, numero_rodas, carregado):
    super().__init__(cor, placa, numero_rodas)
    self.carregado = True

  def esta_carregado(self):
    print(f"{'Sim' if self.carregado else 'Nao'} estou carregado")

moto = Motocicleta("Preta", "HFG-4322", 2)
moto.ligar_motor()

carro = Carro("Branco", "HFG-4325", 4)
carro.ligar_motor()

caminhao = Caminhao("Roxo", "POF-5987", 8, False)
caminhao.ligar_motor()
caminhao.esta_carregado()

print(moto, carro, caminhao)