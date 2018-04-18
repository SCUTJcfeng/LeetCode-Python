# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list_node = ListNode(None)
        a = l1
        b = l2
        c = list_node
        carr = 0

        while a or b:
            res = carr
            flag_a = True
            flag_b = True
            if a:
                res += a.val
            else:
                flag_a = False
            if b:
                res += b.val
            else:
                flag_b = False

            if res > 9:
                carr = 1
                res -= 10
                c.next = ListNode(1)
            else:
                carr = 0
            c.val = res

            if flag_a and a.next or flag_b and b.next:
                c.next = ListNode(None)
            c = c.next
            if flag_a:
                a = a.next
            if flag_b:
                b = b.next

        return list_node

l1 = ListNode(5)
p1 = ListNode(4)
p2 = ListNode(3)

l2 = ListNode(5)
p3 = ListNode(3)
p4 = ListNode(4)

# l1.next = p1
# p1.next = p2

# l2.next =p3
# p3.next =p4

so = Solution()
res = so.addTwoNumbers(l1, l2)
