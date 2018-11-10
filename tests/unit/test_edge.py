from unittest import TestCase

from model.graph.Edge import Edge
from model.graph.Vertice import Vertice


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

    def test_edge_linking_idempotency(self):
        """Multiple connections should be simply idempotent."""

        vertice1 = Vertice("one")
        vertice2 = Vertice("two")

        edge = Edge(vertice1, vertice2)

        self.assertFalse(edge.connected())
        edge.connect_vertices()
        self.assertTrue(edge.connected())
        edge.connect_vertices()
        self.assertTrue(edge.connected())
        self.assertTrue(vertice1.is_neighbor(vertice2))
        self.assertTrue(vertice2.is_neighbor(vertice1))

    def test_single_direction_connection_to_both_connected(self):
        vertice1 = Vertice("one")
        vertice2 = Vertice("two")

        vertice1.add_neighbor(vertice2)
        edge = Edge(vertice1, vertice2)
        self.assertTrue(edge.connected())

        self.assertTrue(vertice1.is_neighbor(vertice2))
        self.assertFalse(vertice2.is_neighbor(vertice1))
        edge.connect_vertices()
        self.assertTrue(vertice1.is_neighbor(vertice2))
        self.assertTrue(vertice2.is_neighbor(vertice1))

    def test_single_direction_connection_both_connected_other_way(self):
        """This should be equivalent as the previous test"""
        vertice1 = Vertice("one")
        vertice2 = Vertice("two")

        vertice2.add_neighbor(vertice1)
        edge = Edge(vertice1, vertice2)
        self.assertTrue(edge.connected())

        self.assertFalse(vertice1.is_neighbor(vertice2))
        self.assertTrue(vertice2.is_neighbor(vertice1))
        edge.connect_vertices()
        self.assertTrue(vertice1.is_neighbor(vertice2))
        self.assertTrue(vertice2.is_neighbor(vertice1))

    def test_edge_disconnect_idempotency(self):
        vertice1 = Vertice("one")
        vertice2 = Vertice("two")

        edge = Edge(vertice1, vertice2)
        edge.connect_vertices()

        self.assertTrue(edge.connected())
        edge.disconnect_vertices()
        self.assertFalse(edge.connected())
        edge.disconnect_vertices()
        self.assertFalse(edge.connected())

    def test_edge_disconnection_single_connection(self):
        vertice1 = Vertice("one")
        vertice2 = Vertice("two")

        edge = Edge(vertice1, vertice2)
        vertice1.add_neighbor(vertice2)

        self.assertTrue(edge.connected())
        self.assertTrue(vertice1.is_neighbor(vertice2))
        edge.disconnect_vertices()
        self.assertFalse(vertice1.is_neighbor(vertice2))

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
