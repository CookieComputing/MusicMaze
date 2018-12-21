from unittest import TestCase
from model.graph.Graph import Graph


class TestGraph(TestCase):
    """This class represent unit test cases for the graph."""

    def find_vertice(self, name, vertices):
        """Helper function to locate a vertice in the graph. The return type
        of vertices is a set, so there is no order guarantee from the
        returned copied set"""
        for vertice in vertices:
            if vertice.name() == name:
                return vertice
        self.fail("Could not find a vertice with given name")

    def test_adding_vertice_basic_add(self):
        g = Graph()

        self.assertFalse(g.contains_vertice("one"))
        g.add_vertice("one")
        self.assertTrue(g.contains_vertice("one"))

    def test_adding_edge_forces_connection(self):
        g = Graph()

        g.add_vertice("one")
        g.add_vertice("two")

        self.assertFalse(g.contains_edge("one", "two"))
        g.add_edge("one", "two")
        self.assertTrue(g.contains_edge("two", "one"))
        self.assertTrue(g.contains_edge("one", "two"))

        vertices = g.vertices()
        vertice_one = self.find_vertice("one", vertices)
        vertice_two = self.find_vertice("two", vertices)

        self.assertTrue(vertice_one.is_neighbor(vertice_two))
        self.assertTrue(vertice_two.is_neighbor(vertice_one))

    def test_removing_edges_severs_connections(self):
        g = Graph()

        g.add_vertice("one")
        g.add_vertice("two")

        vertices = g.vertices()
        vertice_one = self.find_vertice("one", vertices)
        vertice_two = self.find_vertice("two", vertices)

        g.add_edge("one", "two")
        self.assertTrue(g.contains_edge("one", "two"))
        self.assertTrue(vertice_one.is_neighbor(vertice_two))
        self.assertTrue(vertice_two.is_neighbor(vertice_one))

        g.remove_edge("two", "one")
        self.assertFalse(g.contains_edge("one", "two"))
        self.assertFalse(vertice_one.is_neighbor(vertice_two))
        self.assertFalse(vertice_two.is_neighbor(vertice_one))

    def test_removing_edges_with_no_added_edge(self):
        """Expected behavior is to interact with the graph by using
        edges. By mutating the vertices and add neighbors manually,
        the edges will not be correctly connected"""
        g = Graph()

        g.add_vertice("one")
        g.add_vertice("two")

        vertices = g.vertices()
        vertice_one = self.find_vertice("one", vertices)
        vertice_two = self.find_vertice("two", vertices)

        vertice_one.add_neighbor(vertice_two)
        self.assertTrue(vertice_one.is_neighbor(vertice_two))
        self.assertFalse(vertice_two.is_neighbor(vertice_one))

        g.remove_edge("one", "two")
        # There was initially no edge and thus nothing was changed
        self.assertTrue(vertice_one.is_neighbor(vertice_two))
        self.assertFalse(vertice_two.is_neighbor(vertice_one))

    def test_remove_edges_with_no_existing_vertices(self):
        g = Graph()
        g.remove_edge("dog", "fad")

    def test_no_neighbors(self):
        g = Graph()

        g.add_vertice("hi")

        self.assertEqual([], g.neighbors("hi"))

    def test_multiple_neighbors(self):
        g = Graph()

        g.add_vertice("one")
        g.add_vertice("two")
        g.add_vertice("three")
        g.add_vertice("four")

        g.add_edge("one", "two")
        g.add_edge("one", "three")

        g.add_edge("two", "three")
        g.add_edge("two", "four")

        self.assertCountEqual(["two", "three"], g.neighbors("one"))
        self.assertCountEqual(["one", "three", "four"], g.neighbors("two"))
        self.assertCountEqual(["one", "two"], g.neighbors("three"))
        self.assertCountEqual(["two"], g.neighbors("four"))

    def test_adding_non_existent_edge(self):
        g = Graph()

        g.add_vertice("one")

        try:
            g.add_edge("one", "nil")
            self.fail("Should not be able to add edge if both vertices exist")
        except ValueError as e:
            self.assertEqual("Vertice contained in edge not in graph", str(e))

    def test_add_self_reference_edge(self):
        g = Graph()
        g.add_vertice("single")

        try:
            g.add_edge("single", "single")
        except ValueError as e:
            self.assertEqual("Vertice cannot become it's own neighbor", str(e))

        self.assertFalse(g.contains_edge("single", "single"))

    def test_other_non_existent_edge(self):
        g = Graph()
        g.add_vertice("other")

        try:
            g.add_edge("nil", "other")
            self.fail("Should not be able to add edge if both vertices exist")
        except ValueError as e:
            self.assertEqual("Vertice contained in edge not in graph", str(e))

    def test_both_non_existent_edge(self):
        g = Graph()
        g.add_vertice("other")

        try:
            g.add_edge("nil", "nope")
            self.fail("Should not be able to add edge if both vertices exist")
        except ValueError as e:
            self.assertEqual("Vertice contained in edge not in graph", str(e))

    def test_adding_existent_edge(self):
        g = Graph()

        g.add_vertice("one")

        try:
            g.add_vertice("one")
            self.fail("Should not be able to add another vertice")
        except ValueError as e:
            self.assertEqual("Vertice already in the graph", str(e))

        self.assertTrue(g.contains_vertice("one"))

    def test_non_existent_node_neighbor(self):
        g = Graph()

        try:
            g.neighbors("lol")
            self.fail("Expected fail if no lol exists")
        except ValueError as e:
            self.assertEqual("Vertice not in graph", str(e))

