class WordDictionary:

    def __init__(self):
        self.dic = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.dic 

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.endOfWord = True
        
    def search(self, word: str) -> bool:
        q = deque([(self.dic,0)])

        while q: 
            for obj in range(len(q)):
                curr,idx = q.popleft()
 
                if idx == len(word) and curr.endOfWord:
                    return True

                if idx >= len(word): continue

                if word[idx] in curr.children:
                    q.append((curr.children[word[idx]], idx+1))

                if word[idx] == '.':
                    for child in curr.children:
                        q.append((curr.children[child],idx+1))
                
        return False
        
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False