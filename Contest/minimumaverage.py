def minimumAverage(customers):
    # Write your code here
    h = []
    total_time = 0
    curr_time = 0
    customers.sort()
    curr_idx = 0
    while curr_idx < len(customers) or h:
        if not h:
            heapq.heappush(h,(customers[curr_idx][1],customers[curr_idx][0]))
            curr_time = customers[curr_idx][0]
            curr_idx += 1
        temp = heapq.heappop(h)
        arrival_time, order_time = temp[1], temp[0]
        waiting = curr_time + order_time - arrival_time
        total_time += waiting
        curr_time += order_time
        while curr_idx < len(customers) and customers[curr_idx][0] < curr_time:
            heapq.heappush(h,(customers[curr_idx][1],customers[curr_idx][0]))
            curr_idx += 1
        
    return total_time//len(customers)    
        