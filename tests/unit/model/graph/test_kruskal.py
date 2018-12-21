from unittest import TestCase

from model.graph.Graph import Graph
from model.graph.kruskal import kruskal


class TestKruskal(TestCase):
    """Tests to see that kruskal will return the set of edges corresponding
    to the minimum spanning tree from various graphs"""

    @staticmethod
    def contains_edge(v1, v2, edges):
        for edge in edges:
            if (v1 == edge.from_vertice().name()
                    and v2 == edge.to_vertice().name()) \
                   or (v2 == edge.from_vertice().name()
                       and v1 == edge.to_vertice().name()):
                return True
        return False

    def test_three_by_three_graph(self):
        g = Graph()

        # The graph looks like this:
        # o - o - o
        #     |
        # o - o - o
        # |
        # o - o - o

        node_00 = "(0, 0)"
        node_01 = "(0, 1)"
        node_02 = "(0, 2)"
        node_10 = "(1, 0)"
        node_11 = "(1, 1)"
        node_12 = "(1, 2)"
        node_20 = "(2, 0)"
        node_21 = "(2, 1)"
        node_22 = "(2, 2)"

        g.add_vertice(node_00)
        g.add_vertice(node_01)
        g.add_vertice(node_02)
        g.add_vertice(node_10)
        g.add_vertice(node_11)
        g.add_vertice(node_12)
        g.add_vertice(node_20)
        g.add_vertice(node_21)
        g.add_vertice(node_22)

        g.add_edge(node_00, node_01, 0)
        g.add_edge(node_01, node_02, 1)
        g.add_edge(node_00, node_10, 10)
        g.add_edge(node_01, node_11, 2)
        g.add_edge(node_02, node_12, 11)
        g.add_edge(node_10, node_11, 3)
        g.add_edge(node_11, node_12, 4)
        g.add_edge(node_10, node_20, 5)
        g.add_edge(node_11, node_21, 12)
        g.add_edge(node_12, node_22, 13)
        g.add_edge(node_20, node_21, 6)
        g.add_edge(node_21, node_22, 7)

        kruskal_edges = kruskal(g)
        self.assertEqual(8, len(kruskal_edges))
        self.assertTrue(self.contains_edge(node_00, node_01, kruskal_edges))
        self.assertTrue(self.contains_edge(node_01, node_02, kruskal_edges))
        self.assertTrue(self.contains_edge(node_01, node_11, kruskal_edges))
        self.assertTrue(self.contains_edge(node_10, node_11, kruskal_edges))
        self.assertTrue(self.contains_edge(node_11, node_12, kruskal_edges))
        self.assertTrue(self.contains_edge(node_10, node_20, kruskal_edges))
        self.assertTrue(self.contains_edge(node_20, node_21, kruskal_edges))
        self.assertTrue(self.contains_edge(node_21, node_22, kruskal_edges))

    def test_two_by_three_graph(self):
        g = Graph()

        # The graph should look like this:
        # o - o - o
        # |       |
        # o - o   o

        node_00 = "(0, 0)"
        node_01 = "(0, 1)"
        node_02 = "(0, 2)"
        node_10 = "(1, 0)"
        node_11 = "(1, 1)"
        node_12 = "(1, 2)"

        g.add_vertice(node_00)
        g.add_vertice(node_01)
        g.add_vertice(node_02)
        g.add_vertice(node_10)
        g.add_vertice(node_11)
        g.add_vertice(node_12)

        g.add_edge(node_00, node_01, 0)
        g.add_edge(node_01, node_02, 1)
        g.add_edge(node_10, node_11, 2)
        g.add_edge(node_11, node_12, 9)
        g.add_edge(node_00, node_10, 3)
        g.add_edge(node_01, node_11, 10)
        g.add_edge(node_02, node_12, 4)

        kruskal_edges = kruskal(g)
        self.assertEqual(5, len(kruskal_edges))
        self.assertTrue(self.contains_edge(node_00, node_01, kruskal_edges))
        self.assertTrue(self.contains_edge(node_01, node_02, kruskal_edges))
        self.assertTrue(self.contains_edge(node_00, node_10, kruskal_edges))
        self.assertTrue(self.contains_edge(node_02, node_12, kruskal_edges))
        self.assertTrue(self.contains_edge(node_10, node_11, kruskal_edges))

    def test_three_by_two_graph(self):
        g = Graph()
        # The graph should look like this:
        # o - o
        #     |
        # o   o
        # |   |
        # o - o

        node_00 = "(0, 0)"
        node_01 = "(0, 1)"
        node_10 = "(1, 0)"
        node_11 = "(1, 1)"
        node_20 = "(2, 0)"
        node_21 = "(2, 1)"

        g.add_vertice(node_00)
        g.add_vertice(node_01)
        g.add_vertice(node_10)
        g.add_vertice(node_11)
        g.add_vertice(node_20)
        g.add_vertice(node_21)

        g.add_edge(node_00, node_01, 0)
        g.add_edge(node_00, node_10, 10)
        g.add_edge(node_01, node_11, 1)
        g.add_edge(node_10, node_11, 11)
        g.add_edge(node_10, node_20, 2)
        g.add_edge(node_11, node_21, 3)
        g.add_edge(node_20, node_21, 4)

        kruskal_edges = kruskal(g)
        self.assertEqual(5, len(kruskal_edges))
        self.assertTrue(self.contains_edge(node_00, node_01, kruskal_edges))
        self.assertTrue(self.contains_edge(node_01, node_11, kruskal_edges))
        self.assertTrue(self.contains_edge(node_11, node_21, kruskal_edges))
        self.assertTrue(self.contains_edge(node_21, node_20, kruskal_edges))
        self.assertTrue(self.contains_edge(node_20, node_10, kruskal_edges))


    def test_two_by_two_graph(self):
        g = Graph()

        # The graph looks like this:
        # o - o
        #     |
        # o - o

        node_00 = "(0, 0)"
        node_01 = "(0, 1)"
        node_10 = "(1, 0)"
        node_11 = "(1, 1)"

        g.add_vertice(node_00)
        g.add_vertice(node_01)
        g.add_vertice(node_10)
        g.add_vertice(node_11)

        g.add_edge(node_00, node_01, 1)
        g.add_edge(node_10, node_11, 2)
        g.add_edge(node_01, node_11, 3)
        g.add_edge(node_00, node_11, 4)

        kruskal_edges = kruskal(g)

        self.assertEqual(3, len(kruskal_edges))
        self.assertTrue(self.contains_edge(node_00, node_01, kruskal_edges))
        self.assertTrue(self.contains_edge(node_10, node_11, kruskal_edges))
        self.assertTrue(self.contains_edge(node_01, node_11, kruskal_edges))

    def test_one_direction_horizontal_connection(self):
        g = Graph()
        # The graph looks like this:
        # o - o - o

        node_00 = "(0, 0)"
        node_01 = "(0, 1)"
        node_02 = "(0, 2)"
        g.add_vertice(node_00)
        g.add_vertice(node_01)
        g.add_vertice(node_02)

        g.add_edge(node_00, node_01, 1)
        g.add_edge(node_01, node_02, 2)

        kruskal_edges = kruskal(g)
        self.assertEqual(2, len(kruskal_edges))
        self.assertTrue(self.contains_edge(node_00, node_01, kruskal_edges))
        self.assertTrue(self.contains_edge(node_01, node_02, kruskal_edges))

    def test_one_direction_vertical_connection(self):
        g = Graph()

        node_00 = "(0, 0)"
        node_10 = "(1, 0)"
        node_20 = "(2, 0)"

        g.add_vertice(node_00)
        g.add_vertice(node_10)
        g.add_vertice(node_20)

        g.add_edge(node_00, node_10, 1)
        g.add_edge(node_10, node_20, 2)

        kruskal_edges = kruskal(g)
        self.assertEqual(2, len(kruskal_edges))
        self.assertTrue(self.contains_edge(node_00, node_10, kruskal_edges))
        self.assertTrue(self.contains_edge(node_10, node_20, kruskal_edges))

