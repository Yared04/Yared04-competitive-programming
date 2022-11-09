class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        answer = set()
        def helper(idx, new_string):
            if idx == len(s):
                answer.add(new_string)
                return
            ns = None
            if 64 < ord(s[idx]) < 97:
                ns = new_string[:idx] + chr(ord(new_string[idx]) + 32) + new_string[idx+1:]
            elif ord(new_string[idx]) > 96:
                ns = new_string[:idx] + chr(ord(s[idx]) - 32) + new_string[idx+1:]
            if ns:
                helper(idx + 1, ns)
            helper(idx + 1, new_string)
        
        helper(0, s)
        return list(answer)
            