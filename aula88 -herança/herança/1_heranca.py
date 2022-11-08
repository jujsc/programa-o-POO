# Heranca

class Caixa:
  def set_altura(self, val):
    self._altura = val

  def set_largura(self, val):
    self._largura = val

  def get_altura(self):
    return self._altura

  def get_largura(self):
    return self._largura

class CaixaCor(Caixa):
  def set_cor(self, val):
    self._cor = val
  
  def get_cor(self):
    return self._cor

if __name__ == '__main__':
  caixaCor = CaixaCor()
  caixaCor.set_cor('Verde')
  caixaCor.set_altura(5)
  caixaCor.set_largura(7)

  print('Cor:', caixaCor.get_cor())
  print('Altura:', caixaCor.get_altura())
  print('Largura:', caixaCor.get_largura())