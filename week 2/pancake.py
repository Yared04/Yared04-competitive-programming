# def twoStacks(maxSum, a, b):
#     sum = 0
#     count = []
#     while sum < maxSum:
#         if a[0] > b[0]:
#             count.append(b.pop(0))
#             sum += count[-1]
            
#         elif a[0] < b[0]:
#             count.append(a.pop(0))
#             sum +=count[-1]
#     if sum > maxSum:
#         count.pop(-1)
#     return len(count)

# print(twoStacks(10,[4,2,4,6,1],[2,1,8,5]))