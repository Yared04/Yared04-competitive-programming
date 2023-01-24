class Solution:
    def countSubstrings(self, s: str) -> int:
        self.count = 0
        #taking each letter of s as a center and expanding left and right to check if the resulting substring
        #is a palindrome as well
        def countPalindrome(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                self.count += 1
                left -= 1
                right += 1

        for i in range(len(s)):
            #We should consider even and odd length substrings, meaning I should start from a single letter
            #and from two consecutive letters as the center of a substring
            countPalindrome(i, i)
            countPalindrome(i, i+1)
        
        return self.count
                
