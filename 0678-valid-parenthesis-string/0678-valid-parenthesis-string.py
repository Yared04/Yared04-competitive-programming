class Solution:
    def checkValidString(self, s: str) -> bool:
        op1 = 0
        op2 = 0
        for char in s:
            if char == '(':
                op1 += 1
                op2 += 1
            elif char == ')':
                op1 -= 1
                op2 = max(op2 - 1, 0)
            elif char == '*':
                op1 += 1
                op2 = max(op2 - 1, 0)
            if op1 < 0:
                return False
        return op2 == 0
                