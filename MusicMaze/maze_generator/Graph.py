class Graph:
    """This class represents an implementation of a graph. The graph is a
    set of vertices and edges, and is interpreted using an adjacency list
    for the ease of connecting vertices with their neighbors. The graph itself
    serves as an interpretation for the entire maze: The locations that the user
    can walk onto are considered the vertices, and the edges are considered the
    possible paths that the user can walk onto. The graph is undirected, thus
    an edge will imply that the user can walk to one position and back.

    This maze is interpreted as a 2D grid of cells, where the cells can be
    interpreted as if they were in (row, col) form. Thus, if the list of
    vertices called from the graph can be interpreted as being neighboring
    vertices if they are indexed next to each other."""

    def __init__(self, size=1):
        """Initialize the graph with the initial dimensions of the grid. The
        grid is a size * size board containing size * size vertices that can
        be referenced by (row, col). Initially, all vertices will be
        connected to their neighboring cells, and this can only be changed
        by calling the generate_maze() function.

        Args:
            size(int): the dimension of the maze
        Raises:
            ValueError: if the size of the board is a non-negative number
            TypeError: if the size is not an integer
        """

        if size <= 0:
            raise ValueError("Given invalid size parameter")

        self.__size = size
        self.__edges = []
        self.__vertices = []

    def generate_maze(self, algorithm):
        """Given an algorithm, generate a maze from this graph's given edges
        and then use that MST found from the algorithm as this graph's edges."""
        pass

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
