class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        words = set(wordList + [beginWord])
        dict = defaultdict(set)
        for s in wordList + [beginWord]:
            for i in range(len(s)):
                p1,p2 = s[0:i],s[i+1:]
                for a in alphabet:
                    temp = p1 + a + p2
                    if temp in words and temp != s:
                        dict[s].add(temp)
        print(dict)
        visited = set()
        q = collections.deque([(beginWord,1)])
        while q:
            current, step = q.popleft()
            visited.add(current)
            if current == endWord:
                return step
            for word in dict[current]:
                if word not in visited:
                    q.append((word, step + 1))
        return 0
            
                
            
        
                
                
         