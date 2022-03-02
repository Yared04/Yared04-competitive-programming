class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        h = [str(num[0])]
        for i in range(1, len(num)):
            while h and  h[-1] > num[i]  and k > 0:
                h.pop()
                k -= 1
            h.append(str(num[i]))
                
        for _ in range(k):
             h.pop()
        s = int("".join(h)) if h else "0"
        return str(s)
            
