import heapq


class EdgeWrapper:
    """Nested class that simply returns true upon less than comparison."""
    def __init__(self, edge):
        self.__edge = edge

    def edge(self):
        return self.__edge

    def weight(self):
        return self.__edge.weight()

    def __lt__(self, other):
        """Automatically return true on less than comparisons. The priority
        queue is less concerned with the stability of the inputs, and much
        more interested in the edge weights instead."""
        return True


class PriorityQueue:
    """This class represents a priority queue to be used as part of Kruskal's
    algorithm to generate the minimum spanning tree. The primary purpose of this
    class is to function as a wrapper to Python's heapq module, which does
    not allow for keys, nor does it function as expected when items have
    equal values."""

    def __init__(self):
        self.__heap = []

    def push(self, edge):
        """Pushes the edge onto the priority queue based on it's weight.

        Args:
            edge(Edge): The edge to be pushed onto the priority queue
        """
        ew = EdgeWrapper(edge)
        heapq.heappush(self.__heap, (ew.weight(), ew))

    def extract_min(self):
        """Extracts the edge with the minimum weight in the priority queue.

        Returns:
            Edge: the edge with the minimum weight associated to it
        Raises:
            ValueErorr: If the priority is empty
        """
        if self.is_empty():
            raise ValueError("Priority queue is empty")

        edge_tuple = heapq.heappop(self.__heap)
        ew = edge_tuple[1]
        return ew.edge()

    def is_empty(self):
        """Determine if the queue is empty.

        Returns:
            boolean: whether or not this queue is empty
        """
        return len(self.__heap) == 0

    def __len__(self):
        """Returns the size of the item of this priority queue

        Returns:
            int: how many items are in this priority queue"""
        return len(self.__heap)
