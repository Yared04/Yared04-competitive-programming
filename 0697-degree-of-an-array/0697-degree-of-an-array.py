class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = defaultdict(list)
        for i, n in enumerate(nums):
            count[n].append(i)        
        degree = max([len(x) for x in count.values()])
        
        result = len(nums)
        for indices in count.values():
            if len(indices) == degree:
                result = min(result, indices[-1] - indices[0])
        return result + 1           