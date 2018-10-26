from unittest import TestCase

from maze_generator.Edge import Edge
from maze_generator.Vertice import Vertice


class TestEdge(TestCase):

    def test_neighbor_linked_connect(self):
        """Single directional connections should return true for the
        edge connected() function"""
        vertice1 = Vertice("one")
        vertice2 = Vertice("two")
        edge = Edge(vertice1, vertice2)

        self.assertFalse(vertice1.is_neighbor(vertice2))
        self.assertFalse(vertice2.is_neighbor(vertice1))
        self.assertFalse(edge.connected())

        vertice1.add_neighbor(vertice2)
        self.assertTrue(vertice1.is_neighbor(vertice2))
        self.assertFalse(vertice2.is_neighbor(vertice1))
        self.assertTrue(edge.connected())

    def test_simple_connect(self):
        """Ensure that the connection function works with simple connections"""

        vertice1 = Vertice("one")
        vertice2 = Vertice("two")
        edge = Edge(vertice1, vertice2)

        self.assertFalse(vertice1.is_neighbor(vertice2))
        self.assertFalse(vertice2.is_neighbor(vertice1))
        self.assertFalse(edge.connected())

        edge.connect_vertices()
        self.assertTrue(edge.connected())
        self.assertTrue(vertice1.is_neighbor(vertice2))
        self.assertTrue(vertice2.is_neighbor(vertice1))

    def test_symbolic_edge_linking(self):
        """When an edge is created, it should not physically link the two edges
        within initialization"""

        vertice1 = Vertice("one")
        vertice2 = Vertice("two")

        self.assertFalse(vertice1.is_neighbor(vertice2))
        self.assertFalse(vertice2.is_neighbor(vertice1))

        Edge(vertice1, vertice2)

        self.assertFalse(vertice1.is_neighbor(vertice2))
        self.assertFalse(vertice2.is_neighbor(vertice1))

    def test_edge_linking_when_connection_exists(self):
        """Edges should not be able to be created if the edge has already
        connected the two vertices"""

        vertice1 = Vertice("one")
        vertice2 = Vertice("two")

        edge = Edge(vertice1, vertice2)
        edge.connect_vertices()

        try:
            edge.connect_vertices()
            self.fail("Should not be able to connect vertices twice")
        except ValueError as e:
            self.assertEqual("Attempting to add duplicate neighbor", str(e))

    def test_edge_linking_when_another_edge_exists(self):
        """Edges should not be able to be created if another edge
        exists already"""

        vertice1 = Vertice("one")
        vertice2 = Vertice("two")

        edge = Edge(vertice1, vertice2)
        edge.connect_vertices()

        try:
            y = Edge(vertice1, vertice2)
            y.connect_vertices()
            self.fail("Another edge should not be able to be created")
        except ValueError as e:
            self.assertEqual("Attempting to add duplicate neighbor", str(e))

    def test_edge_linking_with_one_link(self):
        """Directional neighbors should also raise errors on edge creation"""

        vertice1 = Vertice("one")
        vertice2 = Vertice("two")

        vertice1.add_neighbor(vertice2)
        edge1 = Edge(vertice1, vertice2)
        try:
            edge1.connect_vertices()
            self.fail("Another edge should not be able to be created")
        except ValueError as e:
            self.assertEqual("Attempting to add duplicate neighbor", str(e))

        edge2 = Edge(vertice2, vertice1)
        try:
            edge2.connect_vertices()
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

        edge = Edge(vertice1, vertice2)
        try:
            edge.connect_vertices()
            self.fail("Another edge should not be able to be created")
        except ValueError as e:
            self.assertEqual("Attempting to add duplicate neighbor", str(e))

    def test_edge_from_vertice(self):
        vertice1 = Vertice("one")
        vertice2 = Vertice("two")

        edge = Edge(vertice1, vertice2)

        self.assertEqual(vertice1, edge.from_vertice())

    def test_edge_to_vertice(self):
        vertice1 = Vertice("one")
        vertice2 = Vertice("two")

        edge = Edge(vertice1, vertice2)

        self.assertEqual(vertice2, edge.to_vertice())

    def test_default_edge_weight(self):
        vertice1 = Vertice("one")
        vertice2 = Vertice("two")

        edge = Edge(vertice1, vertice2)
        self.assertEqual(0, edge.weight())

    def test_custom_edge_weight(self):
        vertice1 = Vertice("one")
        vertice2 = Vertice("two")

        edge = Edge(vertice1, vertice2, 5)
        self.assertEqual(5, edge.weight())
