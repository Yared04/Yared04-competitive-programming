def evalRPN(tokens) -> int:
     stack = []
     for i in range(len(tokens)):
         if tokens[i] == "+":
             sum= int(stack.pop())+int( stack.pop())
             stack.append(sum)
         elif tokens[i] == "-":
             first =int(stack.pop())
             second =  int(stack.pop())
             dif= second - first
             stack.append(dif)
         elif tokens[i] == "*":
             prdct = int(stack.pop()) * int(stack.pop())
             stack.append(prdct)
         elif tokens[i] == "/":
             first =int(stack.pop())
             second =  int(stack.pop())
             div = second / first
             stack.append(div)
         else:
             stack.append(tokens[i])
     print(stack)
     return int(stack[0])
 
tokens =["0","3","/"]
print(evalRPN(tokens))