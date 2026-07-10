class Solution {
public:
    string getPermutation(int n, int k) {

        vector<int> nums;

        // Store numbers 1 to n
        for(int i = 1; i <= n; i++) {
            nums.push_back(i);
        }

        // factorial array
        vector<int> fact(n);

        fact[0] = 1;

        for(int i = 1; i < n; i++) {
            fact[i] = fact[i-1] * i;
        }

        // convert to 0-based indexing
        k--;

        string ans = "";

        for(int i = n; i >= 1; i--) {

            // size of each block
            int blockSize = fact[i-1];

            // find index
            int index = k / blockSize;

            // append selected number
            ans += to_string(nums[index]);

            // remove used number
            nums.erase(nums.begin() + index);

            // update k
            k %= blockSize;
        }

        return ans;
    }
};