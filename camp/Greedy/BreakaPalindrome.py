class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        answer = ""
        wordLength = len(palindrome)
        for i in range(wordLength):
            if wordLength % 2 == 1 and i == wordLength // 2:
               continue
            if palindrome[i]  != "a" and i < len(palindrome):
                answer = palindrome[:i] + "a" + palindrome[i+1:]
                break
            else:
                answer = palindrome[:wordLength-1] + "b"
        return answer
                