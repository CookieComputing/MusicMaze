class Deque:
    """This class represents a double ended queue, to be used as part of
    the music maze project mostly due to the motivation of wanting to
    write a deque from scratch."""

    def __init__(self):
        """Constructs a deque. A deque will always be empty at the start."""
        self.__size = 0

        # the sentinel node is the "root" of the deque and essentially
        # has information towards both the head and tail of the deque
        self.__node = _SentinelNode()

    def peek_head(self):
        """Peek at the head of the deque without removing it.

        Returns:
            Any: the data of the head of the tail
        Raises:
            IndexError: if a head does not exist"""
        if not self.__size:
            raise IndexError("Deque is empty")
        return self.__node.peek_head()

    def peek_tail(self):
        """Peek at the tail of the deque without removing it.

        Returns:
            Any: the data of the tail of the tail, generic data type
        Raises:
            IndexError: if a tail does not exist"""
        if not self.__size:
            raise IndexError("Deque is empty")
        return self.__node.peek_tail()

    def push_head(self, data):
        """Pushes the data to the head of the deque.

        Args:
            data(Any): the data to push to the front of the deque"""
        self.__size += 1
        self.__node.push_head(data)

    def push_tail(self, data):
        """Pushes the data to the tail of the deque.

        Args:
            data(Any): the data to push to the back of the deque"""
        self.__size += 1
        self.__node.push_tail(data)

    def pop_head(self):
        """Pops the front-most data off of the deque.

        Returns:
            Any: the data off of the front of the deque
        Raises:
            IndexError: If the head does not exist"""
        if not self.__size:
            raise IndexError("Deque is empty")
        self.__size -= 1
        return self.__node.pop_head()

    def pop_tail(self):
        """Pops the back-most data off of the deque.

        Returns:
            Any: the data off of the back of the deque
        Raises:
            IndexError: If the tail does not exist"""
        if not self.__size:
            raise IndexError("Deque is empty")
        self.__size -= 1
        return self.__node.pop_tail()

    def __len__(self):
        """Return the length of this deque.

        Returns:
            int: the length of the deque"""
        return self.__size

    def __bool__(self):
        """Determines if this deque is empty.

        Returns:
            bool: Whether or not this deque is empty"""
        return len(self) > 0


class _Node:
    """This class is the primary workhorse of the deque, representing the
    nodes for a doubly linked list and containing the data needed for this
    deque. The node class itself should not be used for general purposes.
    Instead, the deque class should be used as the wrapper behind all of the
    node code."""

    def __init__(self, data=None):
        self._data = data
        self._prev = None
        self._next = None

    def data(self):
        """Returns the data of this node."""
        return self._data

    def add_prev_node(self, prev_node):
        """Connect this node's prev pointer to another node.

        Args:
            prev_node(_Node): the previous node"""
        self._prev = prev_node

    def add_next_node(self, next_node):
        """Connect this node's next pointer to another node.

        Args:
            next_node(_Node): the next node"""
        self._next = next_node

    def remove(self):
        """Removes this node from being referenced and returns the data.

        Returns:
            Any: the data in this node"""
        self._prev.add_next_node(self._next)
        self._next.add_prev_node(self._prev)
        return self.data()


class _SentinelNode(_Node):
    """This sentinel node is used for the purpose of holding a dummy node
    for next and prev pointers to point to. This class should not be used
    in general purposes. Instead, a deque should be used for all data structure
    purposes."""

    def __init__(self):
        super().__init__()
        self._prev = self
        self._next = self

    def push_head(self, data):
        node = _Node(data)
        node.add_prev_node(self)
        node.add_next_node(self._next)
        self._next.add_prev_node(node)
        self.add_next_node(node)

    def push_tail(self, data):
        node = _Node(data)
        node.add_prev_node(self._prev)
        node.add_next_node(self)
        self._prev.add_next_node(node)
        self.add_prev_node(node)

    def peek_head(self):
        return self._next.data()

    def peek_tail(self):
        return self._prev.data()

    def pop_head(self):
        return self._next.remove()

    def pop_tail(self):
        return self._prev.remove()

    def remove(self):
        raise NotImplementedError("Sentinels cannot remove themselves")
