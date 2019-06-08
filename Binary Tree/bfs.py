# !/usr/bin/python3.6
# -*- coding:utf-8 -*-
'''
Project: Binary Tree
Author: jc feng (jcfeng2013@gmail.com)
File Created: 2019-06-08 13:53:21
Last Modified: 2019-06-08 15:16:09
'''

from tree import Tree


class Solution:
    def levelOrder(self, root):
        my_list = []
        self.level_order(root, my_list)
        return my_list

    def level_order(self, root, my_list):
        if root is None:
            return
        stack = [[root]]
        my_list.append([root.val])
        while stack:
            head_list = stack.pop(0)
            temp_list = []
            temp_stack = []
            for head in head_list:
                left, right = head.l_child, head.r_child
                if left:
                    temp_list.append(left.val)
                    temp_stack.append(left)
                if right:
                    temp_list.append(right.val)
                    temp_stack.append(right)
            if temp_list:
                my_list.append(temp_list)
                stack.append(temp_stack)


if __name__ == "__main__":
    t = Tree()
    for i in range(15):
        t.add(i)
    my_list = Solution().levelOrder(t.root)
