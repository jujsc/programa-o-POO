class TrianguloRetangulo:
    def __init__(self):
        self._cat1 =0.0
        self._cat2 =0.0

    def set_cat1(self, cat1):
        if cat1 >0:
            self._cat1 = cat1
        else: 
            print("Cateto 1 dve ser maior que 0.")
    
    def set_cat2(self, cat2):
        if cat2 >0:
            self._cat2 = cat2
        else: 
            print("Cateto 2 dve ser maior que 0.")


    def area(self):
        return self._cat1 * self._cat2 /2

if __name__ == '__main__':
    cat1 = float(input("Informe o valor do cateto 1:"))
    cat2 = float(input("Informe o valor do cateto 2:"))
    tr = TrianguloRetangulo()
    tr.set_cat1(cat1)
    tr.set_cat2(cat2)
    area = tr.area()
    print('Área do triângulo: {:.3f}'.format(area))
