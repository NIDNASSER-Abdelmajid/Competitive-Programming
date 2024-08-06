class Solution:
    def minimumPushes(self, word: str) -> int:
        chr = {}
        for i in word:
            if i in chr:
                chr[i] += 1
            else:
                chr[i] = 1

        kp = {}
        counter, pushes = 8, 1
        sorted_dict = dict(sorted(chr.items(), key=lambda x:x[1], reverse=True))

        for i in sorted_dict:
            if counter == 0:
                counter = 8
                pushes += 1
            kp[i] = [pushes, chr[i]]
            counter -= 1

        return sum([kp[ch][0] * kp[ch][1] for ch in kp])

