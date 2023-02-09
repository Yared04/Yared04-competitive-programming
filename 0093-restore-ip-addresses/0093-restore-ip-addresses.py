class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        def isValidIp(sequence):
            address = list(sequence.split('.'))
           
            for p in address:
                if int(p) > 255 or (len(p) > 1 and p[0] == '0'):
                    return False
            return True
                
        self.result = []
        def dp(s, dots, seq):
            if dots == 0 and len(s) == 0:
                if isValidIp(seq[:-1]):
                    self.result.append(seq[:-1])
                return
            if dots == 0 or len(s) == 0:
                return
            
            for i in range(3):
                if i+1 > len(s):
                    break
                dp(s[i+1:], dots-1, seq + s[:i+1]+'.')
                    
               
        dp(s, 4, '')
        return self.result
    
