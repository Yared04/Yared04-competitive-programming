class Solution:
    def countSubstrings(self, s: str) -> int:
        
        #checking if the given substring is a palindrome or no by checking the inside of the substring
        @lru_cache(None)
        def isPalindrome(left, right):
            if left > right:
                return True
            if s[left] != s[right]:
                return False
            return isPalindrome(left + 1, right - 1)
        
        #checking every possible substring
        count = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if isPalindrome(i, j):
                    count += 1
                    
        return count        
           
                
