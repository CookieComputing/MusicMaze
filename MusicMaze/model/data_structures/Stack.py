from model.data_structures.Deque import Deque


class Stack:
    """This class represents an implementation of a stack using a deque. The
    purpose of this class is solely for novelty: Making a stack from scratch
    is more interesting than using a built in, and making test cases were
    also interesting."""

    def __init__(self):
        """Constructs an empty stack."""
        self.__deque = Deque()

    def peek(self):
        """Returns the top entry of the stack (last inserted).

        Returns:
            Any: the data of the last item pushed onto the stack.
        Raises:
            IndexError: If the stack is empty"""
        if not self:
            raise IndexError("Stack is empty")
        return self.__deque.peek_head()

    def pop(self):
        """Removes and returns the top entry of the stack.

        Returns:
            Any: the data of the last item pushed onto the stack.
        Raises:
            IndexError: If the stack is empty"""
        if not self:
            raise IndexError("Stack is empty")
        return self.__deque.pop_head()

    def push(self, data):
        """Pushes the data onto the top of the stack.

        Args:
            data(Any): any sort of data to push onto the stack."""
        self.__deque.push_head(data)

    def __len__(self):
        """Returns the size of this stack.

        Returns:
            int: the size of this stack"""
        return len(self.__deque)

    def __bool__(self):
        """Returns true if this stack is non empty

        Returns:
            bool: True if len(stack) > 0"""
        return len(self) > 0
