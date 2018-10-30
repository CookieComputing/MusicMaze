class Graph:
    """This class represents an implementation of a graph. The graph is a
    set of vertices and edges, and is interpreted using an adjacency list
    for the ease of connecting vertices with their neighbors. The graph itself
    is not a maze, but an rather interpretation of a connected tree of nodes.
  """

    def __init__(self):
        """Initializes the graph as an initially empty graph. All vertices
        and edges must subsequently be added to the graph.
        """
        self.__vertices = []
        self.__edges = []

    def add_edge(self, edge):
        """Adds an edge to this graph."""

    def edges(self):
        """Returns the edges of this graph.

        Returns:
            list(Edge): the edges of this graph
        """
        return self.__edges

    def vertices(self):
        """Returns the vertices of this graph.

        Returns:
            list(Vertice): the vertices of this graph
        """
        return self.__vertices
