class WordDictionary:

    def __init__(self):
        self.trie = {}
    def addWord(self, word: str) -> None:
        curr = self.trie
        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]
        curr['@'] = {}
        # print(self.trie)

    def search(self, word: str) -> bool:
        return self.helper(word, self.trie)
        
    def helper(self, word, curr):
        if len(word) == 0:
            if '@' in curr:
                return True
            return False
        if word[0] != ".":
            if word[0] not in curr:
                return False
            return self.helper(word[1:], curr[word[0]])
        else:
            for ch in curr.keys():
                if self.helper(word[1:], curr[ch]):
                    return True
            return False
             
    


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)