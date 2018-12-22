class Queue:
    """This class represents a queue data structure, reinvented out of the
    wheel purely for the sake of novelty."""

    def __init__(self):
        """Constructs an empty queue."""
        pass

    def peek(self):
        """Peek at the earliest entry in the queue without removing it.

        Returns:
            Any: the data of the front-most entry in the queue
        Raises:
            IndexError: If no data is in the queue."""
        pass

    def enqueue(self, data):
        """Puts the given data into the queue.

        Args:
            data(Any): the data to be inserted into the back of the queue"""
        pass

    def dequeue(self):
        """Removes the earliest entry from the queue and returns it.

        Returns:
            Any: the data of the earliest entry in the queue
        Raises:
            IndexError: If the queue is empty"""
        pass

    def __len__(self):
        """Returns the size of the queue.

        Returns:
            int: the size of the queue"""
        pass

    def __bool__(self):
        """Returns true if the queue has an entry

        Returns:
            bool: True if len(queue) > 0, false otherwise"""
        pass
