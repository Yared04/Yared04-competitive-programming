class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(seq):
            return seq == seq[::-1]
        
        i, j = 0, len(s)-1
        while i < len(s) and s[i] == s[j]:
            i += 1
            j -= 1
        
        return checkPalindrome(s[i:j]) or checkPalindrome(s[i+1: j+1])
     