"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any
import heapq

# TODO Проверить, как написан код у Виктора :)
class PriorityQueue:
    def __init__(self):
        self.enqueue_priority = []  # todo для очереди можно использовать python dict
        self.enqueue_item = {}

    def enqueue(self, elem: Any, priority: int = 0) -> Any:
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing
        """
        # heapq.heappush(self.priority_queue, (priority, elem))
        # return self.priority_queue
        self.enqueue_item = {
            'elem': elem,
            'priority': priority
        }
        if not self.enqueue_priority:
            self.enqueue_priority.append(self.enqueue_item)
            return None
        for index, self.current_item in enumerate(self.enqueue_priority):
            if self.enqueue_item['priority'] >= self.current_item['priority']:
                self.enqueue_priority.insert(index, self.enqueue_item)
        else:
            self.enqueue_priority.append(self.enqueue_item)

    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if not elements.

        :return: dequeued element
        """
        # if not self.priority_queue:
        #     return None
        # return heapq.heappop(self.priority_queue)[-1]
        if not self.enqueue_priority:
            return None
        return self.enqueue_priority.pop()["elem"]

    def peek(self, ind: int = 0, priority: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """
        self.reversed_index = -ind -1
        # try:
        #     self.priority_queue[priority]
        # except IndexError:
        #     return None
        return self.enqueue_priority[self.reversed_index]["elem"]

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        self.enqueue_item.clear()
        return None
