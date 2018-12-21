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
        g.remove_edge("dfsafas", "fdsfas")

    def test_simple_case_BFS_depth(self):
        g = Graph()

        g.add_vertice("one")
        self.assertEqual(["one"], g.nodes_at_level("one", 0))

    def test_simple_connection_BFS_depth(self):
        g = Graph()

        g.add_vertice("one")
        g.add_vertice("two")
        g.add_vertice("three")

        g.add_edge("one", "two")
        g.add_edge("two", "three")
        self.assertEqual(["one"], g.nodes_at_level("one", 0))
        self.assertEqual(["two"], g.nodes_at_level("one", 1))
        self.assertEqual(["three"], g.nodes_at_level("one", 2))

    def test_forked_BFS(self):
        g = Graph()

        v00 = "(0, 0)"
        v01 = "(0, 1)"
        v10 = "(1, 0)"
        v11 = "(1, 1)"

        g.add_vertice(v00)
        g.add_vertice(v01)
        g.add_vertice(v10)
        g.add_vertice(v11)

        g.add_edge(v00, v01)
        g.add_edge(v00, v10)

        g.add_edge(v10, v11)
        self.assertCountEqual([v00], g.nodes_at_level(v00, 0))
        self.assertCountEqual([v01, v10], g.nodes_at_level(v00, 1))
        self.assertCountEqual([v11], g.nodes_at_level(v00, 2))

    def test_complex_graph_BFS(self):

        g = Graph()

        v00 = "(0, 0)"
        v01 = "(0, 1)"
        v02 = "(0, 2)"
        v10 = "(1, 0)"
        v11 = "(1, 1)"
        v12 = "(1, 2)"
        v20 = "(2, 0)"
        v21 = "(2, 1)"
        v22 = "(2, 2)"

        g.add_vertice(v00)
        g.add_vertice(v01)
        g.add_vertice(v02)
        g.add_vertice(v10)
        g.add_vertice(v11)
        g.add_vertice(v12)
        g.add_vertice(v20)
        g.add_vertice(v21)
        g.add_vertice(v22)

        # o - o - o
        #     |
        # o   o   o`
        # |   |   |
        # o - o - o

        g.add_edge(v00, v01)
        g.add_edge(v01, v02)
        g.add_edge(v01, v11)
        g.add_edge(v10, v20)
        g.add_edge(v11, v21)
        g.add_edge(v12, v22)
        g.add_edge(v20, v21)
        g.add_edge(v21, v22)

        self.assertCountEqual([v00], g.nodes_at_level(v00, 0))
        self.assertCountEqual([v01], g.nodes_at_level(v00, 1))
        self.assertCountEqual([v02, v11], g.nodes_at_level(v00, 2))
        self.assertCountEqual([v21], g.nodes_at_level(v00, 3))
        self.assertCountEqual([v20, v22], g.nodes_at_level(v00, 4))
        self.assertCountEqual([v10, v12], g.nodes_at_level(v00, 5))

        self.assertCountEqual([v21], g.nodes_at_level(v21, 0))
        self.assertCountEqual([v20, v22, v11], g.nodes_at_level(v21, 1))
        self.assertCountEqual([v10, v12, v01], g.nodes_at_level(v21, 2))
        self.assertCountEqual([v00, v02], g.nodes_at_level(v21, 3))

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

    def test_BFS_invalid_root(self):
        g = Graph()

        try:
            g.nodes_at_level("dfsfs", 2)
            self.fail("Should not be able to use non-existent vertice")
        except ValueError as e:
            self.assertEqual("Root not found in graph", str(e))

    def test_BFS_negative_depth(self):
        g = Graph()
        g.add_vertice("s")

        try:
            g.nodes_at_level("s", -1)
            self.fail("Should not be able to use negative depth")
        except ValueError as e:
            self.assertEqual("Given invalid depth", str(e))

