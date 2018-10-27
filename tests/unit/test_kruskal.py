import random
from unittest import TestCase

from maze_generator.Edge import Edge
from maze_generator.Graph import Graph
from maze_generator.Vertice import Vertice
from maze_generator.kruskal import kruskal


class TestKruskal(TestCase):
    """Tests to see that kruskal will return the set of edges corresponding
    to the minimum spanning tree from various graphs"""

    def test_simple_horizontal_graph(self):
        """A horizontal graph should give the same set of edges, possibly in
        a different order thanks to the random weights"""
        width = 5
        height = 1
        seed = 1
        g = Graph(width, height, seed)

        test_vertices = []
        for col in range(width):
            test_vertices.append(Vertice("({0}, {1})".format(0, col)))

        random.seed(seed)
        test_edges = []
        for col in range(width-1):
            test_edges.append(Edge(test_vertices[col], test_vertices[col+1],
                                   random.randint(1, 10000)))
        test_edges = sorted(test_edges, key=lambda x: x.weight())

        kruskal_edges = kruskal(g)
        self.assertEqual(4, len(kruskal_edges))

        for index in range(len(test_edges)):
            self.assertEqual("({0}, {1})".format(
                kruskal_edges[index].from_vertice().name(),
                kruskal_edges[index].to_vertice().name()),
                "({0}, {1})".format(
                test_edges[index].from_vertice().name(),
                test_edges[index].to_vertice().name()
            ))

    def test_simple_horizontal_graph(self):
        """A horizontal graph should give the same set of edges, possibly in
        a different order thanks to the random weights"""
        width = 1
        height = 5
        seed = 1
        g = Graph(width, height, seed)

        test_vertices = []
        for row in range(height):
            test_vertices.append(Vertice("({0}, {1})".format(row, 0)))

        random.seed(seed)
        test_edges = []
        for row in range(height-1):
            test_edges.append(Edge(test_vertices[row], test_vertices[row+1],
                                   random.randint(1, 10000)))
        test_edges = sorted(test_edges, key=lambda x: x.weight())

        kruskal_edges = kruskal(g)
        self.assertEqual(4, len(kruskal_edges))

        for index in range(len(test_edges)):
            self.assertEqual("({0}, {1})".format(
                kruskal_edges[index].from_vertice().name(),
                kruskal_edges[index].to_vertice().name()),
                "({0}, {1})".format(
                    test_edges[index].from_vertice().name(),
                    test_edges[index].to_vertice().name()
                ))

    def test_empty_graph(self):
        g = Graph(1,1)
        self.assertEqual([], kruskal(g))
