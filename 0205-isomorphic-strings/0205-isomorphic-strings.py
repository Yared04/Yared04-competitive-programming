class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_freq = {}
        t_freq = {}
        for idx,c in enumerate(s):
            if c in s_freq:
                s_freq[c].append(idx)
            else:
                s_freq[c] = [idx]
        for idx,c in enumerate(t):
            if c in t_freq:
                t_freq[c].append(idx)
            else:
                t_freq[c] = [idx]
        print(s_freq, t_freq)
        ss = list(s_freq.values())
        ss.sort(key=len)
        tt = list(t_freq.values())
        tt.sort(key=len)
        if ss == tt:
            return True
        return False