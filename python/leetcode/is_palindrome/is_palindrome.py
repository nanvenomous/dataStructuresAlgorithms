import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        if x == 0: return True
        len_n = int(math.log10(x) + 1)
        il = int(len_n/2) - 1
        while il >= 0:
            iu = len_n - il - 1
            if x//10**iu%10 != x//10**il%10: return False
            il -= 1
        return True
