class Vertice:
    """This class represents an implementation of a vertice. A vertice in the
    graph will be interpreted as a "position" that a user can walk onto in the
    maze, and will consequently also be used as the cells of a maze."""

    def __init__(self, name, neighbors=None):
        """Initialize a vertice. A vertice should given a unique identifier
        to promote the identification of nodes.

        Args:
            name(str): the unique identifier of a vertice. This name should be
                used to promote a uid for a node and proper care with vertices
                should enforce that no two nodes have the same name.
            neighbors(list(Vertice)): If supplied, assign the vertice's
                neighbors to be all of the vertices contained in the list.
        Raises:
            ValueError: If the name is empty or None
            """
        if not name:
            raise ValueError("Given null name in vertice")

        if neighbors is None:
            neighbors = []

        self.__name = name
        self.__neighbors = neighbors

    def add_neighbor(self, neighbor):
        """Assign the given vertice to become this node's neighbor. This is
        assignment is a directed assignment, however, so only this vertice will
        be able to recognize the given neighbor as a neighbor after a single
        operation of this function.

        Args:
            neighbor(Vertice): the vertice to become a neighbor to
        Raises:
            ValueError: If given a null neighbor or attempting to add itself
                as a potential neighbor
        """
        if not neighbor:
            raise ValueError("Given invalid neighbor")
        if neighbor == self:
            raise ValueError("Vertice cannot become it's own neighbor")
        self.__neighbors.append(neighbor)

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
        return potential_neighbor in self.__neighbors

    def neighbors(self):
        """Returns a copied list of this vertice's neighbors.

        Returns:
            neighbors(list(Vertice)): This vertice's neigbhors
        """
        return [vertice for vertice in self.__neighbors]
