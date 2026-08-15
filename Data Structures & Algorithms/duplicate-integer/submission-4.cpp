class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        if (nums.empty()) return false;
        sort(nums.begin(), nums.end());
        for(int i = 0; i < (int)nums.size() - 1; i++){
            int j = i + 1;
            if((nums[i] - nums[j]) == 0){
                return true;
            }
        }
        return false;
    }
};