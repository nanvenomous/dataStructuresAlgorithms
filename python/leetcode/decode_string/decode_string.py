import re
class DecodeString:
    def __init__(self):
        self.s = None

    def decodeString(self, s: str) -> str:
        self.s = s
        return self.decode_one_layer()

    def decode_one_layer(self):
        if '[' not in self.s: return self.s
        self.s = re.sub(r'[0-9]*\[[a-z]*\]', self.my_replacement, self.s)
        return self.decode_one_layer()

    @staticmethod
    def my_replacement(match):
        m = match.group(0)
        num = int(re.match(r'[0-9]*', m).group(0))
        expr = re.search(r'\[[a-z]*\]', m).group(0)
        lets = re.sub(r'[\[\]]', '', expr)
        return ''.join([lets for _ in range(num)])