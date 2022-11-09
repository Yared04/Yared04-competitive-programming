class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        answer = []
        def helper(idx, new_string):
            if idx == len(s):
                answer.append(new_string)
                return
            if s[idx].isalpha():
                helper(idx + 1, new_string + s[idx].lower())
            helper(idx + 1, new_string + s[idx].upper())
        
        helper(0, '')
        return answer
            