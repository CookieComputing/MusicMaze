class Vertice:
    """This class represents an implementation of a vertice. A vertice in the
    graph will be interpreted as a "position" that a user can walk onto in the
    maze, and will consequently also be used as the cells of a maze."""

    def __init__(self, name):
        """Initialize a vertice. A vertice should given a unique identifier
        to promote the identification of nodes.

        Args:
            name(str): the unique identifier of a vertice. This name should be
                used to promote a uid for a node and proper care with vertices
                should enforce that no two nodes have the same name.
        Raises:
            ValueError: If the name is empty or None
            """
        if not name:
            raise ValueError("Given null name in vertice")

        self.__name = name
        self.__neighbors = dict()

    def add_neighbor(self, neighbor):
        """Assign the given vertice to become this node's neighbor. This is
        assignment is a directed assignment, however, so only this vertice will
        be able to recognize the given neighbor as a neighbor after a single
        operation of this function.

        Args:
            neighbor(Vertice): the vertice to become a neighbor to
        Raises:
            ValueError: If given a null neighbor or attempting to add itself
                as a potential neighbor, or if adding a duplicate neighbor
        """
        if not neighbor:
            raise ValueError("Given invalid neighbor")
        if neighbor == self:
            raise ValueError("Vertice cannot become it's own neighbor")
        if neighbor.name() in self.__neighbors:
            raise ValueError("Attempting to add duplicate neighbor")
        self.__neighbors[neighbor.name()] = neighbor

    def remove_neighbor(self, neighbor):
        """Removes a given neighbor from this vertice's neighbors.

        Args:
            neighbor(str): the neighbor to remove
        Raises:
            ValueError(str): If the neighbor does not exist
        """
        if neighbor.name() not in self.__neighbors:
            raise ValueError("Neighbor does not exist to remove")
        if neighbor != self.__neighbors[neighbor.name()]:
            raise ValueError("Given vertice is not the actual vertice neighbor")
        del self.__neighbors[neighbor.name()]

    def is_neighbor(self, potential_neighbor):
        """Determines if the given vertice is a potential neighbor of this
        vertice. This neighbor checking function will only determine that
        the given vertice is a neighbor from this vertice's perspective, and
        not from the neighbor's perspective.

        Args:
            potential_neighbor(Vertice): the expected neighbor
        Returns:
            boolean: If the vertice is indeed a neighbor of this vertice.
        """
        if potential_neighbor.name() not in self.__neighbors:
            return False
        return self.__neighbors[potential_neighbor.name()] \
            == potential_neighbor

    def neighbors(self):
        """Returns a list of this vertice's neighbors. Since this is an
        internal implementation detail, we make the choice to allow the
        vertice to return actual references to other vertices. There is
        no guarantee of the order of the neighbors.

        Returns:
            neighbors(list(Vertice)): This vertice's neighbors
        """
        return list(self.__neighbors.values())

    def name(self):
        """Return the unique name of this vertice.

        Returns:
            str: the name of this vertice"""
        return self.__name
