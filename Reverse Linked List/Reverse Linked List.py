# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        b = None
        while head:
            a = head
            head = head.next
            a.next = b
            b = a
        return b

head = ListNode(1)
p1 = ListNode(2)
p2 = ListNode(3)

head.next = p1
p1.next = p2
# head = [1,2,3]
so = Solution()
rev_head = so.reverseList(head)