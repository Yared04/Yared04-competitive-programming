class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        n = len(nums)
        bucket = [[] for _ in range(n+1)]
        
        for key, val in freq.items():
            bucket[val].append(key)

        answer = []
        while k > 0:
            if bucket[n]:
                for num in bucket[n]:
                    answer.append(num)
                    k -= 1
                    if k == 0:
                        return answer
            n -= 1
            
            
            
        