class Solution:
    def compress(self, chars: List[str]) -> int:
        pt1 = 0
        pt2 = 1
        temp = []
        while  pt1 < len(chars) or pt2 < len(chars):
            cnt = 0
            while pt2 < len(chars) and chars[pt1] == chars[pt2]:
                pt2 += 1
            # temp += [pt1]
            cnt += pt2 - pt1
            if cnt > 1:
                count = []
                for i in str(cnt):
                    count.append(i)                      
                
                temp += chars[pt1:pt1+1] + count 
            else:
                temp += chars[pt1] 
            pt1 = pt2
            pt2 = pt1+1
        chars[:] = temp
            
        return len(chars)
