"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        self.queue = []  # todo для очереди можно использовать python list

    def enqueue(self, elem: Any) -> Any:
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing
        """
        self.queue.insert(0, elem)
        print(elem)
        return self.queue

    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if no elements.

        :return: dequeued element
        """

        if not self.queue:
            return None
        return self.queue.pop()

    def peek(self, ind: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """
        self.reversed_index = -ind -1
        try:
            self.queue[ind]
        except IndexError:
            return None
        print(ind)
        return self.queue[self.reversed_index]

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        self.queue.clear()
        return None
