class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.length();
        int left = 0;
        int maxLength = 0;
        int len = 0;
        std::map<char,int> window;

        for(int right=0; right < n; right++)
        {
            while(window[s[right]] == 1)
            {
                window[s[left]] = 0;
                len--;
                left++;
            }

            window[s[right]] = 1;
            len++;

            if(len > maxLength) maxLength = len;
        }
        

        return maxLength;
    }
};
