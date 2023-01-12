#User function Template for python3
from collections import defaultdict, deque
class Solution:
    def topSort(self, graph, queue, indegree):
        order = []
        while queue:
            cur = queue.popleft()
            order.append(cur)
            for neighbor in graph[cur]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return order
        
    def findOrder(self,dict, N, K):
        len_d = len(dict)
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for word in dict:
            for letter in word:
                indegree[letter] = 0
        
        for i in range(len_d - 1):
            s = dict[i]
            t = dict[i + 1]
            j = 0 
            while j < min(len(s), len(t)) and s[j] == t[j]:
                j += 1
            if j < min(len(s), len(t)):
                graph[s[j]].append(t[j])
                indegree[t[j]] += 1
                
                
        q = deque([])
        for letter in indegree:
            if indegree[letter] == 0:
                q.append(letter)
           
        ans = self.topSort(graph, q, indegree)
        return "".join(ans)
        
        
       

#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends