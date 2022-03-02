class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        max_heap = []
        idx = 0
        for i in range(1, len(heights)):
            if heights[i] <= heights[idx]:
                idx += 1
            elif heights[i] > heights[idx]:
                dif = heights[i] - heights[idx]
                if dif <= bricks:
                    heapq.heappush(max_heap, -(dif))
                    bricks = bricks - dif
                    idx += 1
                elif ladders > 0:
                    if max_heap and -max_heap[0] > dif:
                        popped = heapq.heappop(max_heap)
                        heappush(max_heap, -dif)
                        bricks += -popped - dif
                        idx += 1
                        ladders -= 1
                    else:               
                        ladders -= 1
                        idx += 1
                else:
                    return idx
           
        return len(heights)-1
