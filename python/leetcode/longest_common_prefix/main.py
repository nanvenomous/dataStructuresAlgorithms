"""
1. how do I as a person solve the problem
2. what sub problems are difficult, solve those first
3. write the code
"""

from typing import List
"""
s      : com_prefix
-------------------
flower : flower
flow   : flow
flight : fl

return com_prefix
"""

strs = ['flower', 'flow', 'flight']

class Solution:
    @staticmethod
    def _common_prefix(com_prefix, s):
        while com_prefix:
            if s.startswith(com_prefix):
                return com_prefix
            com_prefix = com_prefix[:len(com_prefix) - 1]

    def longestCommonPrefix(self, strs: List[str]) -> str:
        com_prefix = strs[0]
        for s in strs:
            Solution._common_prefix(com_prefix, s)
        return com_prefix

s = Solution()
answer = s.longestCommonPrefix(strs)
print(answer)
