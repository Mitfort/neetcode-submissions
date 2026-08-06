class PrefixTree:

    def __init__(self):
        self.dic = TreeNode()

    def insert(self, word: str) -> None:
        cur = self.dic

        for c in word:
            if c not in cur.children:
                cur.children[c] = TreeNode()
            cur = cur.children[c]
        
        cur.endOfWord = True


    def search(self, word: str) -> bool:
        cur = self.dic

        for c in word:
            if c not in cur.children:
                return False
            
            cur = cur.children[c]
        return cur.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.dic

        for c in prefix:
            if c not in cur.children:
                return False
            
            cur = cur.children[c]
        
        return True


class TreeNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        