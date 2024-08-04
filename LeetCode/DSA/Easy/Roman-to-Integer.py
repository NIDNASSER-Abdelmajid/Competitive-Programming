class Solution:
    def romanToInt(self, s: str) -> int:
        R_to_I = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1,}
        if len(s) == 1:
            return R_to_I[s]
        else:
            c1 = R_to_I[s[0]]
            Int = 0
            for i in s[1:]:
                c2 = R_to_I[i]
                if c1 >= c2:
                    Int += c1
                else:
                    Int -= c1
                c1 = c2
            return Int + c2
