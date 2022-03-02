class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                heapq.heappush(heap, matrix[i][j])
        print(heap)
        for i in range(k):
            result = heapq.heappop(heap)
        return result
            
        