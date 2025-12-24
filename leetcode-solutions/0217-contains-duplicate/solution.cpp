class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> duplicate;
        for(int x : nums){
            if(duplicate.count(x)){
                return true;
            }
            duplicate.insert(x);
        }
        return false;
    }
};
