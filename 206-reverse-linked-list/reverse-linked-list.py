# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):

        new_head = None

        while head:
            new_head = self.insert_beginning(new_head, head.val)
            head = head.next

        return new_head

    def insert_beginning(self, head, value):
        new_node = ListNode(value)
        new_node.next = head
        return new_node
    