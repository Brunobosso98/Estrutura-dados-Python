# Chama o mesmo método, mas se comporta diferente em cada um

class Passaro:
  def voar(self):
    print("Voando")

class Pardal(Passaro):
  def voar(self):
    super().voar()

class Avestruz(Passaro):
  def voar(self):
    print("Avestruz não voa")

# FIXME: exemplo ruim do uso de herança para "ganhar" o método voar
class Aviao(Passaro):
  def voar(self):
    print("Avião decolando selocko")

def plano_voo(obj):
  obj.voar()

p1 = Pardal()
p2 = Avestruz()

plano_voo(p1)
plano_voo(p2)
plano_voo(Aviao())