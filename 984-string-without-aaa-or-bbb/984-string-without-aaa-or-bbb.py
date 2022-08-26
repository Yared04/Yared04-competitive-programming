class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        res = ''
        while a > 0 or b > 0:
            if a == b:
                res += "ab" * a
                return res
            else:
                    if a > b:
                        if a > 1:
                            res += "aa"
                            a -= 2
                        else: 
                            res += "a"
                            a -= 1
                        if b > 0:
                            res += "b"
                            b -= 1
                    elif a < b:
                        if b > 1:
                            res += "bb"
                            b -= 2
                        else: 
                            res += "b"
                            b -= 1
                        if a >0: 
                            res += "a"
                            a -= 1
        return res
                                
                
                
            
  
            
            