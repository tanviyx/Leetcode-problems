# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        count=0
        s=set(nums)
        while head:
            if head.val in s:
                if head.next==None:
                    count+=1
                elif head.next.val not in s:
                    count+=1
            head=head.next
    
        return count