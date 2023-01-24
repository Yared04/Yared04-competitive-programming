class Solution:
    def countSubstrings(self, s: str) -> int:
        self.count = 0
        def countPalindrome(left, right):
            while s[left] == s[right]:
                self.count += 1
                left -= 1
                right += 1
                if left < 0 or right > len(s) - 1:
                    return
        
        for i in range(len(s)):
            countPalindrome(i, i)
        
        for i in range(len(s)-1):
            countPalindrome(i, i+1)
        
        return self.count
                
