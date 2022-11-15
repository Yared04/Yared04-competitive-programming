class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        i = 0
        answer = []
        for x, y in points:
            heappush(distance, ((x*x + y*y), i))
            i += 1
        while k > 0:
            _, idx = heappop(distance)
            answer.append(points[idx])
            k -= 1
        return answer
                      
        
