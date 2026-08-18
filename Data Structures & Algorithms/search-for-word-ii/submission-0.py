class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

    def add(self,word:str):
        curr = self
    
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.isEndOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        dic = TrieNode()
        res = set()

        for word in words:
            dic.add(word)

        ROWS,COLS = len(board), len(board[0])
        visited = set()

        def dfs(i,j,node,word):
            if i >= ROWS or j >= COLS or i < 0 or j < 0:
                return 

            ch = board[i][j]
            
            if (i,j) in visited or ch not in node.children:
                return

            visited.add((i,j))
            node = node.children[ch]
            word += ch

            if node.isEndOfWord:
                res.add(word)

            dfs(i-1,j,node,word) # TOP
            dfs(i+1,j,node,word) # DOWN
            dfs(i,j-1,node,word) # LEFT
            dfs(i,j+1,node,word) # RIGHT

            visited.remove((i,j))

        for row in range(ROWS):
            for col in range(COLS):
                dfs(row,col,dic,"")
        
        return list(res)
 

            
