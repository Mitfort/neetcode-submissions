class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::map<int,int> roznice;

        for(int i=0; i < nums.size(); i++)
        {
            int diff = target - nums[i];

            if(roznice.count(diff))
            {
                return {roznice[diff],i};
            }
            
            roznice[nums[i]] = i;
        }

        return {0,0};
    }
};
