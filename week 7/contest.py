t = int(input())

for i in range(t):
    s = input() 
    stack =[]
    for letter in s:
        if not stack:
            stack.append(letter)
        elif letter == stack[-1]:
            stack.pop()
        else:
            stack.append(letter)
    res = "".join(stack)
    res = sorted(res)
    res = "".join(res)
    print(res)

# n = input()
# new = n[::-1]
# output = int(n + new)
# print(output)
# n = input()
# one = 0
# other = 0
# for i in range(1,int(n)):

#     s = input()
#     if s == "1":
#         one += 1
#     else:
#         other += 1

# if one - other > 0 and one > 2:
#     print("YES")
# else:
#     print("NO")