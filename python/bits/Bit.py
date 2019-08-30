class Bit:
  def __init__(self):
    pass

  def optimize_space(self, num):
    # print(int('00010111001', 2))
    binNum = bin(num)
    print(self._bit_len(binNum))
  
  def _bit_len(self, binary_number):
    return len(binary_number) - 2

b = Bit()
b.optimize_space(12)
b.optimize_space(31)