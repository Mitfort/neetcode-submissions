class Solution {
public:
    bool isAnagram(string s, string t) {
        std::map<char,int> text1;
        std::map<char,int> text2;

        for(char letter : s)
        {
            if(text1[letter])
            {
                text1[letter] += 1;
            }
            else
            {
                text1[letter] = 1;
            }
        }

        for(char letter : t)
        {
            if(text2[letter])
            {
                text2[letter] += 1;
            }
            else
            {
                text2[letter] = 1;
            }
        }

        if(text1 == text2) return true;

        return false;
    }
};
