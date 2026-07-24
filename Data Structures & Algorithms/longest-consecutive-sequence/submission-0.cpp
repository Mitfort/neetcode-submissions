class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int longest = 0;
        for(int i=0; i < nums.size(); i++)
        {
            int size = 1;
            bool valid = false;
            int idx = i;
            do
            {
                for(int j=0; j < nums.size(); j++)
                {
                    if(nums[j] == nums[idx] + 1)
                    {
                        size += 1;
                        valid = true;
                        idx = j;
                        break;
                    }
                    else
                    {
                        valid = false;
                    }
                }

            }while(valid);

            if(size > longest)
            {
                longest = size;
            }
        }

        return longest;
    }
};
