class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        curr = self.head

        while curr and index > 0:
            curr = curr.next
            index -= 1

        if curr:
            return curr.val
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)

        if self.head is None:
            self.head = new_node
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:

        if index == 0:
            self.addAtHead(val)
            return

        curr = self.head

        while curr and index > 1:
            curr = curr.next
            index -= 1

        if curr is None:
            return

        new_node = ListNode(val)
        new_node.next = curr.next
        curr.next = new_node

    def deleteAtIndex(self, index: int) -> None:

        if self.head is None:
            return

        if index == 0:
            self.head = self.head.next
            return

        curr = self.head

        while curr.next and index > 1:
            curr = curr.next
            index -= 1

        if curr.next:
            curr.next = curr.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)