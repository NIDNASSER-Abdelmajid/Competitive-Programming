import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        _s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
        n = len(_s)
        if n == 1:
            return True
        elif n == 0:
            return True
        else:
            print(_s)
            p1, p2 = 0, n-1
            while p2 - p1 > 0:
                if _s[p1] != _s[p2]:
                    return False
                p1 += 1
                p2 -= 1   
            return True