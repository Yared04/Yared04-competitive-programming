def cookies(k, A):
    heapq.heapify(A)
    count = 0
    while A[0] < k and len(A) >= 2:
        a1 = heapq.heappop(A)
        a2 = heapq.heappop(A)
        b = a1 +(2*a2)
        heapq.heappush(A,b)
        count += 1
    if len(A) < 2 and A[0] < k:
        return -1
        
    return count
    