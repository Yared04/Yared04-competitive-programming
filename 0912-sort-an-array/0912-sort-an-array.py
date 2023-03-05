class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heap = []
        for num in nums:
            heappush(heap, num)
        ans = []
        while heap:
            ans.append(heappop(heap))
        return ans
        
      
        