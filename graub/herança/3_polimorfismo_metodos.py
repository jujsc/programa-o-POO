# Polimorfismo por Sobrecarga de Método

class A:
  def f1(self):
    print('A.f1()')

  def f2(self):
    print('A.f2()')

class B(A):
  # Sobrescrita do método f1 de A
  def f1(self, val=None):
    if val:  
      print('B.f(', val, ')')
    else:
      # Executa f1 da superclasse
      super().f1()

if __name__ == '__main__':
  b = B()
  b.f1(10)
  b.f1()
  b.f2()