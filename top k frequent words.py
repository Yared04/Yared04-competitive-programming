class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEnd = False
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            idx = ord(c)- 97
            if current.children[idx] ==  None:
                current.children[idx] = TrieNode()
            current =  current.children[idx]
        current.isEnd = True

    def search(self, word: str, isPrefix: bool = False) -> bool:
        current = self.root
        for c in word:
            idx = ord(c)- 97
            if current.children[idx] == None: return False
            current = current.children[idx]
        if current.isEnd or isPrefix:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        return self.search(prefix, True)
        
