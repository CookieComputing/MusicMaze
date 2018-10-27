from random import randint
from unittest import TestCase

from maze_generator.Graph import Graph


class TestGraph(TestCase):
    """This class represent unit test cases for the graph."""

    def test_large_maze_vertices(self):
        """The maze should have a correct ordering for it's vertice names"""
        width = randint(1, 200)
        height = randint(1, 100)

        g = Graph(width, height)
        for row in range(height):
            for col in range(width):
                self.assertEqual("({0}, {1})".format(row, col),
                                 g.vertices()[row][col].name())

    def test_maze_vertices(self):
        """Check various positions in a grid to ensure they exist correctly"""
        width = 5
        height = 2

        g = Graph(width, height)
        self.assertEqual("(0, 0)", g.vertices()[0][0].name())
        self.assertEqual("(1, 0)", g.vertices()[1][0].name())
        self.assertEqual("(1, 4)", g.vertices()[1][4].name())

    def test_default_graph(self):
        """The ordering of the maze should be in the form of (row, col)"""
        g = Graph()

        self.assertEqual("(0, 0)", g.vertices()[0][0].name())

    def test_edge_initialization(self):
        """Ensure that all vertices are initially connected to each other, but
        only softly connected"""

        width = 5
        height = 2
        g = Graph(width, height)

        def edge_equal(edge, from_row, from_col, to_row, to_col):
            from_vertice = edge.from_vertice()
            to_vertice = edge.to_vertice()
            return from_vertice.name() == \
                "({0}, {1})".format(from_row, from_col) \
                and to_vertice.name() == \
                "({0}, {1})".format(to_row, to_col)

        # The graph in visual representation
        # o o o o o
        # o o o o o
        self.assertEqual(2*4 + 5, len(g.edges()))

        for col in range(width-1):
            self.assertTrue(any([edge_equal(edge, 0, col, 0, col+1)
                                 for edge in g.edges()]))
            self.assertTrue(any([edge_equal(edge, 1, col, 1, col+1)
                                 for edge in g.edges()]))

        for col in range(width):
            self.assertTrue(any([edge_equal(edge, 0, col, 1, col)
                                 for edge in g.edges()]))

    def test_one_row_edges(self):
        """A graph with only one row should not crash when initializing edges"""
        width = 5
        height = 1
        g = Graph(width, height)

        self.assertEqual(4, len(g.edges()))

        def edge_equal(edge, from_row, from_col, to_row, to_col):
            from_vertice = edge.from_vertice()
            to_vertice = edge.to_vertice()
            return from_vertice.name() == \
                "({0}, {1})".format(from_row, from_col) \
                and to_vertice.name() == \
                "({0}, {1})".format(to_row, to_col)

        for col in range(4):
            self.assertTrue(any([edge_equal(edge, 0, col, 0, col+1)
                                for edge in g.edges()]))

    def test_one_column_edges(self):
        """A graph with only one column
        should not crash when initializing edges"""
        width = 1
        height = 5
        g = Graph(width, height)

        # o
        # o
        # o
        # o
        # o
        self.assertEqual(4, len(g.edges()))

        def edge_equal(edge, from_row, from_col, to_row, to_col):
            from_vertice = edge.from_vertice()
            to_vertice = edge.to_vertice()
            return from_vertice.name() == \
                "({0}, {1})".format(from_row, from_col) \
                and to_vertice.name() == \
                "({0}, {1})".format(to_row, to_col)

        for row in range(4):
            self.assertTrue(any([edge_equal(edge, row, 0, row+1, 0)
                                 for edge in g.edges()]))

    def test_invalid_width(self):
        try:
            Graph(-1, 3)
            self.fail("Should not be able to pass negative values")
        except ValueError as e:
            self.assertEqual("Given invalid size parameter", str(e))

    def test_invalid_height(self):
        try:
            Graph(1, -3)
            self.fail("Should not be able to pass negative values")
        except ValueError as e:
            self.assertEqual("Given invalid size parameter", str(e))

    def test_invalid_dimensions(self):
        try:
            Graph(0, 0)
            self.fail("Should not be able to pass negative values")
        except ValueError as e:
            self.assertEqual("Given invalid size parameter", str(e))
