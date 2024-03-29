class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            if s[i] == ")":
                temp = []
                while stack[-1] != "(":
                    temp.append(stack.pop())
                stack.pop()
                stack.extend(temp)
                i += 1
            else:
                stack.append(s[i])
                i += 1
        return "".join(stack)