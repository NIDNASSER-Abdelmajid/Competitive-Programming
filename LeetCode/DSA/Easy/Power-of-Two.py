class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        k = 1
        while n >= k:
            if k == n:
                return True
            k *= 2
        return False