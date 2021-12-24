def isValid(str):
    opens = []
    if len(str) % 2 != 0:
        return False
    else:
        for i in range(len(str)):
            balanced = False
            try:
                if str[i] == "(" or str[i]=="{" or str[i] =="[":
                    opens.append(str[i])
                elif str[i] == ")" and opens[-1] == "(":
                    opens.pop()
                    balanced = True
                elif str[i] == "]" and opens[-1] == "[":
                    opens.pop()
                    balanced = True
                elif str[i] == "}" and opens[-1] == "{":
                    opens.pop()
                    balanced = True
                else:
                    return False
            except: IndexError
            
    print(opens)
    return len(opens) == 0 and balanced
    
s = "))"
print(isValid(s))