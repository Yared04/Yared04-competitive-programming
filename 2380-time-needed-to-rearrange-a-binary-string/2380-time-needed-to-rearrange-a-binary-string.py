class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        time=0
        pt = 0
        for i in range(len(s)):
            if s[i]=="1":
                if i != pt :
                    time = max(time+1 ,i-pt)
                pt += 1
        
        return time