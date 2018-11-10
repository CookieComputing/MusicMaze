class Edge:
    """This class represents an edge between two vertices. The existence of
    an edge in a graph implies that the two vertices are connected. The most
    important interpretation of this Edge class is that it is an undirected
    edge, thus an edge implies that both vertices are connected bidirectionally.
    An edge does not necessarily strictly connect two vertices physically: a
    newly created edge does not automatically cause each vertice to become each
    other's neighbor, but rather resembles a symbolic link between the two
    vertices.

    The edges are only connected once connect_vertices() is called, and will
    link both vertices regardless of whether one had already been called.
    disconnect_vertices() will sever the connections between the two classes,
    regardless of whether they were formed or not.
    """

    def __init__(self, vertice_one, vertice_two, weight=0):
        """Initialize an edge. Upon initialization, edges do not necessarily
        connect vertices to one another, they are only "softly" connected by
        the existence of this edge. In fact, it is possible to maintain multiple
        edges that relate the same two vertices, but it is not necessarily
        possible to reconnect these two edges several times.

        Args:
            vertice_one(Vertice): the "from" vertice to connect
            vertice_two(Vertice): the "to" vertice to connect
            weight(int): a provided "weight" of the edge
        Raises:
            ValueError: If either vertice is null, or if the two vertices
                are already connected."""
        if not vertice_one or not vertice_two:
            raise ValueError("Given a null vertice as an arg")

        self.__vertice_one = vertice_one
        self.__vertice_two = vertice_two
        self.__weight = weight

    def connected(self):
        """Determines if the two vertices are connected in some fashion. The
        term "connected" may refer to either a directional connection, or
        a bidirectional connection, but cannot distinguish between who is
        connected to who. To gain information about who is connected to who,
        use the vertices' is_neighbor() function.

        Returns:
            boolean: Whether or not the two vertices represented in this edge
                are physically connected
        """
        return self.__vertice_one.is_neighbor(self.__vertice_two) \
            or self.__vertice_two.is_neighbor(self.__vertice_one)

    def connect_vertices(self):
        """Physically connects the two vertices together if they are not
        already connected. This function is idempotent.
        """

        if not self.__vertice_one.is_neighbor(self.__vertice_two):
            self.__vertice_one.add_neighbor(self.__vertice_two)
        if not self.__vertice_two.is_neighbor(self.__vertice_one):
            self.__vertice_two.add_neighbor(self.__vertice_one)

    def disconnect_vertices(self):
        """Physically disconnects the vertices if they are connected.
        This function is idempotent."""
        if self.__vertice_one.is_neighbor(self.__vertice_two):
            self.__vertice_one.remove_neighbor(self.__vertice_two)
        if self.__vertice_two.is_neighbor(self.__vertice_one):
            self.__vertice_two.remove_neighbor(self.__vertice_one)

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
