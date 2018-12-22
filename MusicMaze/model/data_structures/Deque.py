class Deque:
    """This class represents a double ended queue, to be used as part of
    the music maze project mostly due to the motivation of wanting to
    write a deque from scratch."""

    def __init__(self):
        """Constructs a deque. A deque will always be empty at the start."""
        self.size = 0
        self.head = None
        self.tail = None

    def peek_head(self):
        """Peek at the head of the deque without removing it.

        Returns:
            Any: the data of the head of the tail
        Raises:
            IndexError: if a head does not exist"""
        pass

    def peek_tail(self):
        """Peek at the tail of the deque without removing it.

        Returns:
            Any: the data of the tail of the tail, generic data type
        Raises:
            IndexError: if a tail does not exist"""
        pass

    def push_head(self, data):
        """Pushes the data to the head of the deque.

        Args:
            data(Any): the data to push to the front of the deque"""
        pass

    def push_tail(self, data):
        """Pushes the data to the tail of the deque.

        Args:
            data(Any): the data to push to the back of the deque"""
        pass

    def pop_head(self):
        """Pops the front-most data off of the deque.

        Returns:
            Any: the data off of the front of the deque
        Raises:
            IndexError: If the head does not exist"""
        pass

    def pop_tail(self):
        """Pops the back-most data off of the deque.

        Returns:
            Any: the data off of the back of the deque
        Raises:
            IndexError: If the tail does not exist"""
        pass

    def __len__(self):
        """Return the length of this deque."""
        return self.size

    def __bool__(self):
        """Determines if this deque is empty"""
        return not len(self) == 0


class Node:
    """This class is the primary workhorse of the deque, representing the
    nodes for a doubly linked list and containing the data needed for this
    deque. The node class itself should not be used for general purposes.
    Instead, the deque class should be used as the wrapper behind all of the
    node code."""

    def __init__(self):
        self.__data = None
        self.__prev = None
        self.__next = None
        pass


class SentinelNode(Node):
    """This sentinel node is used for the purpose of holding a dummy node
    for next and prev pointers to point to. This class should not be used
    in general purposes. Instead, a deque should be used for all data structure
    purposes."""

    def __init__(self):
        pass

