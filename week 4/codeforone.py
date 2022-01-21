def codeForOne(n, l, r ):
    new = []
    m = [n]
    while True:
        for num in m :
            if num != 0 and num != 1:
                new.append(num//2)
                new.append(num%2)
                new.append(num//2)
            elif num == 0 or num ==1:
                new.append(num)
        m = new.copy()
        # print(m)
        new = []
        count = 0
        for num in m:
             if  num == 0 or num ==1:
                count += 1
        if count == len(m):
             break
    ctr =0 
    for num in  m[l-1:r]:
        if num == 1:
            ctr += 1
    return ctr
         
       
   
    
        
print(codeForOne(10,3,10))
def code1(n,l,r):
    if n == 1:
        return [1]
    elif n == 0: 
        return [0]
    else:
        ans = []
        ans = code(n//2, l, r)
        if n % 2 == 0:
            return ( ans+ [0] + ans)
        elif n % 2 == 1:
            return (ans + [1] + ans)
        
def code(n,l,r):
    if n == 1:
        return 1
    elif n == 0: 
        return 0
    else:
        if n % 2 == 0:
            return 2 * code(n//2, l, r)
        elif n % 2 == 1:
            return 2 * code(n//2, l, r) + 1
print(code(10,3,2))