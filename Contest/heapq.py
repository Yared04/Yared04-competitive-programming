import heapq
q = int(input())
arr = []
to_delete ={}
for i in range(q):
    a = input()
    b = a.split()
    if b[0] == "1":
        heapq.heappush(arr,int(b[1]))
    elif b[0] == "3":
        while arr[0] in to_delete and to_delete[arr[0]] > 0:
            to_delete[heapq.heappop(arr)] -= 1
        print(arr[0])
    elif b[0] == "2":
        if arr[0] == int(b[1]):
            heapq.heappop(arr)
        else:
            if int(b[1]) in to_delete:
                to_delete[int(b[1])] += 1
            else:
                to_delete[int(b[1])] = 1