class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = Counter(magazine)
        for letter in ransomNote:
            if letter in mag and mag[letter] > 0:
                mag[letter] -= 1
                continue
            else: return False
        return True
                
        
        