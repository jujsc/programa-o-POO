# Construtor e Destrutor

class Primeira:
  def __init__(self, id):
    self._id = id
    print('Construtor Primeira - id:', self._id)

  def __del__(self):
      print('Destrutor Primeira - id:', self._id)

  def get_id(self):
    return self._id

class Segunda(Primeira):
  def __init__(self, id, nr):
    super().__init__(id)
    self._nr = nr
    print('Construtor Segunda - id:', self.get_id(), '- nr:', self._nr)

  def __del__(self):
    print('Destrutor Segunda - id:', self.get_id(), '- nr:', self._nr)
    super().__del__()

if __name__ == '__main__':
  p = Primeira(1)
  s = Segunda(2, 3)
  del p
  del s