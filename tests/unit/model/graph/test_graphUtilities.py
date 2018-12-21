from unittest import TestCase

from model.graph.Graph import Graph
from model.graph.GraphUtilities import nodes_at_level, shortest_path


class TestGraphUtilities(TestCase):

    def test_simple_case_BFS_depth(self):
        g = Graph()

        g.add_vertice("one")
        self.assertEqual(["one"], nodes_at_level(g, "one", 0))

    def test_simple_connection_BFS_depth(self):
        g = Graph()

        g.add_vertice("one")
        g.add_vertice("two")
        g.add_vertice("three")

        g.add_edge("one", "two")
        g.add_edge("two", "three")
        self.assertEqual(["one"], nodes_at_level(g, "one", 0))
        self.assertEqual(["two"], nodes_at_level(g, "one", 1))
        self.assertEqual(["three"], nodes_at_level(g, "one", 2))

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
        self.assertCountEqual([v00], nodes_at_level(g, v00, 0))
        self.assertCountEqual([v01, v10], nodes_at_level(g, v00, 1))
        self.assertCountEqual([v11], nodes_at_level(g, v00, 2))

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

        self.assertCountEqual([v00], nodes_at_level(g, v00, 0))
        self.assertCountEqual([v01], nodes_at_level(g, v00, 1))
        self.assertCountEqual([v02, v11], nodes_at_level(g, v00, 2))
        self.assertCountEqual([v21], nodes_at_level(g, v00, 3))
        self.assertCountEqual([v20, v22], nodes_at_level(g, v00, 4))
        self.assertCountEqual([v10, v12], nodes_at_level(g, v00, 5))

        self.assertCountEqual([v21], nodes_at_level(g, v21, 0))
        self.assertCountEqual([v20, v22, v11], nodes_at_level(g, v21, 1))
        self.assertCountEqual([v10, v12, v01], nodes_at_level(g, v21, 2))
        self.assertCountEqual([v00, v02], nodes_at_level(g, v21, 3))

    def test_shortest_path_empty_case(self):
        g = Graph()

        g.add_vertice("one")
        g.add_vertice("two")
        self.assertEqual([], shortest_path(g, "one", "two"))

    def test_shortest_path_one_path(self):
        g = Graph()

        g.add_vertice("one")
        g.add_vertice("two")
        g.add_edge("one", "two")

        self.assertCountEqual(["one", "two"], shortest_path(g, "one", "two"))

    def test_shortest_path_forked_path(self):

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

        self.assertCountEqual([v00, v10, v11], shortest_path(g, v00, v11))
        self.assertCountEqual([], shortest_path(g, v00, v00))
        self.assertCountEqual([v01, v00, v10, v11], shortest_path(g, v01, v11))

    def test_complex_graph_shortest_path(self):

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

        self.assertCountEqual([v00, v01, v11, v21, v22, v12],
                              shortest_path(g, v00, v12))
        self.assertCountEqual([v00, v01, v02],
                              shortest_path(g, v00, v02))
        self.assertCountEqual([v10, v20, v21, v11, v01, v00],
                              shortest_path(g, v10, v00))
        self.assertCountEqual([v21, v11, v01, v02],
                              shortest_path(g, v21, v02))
        self.assertCountEqual([v12, v22, v21, v20, v10],
                              shortest_path(g, v12, v10))

    def test_BFS_invalid_root(self):
        g = Graph()

        try:
            nodes_at_level(g, "dog", 2)
            self.fail("Should not be able to use non-existent vertice")
        except ValueError as e:
            self.assertEqual("Root not found in graph", str(e))

    def test_BFS_negative_depth(self):
        g = Graph()
        g.add_vertice("s")

        try:
            nodes_at_level(g, "s", -1)
            self.fail("Should not be able to use negative depth")
        except ValueError as e:
            self.assertEqual("Given invalid depth", str(e))

    def test_shortest_path_not_source_node(self):
        g = Graph()
        g.add_vertice("to")

        try:
            shortest_path(g, "from", "to")
            self.fail("Should not be able to find a path in non-existent node")
        except ValueError as e:
            self.assertEqual("Vertice not found in graph", str(e))

    def test_shortest_path_not_dest_node(self):
        g = Graph()
        g.add_vertice("from")

        try:
            shortest_path(g, "from", "to")
            self.fail("Should not be able to find a path in non-existent node")
        except ValueError as e:
            self.assertEqual("Vertice not found in graph", str(e))
