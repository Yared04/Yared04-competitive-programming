class Solution:
    def isPalindrome(self, sequence):
        left = 0
        right = len(sequence) - 1
        while left < right:
            if sequence[left] != sequence[right]:
                return False
            left += 1
            right -= 1
        return True
    def divide(self, idx, seq, comb, res):
        if idx == len(seq):
            res.append(comb[:])
            return
        new_string = ""
        for i in range(idx, len(seq)):
            new_string += seq[i]
            if self.isPalindrome(new_string):
                comb.append(new_string)
                self.divide(i + 1, seq, comb, res)
                comb.pop()
        
    
    
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.divide(0, s, [], res)
        return res
        

