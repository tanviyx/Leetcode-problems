class Solution {
public:
    vector<vector<int>> ans;

    void solve(vector<int>& nums, int index) {
        // Base case: one permutation is formed
        if (index == nums.size()) {
            ans.push_back(nums);
            return;
        }

        // Try every element at the current position
        for (int i = index; i < nums.size(); i++) {
            swap(nums[index], nums[i]);   // Choose
            solve(nums, index + 1);       // Explore
            swap(nums[index], nums[i]);   // Backtrack
        }
    }

    vector<vector<int>> permute(vector<int>& nums) {
        solve(nums, 0);
        return ans;
    }
};