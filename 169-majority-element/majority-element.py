class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()

        max_count = -1
        result = -1

        count = 1
        comp = nums[0]

        for i in range(1, len(nums)):

            if nums[i] == comp:
                count += 1

            else:
                if count > max_count:
                    max_count = count
                    result = comp

                comp = nums[i]
                count = 1

        # Check the last group
        if count > max_count:
            result = comp

        return result