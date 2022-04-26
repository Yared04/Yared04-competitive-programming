import heapq
t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    heap1 = []
    for i in range(len(a)):
        heapq.heappush(heap1, (a[i],b[i]))
    while heap1:
        current = heapq.heappop(heap1)
        if current[0] <= k:
            k += current[1]
        else:
            break
    print(k)
        