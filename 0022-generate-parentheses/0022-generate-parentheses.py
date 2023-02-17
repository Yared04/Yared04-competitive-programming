class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parentheses = []
        
        def backtrack(comb, left, right):
            if len(comb) == 2*n:
                parentheses.append("".join(comb))
            
            if left < n:
                comb.append("(")
                backtrack(comb, left+1, right)
                comb.pop()
                
            if right < left:
                comb.append(")")
                backtrack(comb, left, right+1)
                comb.pop()
        
        backtrack([], 0, 0)
        return parentheses