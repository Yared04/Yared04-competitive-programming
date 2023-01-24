class Solution:
    def countSubstrings(self, s: str) -> int:
        self.count = 0
        def countPalindrome(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                self.count += 1
                left -= 1
                right += 1

        for i in range(len(s)):
            countPalindrome(i, i)
            countPalindrome(i, i+1)
        
        return self.count
                
