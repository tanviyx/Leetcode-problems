class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        nums.sort()

        ans = set()

        for i in range(len(nums)):

            # skip duplicate first values
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            seen = set()

            for j in range(i + 1, len(nums)):

                third = -(nums[i] + nums[j])

                if third in seen:

                    triplet = (nums[i], third, nums[j])

                    ans.add(tuple(sorted(triplet)))

                seen.add(nums[j])

        return [list(x) for x in ans]

        