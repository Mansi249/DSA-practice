class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> need;
        for(int i =0;i< nums.size() ; i++){
            int complement = target - nums[i];
            if(need.count(complement)){
                return {need[complement],i};
            }
            need[nums[i]] = i;
        }
    return{};
    }
};
