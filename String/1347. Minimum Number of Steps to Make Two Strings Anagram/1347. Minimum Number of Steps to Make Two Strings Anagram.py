class Solution:
    def minSteps(self, s: str, t: str) -> int:
        scount = {}
        tcount = {}
        
        for i in s:
            if i in scount:
                scount[i] += 1
            else:
                scount[i] = 1
        for i in t:
            if i in tcount:
                tcount[i] += 1
            else:
                tcount[i] = 1
        steps = 0
        for i in scount:
            diff = scount.get(i, 0) - tcount.get(i, 0)
            if diff > 0:
                steps += diff
        return steps