class Solution:
    def isValid(self, s: str) -> bool:
        opens = []
        if len(s) % 2 != 0:
            return False
        else:
            for i in range(len(s)):
                balanced = False
                try:
                    if s[i] == "(" or s[i]=="{" or s[i] =="[":
                        opens.append(s[i])
                    elif s[i] == ")" and opens[-1] == "(":
                        opens.pop()
                        balanced = True
                    elif s[i] == "]" and opens[-1] == "[":
                        opens.pop()
                        balanced= True
                    elif s[i] == "}" and opens[-1] == "{":
                        opens.pop()
                        balanced = True
                    else:
                        return False
                except:IndexError
        return len(opens) == 0 and balanced