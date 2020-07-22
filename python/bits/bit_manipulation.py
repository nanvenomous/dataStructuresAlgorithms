
class Bit:
    def __init__(self, num):
        self.num = num
        self.bin = bin(num)

    def is_set(self, n):
        check = 1 << n
        return bool(self.num & check)