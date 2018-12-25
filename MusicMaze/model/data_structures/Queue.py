from model.data_structures.Deque import Deque


class Queue:
    """This class represents a queue data structure, reinvented out of the
    wheel purely for the sake of novelty."""

    def __init__(self):
        """Constructs an empty queue."""
        self._deque = Deque()

    def peek(self):
        """Peek at the earliest entry in the queue without removing it.

        Returns:
            Any: the data of the front-most entry in the queue
        Raises:
            IndexError: If no data is in the queue."""
        if not self._deque:
            raise IndexError("Queue is empty")
        return self._deque.peek_head()

    def enqueue(self, data):
        """Puts the given data into the queue.

        Args:
            data(Any): the data to be inserted into the back of the queue"""
        self._deque.push_tail(data)

    def dequeue(self):
        """Removes the earliest entry from the queue and returns it.

        Returns:
            Any: the data of the earliest entry in the queue
        Raises:
            IndexError: If the queue is empty"""
        if not self._deque:
            raise IndexError("Queue is empty")
        return self._deque.pop_head()

    def __len__(self):
        """Returns the size of the queue.

        Returns:
            int: the size of the queue"""
        return len(self._deque)

    def __bool__(self):
        """Returns true if the queue has an entry

        Returns:
            bool: True if len(queue) > 0, false otherwise"""
        return len(self) > 0
