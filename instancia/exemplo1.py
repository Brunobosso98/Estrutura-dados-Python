class Estudante:
  escola = "DIO"

  def __init__(self, nome, numero):
    self.nome = nome
    self.numero = numero

  def __str__(self):
    return f"{self.nome} ({self.numero}) - {self.escola}"

def mostrar_valores(*objs):
  for obj in objs:
    print(obj)

bruno = Estudante("Bru", 56879)
julia = Estudante("Ju", 22546)

mostrar_valores(bruno, julia)
Estudante.escola = "Anglao"
julia.numero = 2
mostrar_valores(bruno, julia)
