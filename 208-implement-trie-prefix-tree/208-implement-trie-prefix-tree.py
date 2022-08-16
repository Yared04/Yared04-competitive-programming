class Trie:

    def __init__(self):
        self.trie = {}
        
    def insert(self, word: str) -> None:
        cur = self.trie
        for char in word:
            if char not in cur:
                cur[char] = {}
            cur = cur[char]
        cur["#"] = {}

    def search(self, word: str) -> bool:
        cur = self.trie
        for char in word:
            if char in cur:
                cur = cur[char]
            else: return False
        return True if "#" in cur else False
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.trie
        for char in prefix:
            if char in cur:
                cur = cur[char]
            else: return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)