class Animal:
  def __init__(self, nro_patas):
    self.nro_patas = nro_patas

  def __str__(self):
    return f"A {self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"   

class Mamifero(Animal):
  def __init__(self, cor_pelo, **kw):
    self.cor_pelo = cor_pelo
    super().__init__(**kw)

class Ave(Animal):
  def __init__(self, cor_bico, **kw):
    self.cor_bico = cor_bico
    super().__init__(**kw)

class Cachorro(Mamifero):
  pass

class Gato(Mamifero):
  pass

class Leao(Mamifero):
  pass

class FalarMixin:
  def falar(self):
    return "to falando pae"

class Ornitorrinco(Mamifero, Ave, FalarMixin):
  def __init__(self, cor_bico, cor_pelo, nro_patas):
#    print(Ornitorrinco.__mro__)
    super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)

gato = Gato(nro_patas=4, cor_pelo="Pretao")
print(gato)

ornitorrinco = Ornitorrinco(nro_patas=4, cor_pelo="Verde", cor_bico="Transparente")
print(ornitorrinco)
print(ornitorrinco.falar())
