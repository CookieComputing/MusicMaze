class Graph:
    """This class represents an implementation of a graph. The graph is a
    set of vertices and edges, and is interpreted using an adjacency list
    for the ease of connecting vertices with their neighbors. The graph itself
    serves as an interpretation for the entire maze: The locations that the user
    can walk onto are considered the vertices, and the edges are considered the
    possible paths that the user can walk onto. The graph is undirected, thus
    an edge will imply that the user can walk to one position and back."""

    def __init__(self, vertices=None, edges=None):
        """Initialize the graph with a set of vertices and edges. The edges
        should likely come from the vertices and should contain references
        to the vertices for the graph to be useful at all.

        Args:
            vertices(list): the set of vertices
            edges(list): the set of edges"""
        if vertices is None:
            vertices = []
        if edges is NameError:
            edges = []

        self.__vertices = vertices
        self.__edges = edges

