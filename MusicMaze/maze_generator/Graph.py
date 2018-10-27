import random

from maze_generator.Edge import Edge
from maze_generator.Vertice import Vertice


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
    vertices if they are indexed next to each other"""

    def __init__(self, width=1, height=1, seed=None):
        """Initialize the graph with the initial dimensions of the grid. The
        grid is a width * height board containing width * height vertices that can
        be referenced by (row, col). Initially, all vertices will be
        connected to their neighboring cells, and this can only be changed
        by calling the generate_maze() function.

        Args:
            width(int): the width of the maze
            height(int): the height of the maze
            seed(int): a random seed used to introduce a specific seed. This
                argument should only be used for the purposes of generating a
                specific maze.
        Raises:
            ValueError: if the size of the board is a non-negative number
            TypeError: if the size is not an integer
        """

        if width <= 0 or height <= 0:
            raise ValueError("Given invalid size parameter")

        if seed:
            random.seed(seed)

        self.__width = width
        self.__height = height
        self.__edges = []
        self.__vertices = []

        self.__generate_vertices()
        self.__generate_edges()

    def generate_maze(self, algorithm):
        """Given an algorithm, generate a maze from this graph's given vertices
        and then use that MST found from the algorithm as this graph's edges.
        This method will generate a completely new set of edges to apply the
        maze generation algorithm on and subsequently use the results of those
        edges as the new maze."""
        pass

    def __generate_edges(self):
        """Connects all vertices in this graph with soft edges. The
        __generate_vertices() method should first initialize all of the
        vertices first before calling this method."""

        self.__edges = []
        random_min = 0
        random_max = 10000

        # add all horizontal edges first
        for row in range(self.__height):
            for col in range(self.__width-1):
                self.__edges.append(Edge(self.__vertices[row][col],
                                         self.__vertices[row][col+1],
                                         random.randint(random_min,
                                                        random_max)))

        if self.__height == 1:
            return

        # add all vertical edges second
        for row in range(0, self.__height-1):
            for col in range(self.__width):
                self.__edges.append(Edge(self.__vertices[row][col],
                                         self.__vertices[row+1][col],
                                         random.randint(random_min,
                                                        random_max)))

    def __generate_vertices(self):
        """Using the size parameter supplied upon initialization, construct
        an size * size list containing vertices that contain names in the form
        of (row, col)."""
        self.__vertices = [[Vertice("({0}, {1})".format(row, col))
                            for col in range(self.__width)]
                           for row in range(self.__height)]

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
