# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head, left, right):

        values = []

        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next

        # Reverse the required portion
        values[left-1:right] = values[left-1:right][::-1]

        # Build a new linked list
        dummy = ListNode(0)
        curr = dummy

        for v in values:
            curr.next = ListNode(v)
            curr = curr.next

        return dummy.next