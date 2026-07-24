class Solution {
public:

    string encode(vector<string>& strs) {
        string result = "";

        for(int i=0; i < strs.size(); i++)
        {
            result += strs[i];
            result += '-';
        }

        return result;
    }

    vector<string> decode(string s) {

        vector<string> strs;
        string word = "";
        for(int i=0; i < s.length(); i++)
        {
            if(s[i] != '-')
            {
                word += s[i];
            }
            else
            {
                strs.push_back(word);
                word = "";
            }
        }

        return strs;

    }
};
