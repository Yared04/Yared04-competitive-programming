class Solution:
    @lru_cache(None)
    def isPalindrome(self, left, right, sequence):
        if left >= right:
            return True
        if sequence[left] != sequence[right]:
            return False
        return self.isPalindrome(left+1, right-1, sequence)
    
    def divide(self, idx, seq, comb, res):
        if idx == len(seq):
            res.append(comb[:])
            return
        new_string = ""
        for i in range(idx, len(seq)):
            new_string += seq[i]
            if self.isPalindrome(0, len(new_string)-1, new_string):
                comb.append(new_string)
                self.divide(i + 1, seq, comb, res)
                comb.pop()
        
    
    
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.divide(0, s, [], res)
        return res
        

