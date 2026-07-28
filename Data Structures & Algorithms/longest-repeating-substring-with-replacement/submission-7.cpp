class Solution {
public:
    int characterReplacement(string s, int k) {
        int maxLen = 0;
        int left = 0;
        int n = s.length();
        int maxCount = 0;
        int count[26] = {0};
        int len = 0;

        for(int right=0; right < n; ++right)
        {
            count[s[right] - 'A']++;

            if(count[s[right] - 'A'] > maxCount)
            {
                maxCount = count[s[right] - 'A'];
            }

            while((right - left + 1) - maxCount > k)
            {
                count[s[left] - 'A']--;
                left++; 
            }

            len = right - left + 1;
            if(len > maxLen) maxLen = len;

        }

        return maxLen;
    }
};
