class Edge:
    """This class represents an edge between two vertices. The existence of
    an edge in a graph implies that the two vertices are connected. The most
    important interpretation of this Edge class is that it is an undirected
    edge, thus an edge implies that both vertices are connected bidirectionally.
    """

    def __init__(self, vertice_one, vertice_two, weight=0):
        """Initialize an edge. Upon initialization, this edge will connect the
        two vertices by adding them as neighbors. The intended behavior is to
        then have these two neighbors both linked by themselves as neighbors,
        and also through this edge object. However, it is possible to create
        indirect connections using the add_neighbor() function, but doing so
        is discouraged and this edge connection technique is encouraged.

        Args:
            vertice_one(Vertice): the "from" vertice to connect
            vertice_two(Vertice): the "to" vertice to connect
            weight(int): a provided "weight" of the edge
        Raises:
            ValueError: If either vertice is null, or if the two vertices
                are already connected."""
        if not vertice_one or not vertice_two:
            raise ValueError("Given a null vertice as an arg")

        if vertice_one.is_neighbor(vertice_two) \
                or vertice_two.is_neighbor(vertice_one):
            raise ValueError("Attempting to add duplicate neighbor")

        vertice_one.add_neighbor(vertice_two)
        vertice_two.add_neighbor(vertice_one)
        self.__vertice_one = vertice_one
        self.__vertice_two = vertice_two
        self.__weight = weight

    def from_vertice(self):
        """Return the "from" vertice of this edge.

        Returns:
            Vertice: the from vertice of this edge
        """
        return self.__vertice_one

    def to_vertice(self):
        """Return the "to" vertice of this edge.

        Returns:
            Vertice: the to vertice of this edge
        """
        return self.__vertice_two

    def weight(self):
        """Return the weight of this edge.

        Returns:
            int: the weight of this graph
        """
        return self.__weight
