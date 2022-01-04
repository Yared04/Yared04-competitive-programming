
def replace( s: str):
        new = ""
        for i in range(len(s)):
            if s[i] == "0":
                new += s[i].replace("0", "01")
                print(new)
            elif s[i] == "1":
                new += s.replace("1","10")
                print(new)
                
        return new
# def kthGrammar( n: int, k: int) -> int:
#         if n == 0:
#             return "0"
#         else: 
#             return replace(kthGrammar(n-1, k))
        
        
print(replace("010"))   
