
# 二叉树遍历


class Node:
    def __init__(self, val=-1, l_child=None, r_child=None):
        self.val = val
        self.l_child = l_child
        self.r_child = r_child


class Tree:
    def __init__(self):
        self.root = Node()
        self.queue = []

    def add(self, val):
        node = Node(val)
        if self.root.val == -1:
            self.root = node
            self.queue.append(self.root)
        else:
            last_node = self.queue[0]
            if last_node.l_child is None:
                last_node.l_child = node
            else:
                last_node.r_child = node
                self.queue.pop(0)
            self.queue.append(node)

    # 前序遍历 递归
    def pre_order(self, root):
        if root is None:
            return
        print(root.val)
        self.pre_order(root.l_child)
        self.pre_order(root.r_child)

    # 中序遍历 递归
    def in_order(self, root):
        if root is None:
            return
        self.in_order(root.l_child)
        print(root.val)
        self.in_order(root.r_child)

    # 后序遍历 递归
    def post_order(self, root):
        if root is None:
            return
        self.post_order(root.l_child)
        self.post_order(root.r_child)
        print(root.val)

    # 前序遍历 非递归
    def pre_order_2(self, root):
        stack = []
        node = root
        while node or stack:
            while node:
                print(node.val)
                stack.append(node)
                node = node.l_child
            node = stack.pop()
            node = node.r_child

    # 中序遍历 非递归
    def in_order_2(self, root):
        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.l_child
            node = stack.pop()
            print(node.val)
            node = node.r_child

    # 后序遍历 非递归
    def post_order_2(self, root):
        stack_1 = []
        stack_2 = []
        node = root
        stack_1.append(node)
        while stack_1:
            node = stack_1.pop()
            if node.l_child:
                stack_1.append(node.l_child)
            if node.r_child:
                stack_1.append(node.r_child)
            stack_2.append(node)
        while stack_2:
            print(stack_2.pop().val)


if __name__ == "__main__":
    t = Tree()
    for i in range(15):
        t.add(i)

    # t.pre_order(t.root)
    # t.in_order(t.root)
    # t.post_order(t.root)
    # t.pre_order_2(t.root)
    # t.in_order_2(t.root)
    t.post_order_2(t.root)
