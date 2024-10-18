from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):
  @abstractmethod
  def ligar(self):
    pass

  @abstractmethod
  def desligar(self):
    pass

  @property
  @abstractproperty
  def marca(self):
    pass

class ControleTV(ControleRemoto):
  def ligar(self):
    print("Ligando TV")
  
  def desligar(self):
    print("Desligando TV")

  @property
  def marca(self):
    print("Samsung")

class ControleAr(ControleRemoto):
  def ligar(self):
    print("Ligando o ar")
  
  def desligar(self):
    print("Desligando o ar")

  @property
  def marca(self):
    print("Samsung")

controle = ControleTV()
controle.ligar()
controle.desligar()

controle = ControleAr()
controle.ligar()