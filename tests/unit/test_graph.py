from unittest import TestCase

from model.graph.Edge import Edge
from model.graph.Graph import Graph
from model.graph.Vertice import Vertice


class TestGraph(TestCase):
    """This class represent unit test cases for the graph."""

    def test_graph_contains_same_edge_different_from_vertice(self):
        v1 = Vertice("one")
        v2 = Vertice("two")

        edge1 = Edge(v1, v2)
        edge2 = Edge(v2, v1)

        g = Graph()
        g.add_vertice(v1)
        g.add_vertice(v2)

        self.assertFalse(g.contains_edge(edge1))
        self.assertFalse(g.contains_edge(edge2))

        g.add_edge(edge1)
        self.assertTrue(g.contains_edge(edge1))
        self.assertTrue(g.contains_edge(edge2))

    def test_overlapping_edge_unique_contains(self):
        """Adding multiple edges to a single vertice should not
        change the contains_edge() function return value"""

        v1 = Vertice("one")
        v2 = Vertice("two")
        v3 = Vertice("three")
        v4 = Vertice("four")

        edge1 = Edge(v1, v2)
        edge2 = Edge(v2, v3)
        edge3 = Edge(v3, v4)

        g = Graph()
        g.add_vertice(v1)
        g.add_vertice(v2)
        g.add_vertice(v3)
        g.add_vertice(v4)

        self.assertFalse(g.contains_edge(edge1))
        self.assertFalse(g.contains_edge(edge2))
        self.assertFalse(g.contains_edge(edge3))

        g.add_edge(edge1)
        self.assertTrue(g.contains_edge(edge1))
        self.assertFalse(g.contains_edge(edge2))
        self.assertFalse(g.contains_edge(edge3))

        g.add_edge(edge2)
        self.assertTrue(g.contains_edge(edge1))
        self.assertTrue(g.contains_edge(edge2))
        self.assertFalse(g.contains_edge(edge3))

        g.add_edge(edge3)
        self.assertTrue(g.contains_edge(edge1))
        self.assertTrue(g.contains_edge(edge2))
        self.assertTrue(g.contains_edge(edge3))

    def test_random_edge_not_contained(self):
        """A random edge that is tangentially related to another edge
        should not affect the current contains function"""

        v1 = Vertice("one")
        v2 = Vertice("three")

        random_vertice1 = Vertice("nope")
        random_vertice2 = Vertice("not here")
        random_vertice3 = Vertice("not here as well")

        edge1 = Edge(v1, v2)

        g = Graph()
        g.add_vertice(v1)
        g.add_vertice(v2)
        g.add_vertice(random_vertice1)
        g.add_vertice(random_vertice2)
        g.add_vertice(random_vertice3)
        g.add_edge(Edge(v1, random_vertice1))
        g.add_edge(Edge(v1, random_vertice2))
        g.add_edge(Edge(v2, random_vertice3))

        self.assertFalse(g.contains_edge(edge1))

    def test_error_when_readding_existing_edge(self):
        """There should be an expected error if an edge was already added"""
        v1 = Vertice("one")
        v2 = Vertice("two")

        edge = Edge(v1, v2)
        g = Graph()
        g.add_vertice(v1)
        g.add_vertice(v2)
        g.add_edge(edge)

        try:
            g.add_edge(edge)
            self.fail("Should not be able to add an existing edge")
        except ValueError as e:
            self.assertEqual("Given an edge that already exists", str(e))

    def test_error_when_adding_other_edges(self):
        """There should be an expected error if an edge was already added"""
        v1 = Vertice("one")
        v2 = Vertice("two")

        edge = Edge(v1, v2)
        g = Graph()
        g.add_vertice(v1)
        g.add_vertice(v2)
        g.add_edge(edge)

        try:
            g.add_edge(Edge(v2, v1))
            self.fail("Should not be able to add an existing edge")
        except ValueError as e:
            self.assertEqual("Given an edge that already exists", str(e))

    def test_error_when_adding_same_vertices_reversed(self):
        """Since we have defined vertices to have unique names, any vertices
        containing such names should be invalid vertices"""
        v1 = Vertice("one")
        v2 = Vertice("two")

        edge = Edge(v1, v2)
        g = Graph()
        g.add_vertice(v1)
        g.add_vertice(v2)
        g.add_edge(edge)

        try:
            g.add_edge(Edge(v2, v1))
            self.fail("Should not be able to add an existing edge")
        except ValueError as e:
            self.assertEqual("Given an edge that already exists", str(e))

