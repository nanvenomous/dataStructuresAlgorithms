"""
"[([]{})]"

b : np
------
[ : 
( : [
[ : [(
] : [([
{ : [(
} : [({
) : [(
] : [

if b is closer
    if np and b matches end of np
        remove end of np
    else not np or matches end of np
        return false
else is opener
    add to np
return not np
"""

does_match = {'{': '}', '[': ']', '(': ')'}
class Solution:
    @staticmethod
    def _does_match(np, i): return i == does_match.get(np, '')

    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        np = []
        for b in s:
            if b in [']', ')', '}']:
                if np and Solution._does_match(np[-1], b):
                    np.pop()
                else: # np empty or not matching end
                    return False
            else: # is opener
                np.append(b)
        return not np


s = Solution()

assert s.isValid('[({[]})]')
assert not s.isValid('[({[(})]')
assert s.isValid('[([]{})]')
