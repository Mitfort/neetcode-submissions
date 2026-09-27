class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        sizes:str = ""
        words:str = ""
        
        for word in strs:
            sizes += str(len(word)) + ';'
            words += '#' + word

        return sizes + words

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        idx:int = 0
        n:int = len(s)
        char:str = ""
        word:str = ""
        sizes:List[int] = []

        # READ THE SIZES 
        while True:
            char = s[idx]
            if char == "#": break

            if char == ";": 
                sizes.append(int(word))
                word = ""
                idx+=1
                continue
            
            word += char
            idx += 1

        print(sizes)
        words:List[str] = []
        word = ""
        size_idx = 0
        
        # READ THE WORDS
        while idx < n:
            char = s[idx]

            if char == "#":
                for i in range(sizes[size_idx]):
                    idx+=1
                    word += s[idx]

                size_idx += 1                
                words.append(word)
                word = ""
                idx += 1
            else:
                idx += 1 
        
        return words
                



            


        
        