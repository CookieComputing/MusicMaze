class Graph:
    """This class represents an implementation of a graph. The graph is a
    set of vertices and edges, and is interpreted using an adjacency list
    for the ease of connecting vertices with their neighbors. The graph itself
    is not a maze, but an rather interpretation of a connected tree of nodes.
    The class is an undirected simple graph, and as such will have unique
    edges that are bidirectional.
  """

    def __init__(self):
        """Initializes the graph as an initially empty graph. All vertices
        and edges must subsequently be added to the graph.
        """
        self.__vertices = set()
        self.__vertice_ids = set()

        # The edges are held in a dictionary whose keys are of the form
        # "from - to"
        # where from and to represent the names of the vertices
        self.__edges = {}

    def add_vertice(self, vertice):
        """Adds a given vertice into the graph. The vertice must be a new
        object and should also have a unique name identifying the vertice.

        Args:
            vertice(Vertice): the given vertice to add
        Raises:
            ValueError: if another vertice exists in the graph with the same
                name as the given vertice"""
        if self.contains_vertice_with_name(vertice.name()) \
                or self.contains_vertice(vertice):
            raise ValueError("Graph already contains vertice with same name")
        self.__vertice_ids.add(vertice.name())
        self.__vertices.add(vertice)

    def contains_vertice(self, vertice):
        """Determines if a specific vertice exists in the graph. The vertice
        should be a physical object in the graph if it is contained.

        Args:
            vertice(Vertice): the given vertice to check
        Returns:
            boolean: Whether or not the vertice in question is in the graph"""
        return vertice in self.__vertices

    def contains_vertice_with_name(self, name):
        """Determines if a specific vertice with a given name is in the graph.

        Args:
            name(str): the name of a vertice in the graph
        Returns:
            boolean: Whether or not such a vertice with a name exists"""
        return name in self.__vertice_ids

    def add_edge(self, edge):
        """Adds an edge to this graph only if that edge does not already
        exist. In our interpretation of the program, this means an undirected
        edge. Furthermore, only edges containing vertices that actually
        exist in the graph are acceptable.

        Raises:
            ValueError: if the edge attempting to be added already exists.
            ValueError: if the edge in question contains vertices that do
                not exist in the graph"""
        if self.contains_edge(edge):
            raise ValueError("Given an edge that already exists")
        if not self.contains_vertice(edge.from_vertice()) \
                or not self.contains_vertice(edge.to_vertice()):
            raise ValueError("Edge contains vertice not in graph")
        edge_name = edge.from_vertice().name() \
                    + " - " \
                    + edge.to_vertice().name()
        self.__edges[edge_name] = edge

    def contains_edge(self, edge):
        """Determines whether or not this graph contains a given edge. An edge
        is considered in the graph if the graph contains some edge such that
        the vertices of that edge match the vertices of the given edge.

        Args:
            edge(Edge): the edge to check in the graph. The edge is
                bidirectional, thus it is acceptable for either side of the edge
                to be checked by the graph.
        Returns:
            boolean: Whether or not the edge is in the graph."""
        return edge.from_vertice().name() + " - " + edge.to_vertice().name() \
            in self.__edges \
            or edge.to_vertice().name() + " - " + edge.from_vertice().name() \
            in self.__edges

    def edges(self):
        """Returns the edges of this graph.

        Returns:
            list(Edge): the edges of this graph
        """
        return list(self.__edges.values())

    def vertices(self):
        """Returns the vertices of this graph.

        Returns:
            list(Vertice): the vertices of this graph
        """
        return self.__vertices
