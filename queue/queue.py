# !/usr/bin/python3.6
# -*- coding:utf-8 -*-
'''
Project: queue
Author: jc feng (jcfeng2013@gmail.com)
File Created: 2019-06-08 15:28:27
Last Modified: 2019-06-08 15:34:56
'''


class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.size = k
        self.queue = []

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if len(self.queue) < self.size:
            self.queue.append(value)
            return True
        return False

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        try:
            self.queue.pop(0)
            return True
        except IndexError:
            return False

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        try:
            return self.queue[0]
        except IndexError:
            return -1

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        try:
            return self.queue[-1]
        except IndexError:
            return -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return len(self.queue) == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return len(self.queue) == self.size
