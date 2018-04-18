# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def reverse_list(self, list_node):
        b = None
        while list_node:
            a = list_node
            list_node = list_node.next
            a.next = b
            b = a
        return b

    def get_num(self, list_node):
        num = 0
        n = 0
        while list_node:
            num += list_node.val * pow(10, n)
            list_node = list_node.next
            n += 1
        return num

    def int_to_list_node(self, num):
        # sum = 975
        node = num % 10
        num = int(num / 10)
        list_node = ListNode(node)
        b = list_node
        while num:
            node = num % 10
            a = ListNode(node)
            b.next = a
            b = a
            num = int(num / 10) # int 默认10位
        return list_node

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        num1 = self.get_num(l1)
        num2 = self.get_num(l2)

        sum = num1 + num2

        return self.int_to_list_node(sum)

l1 = ListNode(2)
p1 = ListNode(4)
p2 = ListNode(3)

l2 = ListNode(5)
p3 = ListNode(6)
p4 = ListNode(4)

l1.next = p1
p1.next = p2

l2.next =p3
p3.next =p4

so = Solution()
res = so.addTwoNumbers(l1, l2)
print(res)
