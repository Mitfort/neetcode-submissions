class PrefixTree:

    def __init__(self):
        self.root:TrieNode = TrieNode()

    def insert(self, word: str) -> None:
        idx:int = 0
        n:int = len(word)
        curr = self.root

        while idx < n:
            
            if word[idx] not in curr.next:
                curr.next[word[idx]] = TrieNode()

            curr = curr.next[word[idx]]
            idx += 1 
        
        curr.endOfWord = True 

    def search(self, word: str) -> bool:
        idx:int = 0
        n:int = len(word)
        curr = self.root 
        
        while idx < n:
            new = curr.next.get(word[idx],None)

            if not new:
                return False 
            
            curr = new 
            idx+=1

        if not curr.endOfWord: return False 

        return True 
        

    def startsWith(self, prefix: str) -> bool:
        idx:int = 0
        n:int = len(prefix)
        curr = self.root 

        while idx < n:
            new = curr.next.get(prefix[idx],None)

            if not new:
                return False 
            
            curr = new 
            idx+=1 
        
        return True 
        
class TrieNode:
    def __init__(self):
        self.next = {}
        self.endOfWord = False 