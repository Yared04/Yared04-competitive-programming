def runningMedian(a):
    min_heap =[]
    max_heap = []
    result = []
    for i in range(len(a)):
        if len(max_heap) < len(min_heap):
                heapq.heappush(min_heap, a[i])
                temp = heapq.heappop(min_heap)
                heapq.heappush(max_heap,-1*temp)
                result.append((min_heap[0]+(-1*max_heap[0]))/2)
        else:
            heapq.heappush(max_heap,-a[i])
            temp = heapq.heappop(max_heap)
            heapq.heappush(min_heap, -temp)
            result.append(min_heap[0]/1)
       
    return result
            