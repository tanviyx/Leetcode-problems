class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        x=n+m

        for i in nums2[::-1]:
            inserted= False
            while not inserted:
                if m!=0 and nums1[m-1]<i:
                    nums1[x-1]=i
                    inserted=True
                    x=x-1
                    break
                elif m!=0 and nums1[m-1]>i:
                    nums1[x-1]=nums1[m-1]
                    inserted=False
                    x=x-1
                else:
                    nums1[x-1]=i
                    inserted=True
                    x=x-1
                    break
                m=m-1
