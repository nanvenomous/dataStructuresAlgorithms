class ComplexNumber:
  def __init__(self, r, i):
    self.real = r
    self.imag = i

  def getData(self):
    print("{0}+{1}j".format(self.real,self.imag))
  
  def printRealPart(self):
    print(self.real)

comNum = ComplexNumber(1, 3)
comNum.printRealPart()