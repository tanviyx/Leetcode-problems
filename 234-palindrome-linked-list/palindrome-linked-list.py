# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head):
        l = []

        while head:
            l.append(head.val)
            head = head.next

        n = len(l)

        for i in range(n // 2):
            if l[i] != l.pop():
                return False

        return True