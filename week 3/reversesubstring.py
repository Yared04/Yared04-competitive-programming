def reverseParentheses(s) -> str:
    stak1 = []
    brak = []
    for i in range(1,len(s)-1):
        for j in range(i+1,len(s)):
            if s[i] == "(" :
                while s[j] != ")":
                    stak1.append(s[j])
                    j += 1
                    
          
        

  
                 
    print(stak1)    
s = "ed(et(oc))el"

reverseParentheses(s)