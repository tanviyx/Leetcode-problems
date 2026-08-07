class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        def shift(pos, value):
            # Shift elements one step to the right
            for k in range(m, pos, -1):
                nums1[k] = nums1[k - 1]
            nums1[pos] = value

        for x in nums2:
            inserted = False

            # Find where to insert x
            for j in range(m):
                if x < nums1[j]:
                    shift(j, x)
                    m += 1
                    inserted = True
                    break

            # If x is larger than every element
            if not inserted:
                nums1[m] = x
                m += 1