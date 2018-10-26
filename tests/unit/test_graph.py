from unittest import TestCase

from maze_generator.Graph import Graph


class TestGraph(TestCase):
    """This class represent unit test cases for the graph."""

    def test_invalid_size(self):
        try:
            Graph(-1)
            self.fail("Should not be able to pass negative values")
        except ValueError as e:
            self.assertEqual("Given invalid size parameter", str(e))
