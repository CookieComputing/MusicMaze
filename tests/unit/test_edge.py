from unittest import TestCase

from maze_generator.Edge import Edge
from maze_generator.Vertice import Vertice


class TestEdge(TestCase):

    def test_edge_linking(self):
        """When an edge is created, it should automatically link two vertices
        together."""

        vertice1 = Vertice("one")
        vertice2 = Vertice("two")

        self.assertFalse(vertice1.is_neighbor(vertice2))
        self.assertFalse(vertice2.is_neighbor(vertice1))

        Edge(vertice1, vertice2)

        self.assertTrue(vertice1.is_neighbor(vertice2))
        self.assertTrue(vertice2.is_neighbor(vertice1))

    def test_edge_linking_when_another_edge_exists(self):
        """Edges should not be able to be created if another edge
        exists already"""

        vertice1 = Vertice("one")
        vertice2 = Vertice("two")

        Edge(vertice1, vertice2)

        try:
            Edge(vertice1, vertice2)
            self.fail("Another edge should not be able to be created")
        except ValueError as e:
            self.assertEqual("Attempting to add duplicate neighbor", str(e))

    def test_edge_linking_with_one_link(self):
        """Directional neighbors should also raise errors on edge creation"""

        vertice1 = Vertice("one")
        vertice2 = Vertice("two")

        vertice1.add_neighbor(vertice2)
        try:
            Edge(vertice1, vertice2)
            self.fail("Another edge should not be able to be created")
        except ValueError as e:
            self.assertEqual("Attempting to add duplicate neighbor", str(e))

        try:
            Edge(vertice2, vertice1)
            self.fail("Another edge should not be able to be created")
        except ValueError as e:
            self.assertEqual("Attempting to add duplicate neighbor", str(e))

        # there should be no side effect with vertice 2 having vertice as
        # a neighbor
        self.assertTrue(vertice1.is_neighbor(vertice2))
        self.assertFalse(vertice2.is_neighbor(vertice1))

    def test_edge_linking_with_two_links(self):

        vertice1 = Vertice("one")
        vertice2 = Vertice("two")

        vertice1.add_neighbor(vertice2)
        vertice2.add_neighbor(vertice1)

        try:
            Edge(vertice1, vertice2)
            self.fail("Another edge should not be able to be created")
        except ValueError as e:
            self.assertEqual("Attempting to add duplicate neighbor", str(e))

    def test_edge_from_vertice(self):
        vertice1 = Vertice("one")
        vertice2 = Vertice("two")

        e = Edge(vertice1, vertice2)

        self.assertEqual(vertice1, e.from_vertice())

    def test_edge_to_vertice(self):
        vertice1 = Vertice("one")
        vertice2 = Vertice("two")

        e = Edge(vertice1, vertice2)

        self.assertEqual(vertice2, e.to_vertice())

    def test_default_edge_weight(self):
        vertice1 = Vertice("one")
        vertice2 = Vertice("two")

        e = Edge(vertice1, vertice2)
        self.assertEqual(0, e.weight())

    def test_custom_edge_weight(self):
        vertice1 = Vertice("one")
        vertice2 = Vertice("two")

        e = Edge(vertice1, vertice2, 5)
        self.assertEqual(5, e.weight())


