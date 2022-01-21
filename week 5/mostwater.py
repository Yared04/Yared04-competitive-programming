class Solution:
    def maxArea(self, height: List[int]) -> int:
        max = [0]
        i = 0
        j = len(height) - 1
        while True:
            if i == j:
                break
            else:
                if height[i] <= height[j]:
                    k = height[i]  * (j - i) 
                    if k >= max[0]:            
                        max[0] = k
                    i += 1
               
                elif height[i] > height[j]:
                    k = height[j]  * (j - i) 
                    if k >= max[0]:            
                        max[0] = k
                    j -= 1
        return max[0]


       
        