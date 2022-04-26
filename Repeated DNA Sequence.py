class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        pt1, pt2 = 0, 10
        answer = []
        freq = {}
        if len(s) < 10:
            return []
        while pt2 <= len(s):
            if s[pt1:pt2] in freq:
                freq[s[pt1:pt2]] += 1
                if freq[s[pt1:pt2]] == 2:
                    answer.append(s[pt1:pt2])
            else:
                freq[s[pt1:pt2]] = 1
            pt1 += 1
            pt2 += 1
        return answer
            
        
        
