import random
from unittest import TestCase

from maze_generator.Edge import Edge
from maze_generator.Graph import Graph
from maze_generator.Vertice import Vertice
from maze_generator.kruskal import kruskal


class TestKruskal(TestCase):
    """Tests to see that kruskal will return the set of edges corresponding
    to the minimum spanning tree from various graphs"""

    def test_three_by_three_graph(self):
        width = 3
        height = 3
        seed = 1
        g = Graph(width, height, seed)
        random_min = 0
        random_max = 10000

        kruskal_edges = kruskal(g)

        self.assertEqual(8, len(kruskal_edges))

        v00 = Vertice("(0, 0)")
        v01 = Vertice("(0, 1)")
        v02 = Vertice("(0, 2)")
        v10 = Vertice("(1, 0)")
        v11 = Vertice("(1, 1)")
        v12 = Vertice("(1, 2)")
        v20 = Vertice("(2, 0)")
        v21 = Vertice("(2, 1)")
        v22 = Vertice("(2, 2)")

        # o - o   o
        # |       |
        # o - o - o
        #     |   |
        # o - o   o
        random.seed(seed)
        edge1 = Edge(v00, v01, random.randint(random_min, random_max))
        Edge(v01, v02, random.randint(random_min, random_max))
        edge3 = Edge(v10, v11, random.randint(random_min, random_max))
        edge4 = Edge(v11, v12, random.randint(random_min, random_max))
        edge5 = Edge(v20, v21, random.randint(random_min, random_max))
        Edge(v21, v22, random.randint(random_min, random_max))

        edge7 = Edge(v00, v10, random.randint(random_min, random_max))
        Edge(v01, v11, random.randint(random_min, random_max))
        edge9 = Edge(v02, v12, random.randint(random_min, random_max))
        Edge(v10, v20, random.randint(random_min, random_max))
        edge11 = Edge(v11, v21, random.randint(random_min, random_max))
        edge12 = Edge(v12, v22, random.randint(random_min, random_max))

        test_edges = sorted([edge1, edge3, edge4, edge5,
                               edge7, edge9, edge11, edge12],
                            key=lambda x: x.weight())

        for index in range(len(kruskal_edges)):
            self.assertEqual(
                "({0}, {1})".format(
                    test_edges[index].from_vertice().name(),
                    test_edges[index].to_vertice().name()),
                "({0}, {1})".format(
                    kruskal_edges[index].from_vertice().name(),
                    kruskal_edges[index].to_vertice().name())
            )

    def test_two_by_three_graph(self):
        width = 2
        height = 3
        seed = 1
        g = Graph(width, height, seed)
        random_min = 0
        random_max = 10000

        kruskal_edges = kruskal(g)
        self.assertEqual(5, len(kruskal_edges))
        # o - o
        # |   |
        # o   o
        #     |
        # o - o

        v00 = Vertice("(0, 0)")
        v01 = Vertice("(0, 1)")
        v10 = Vertice("(1, 0)")
        v11 = Vertice("(1, 1)")
        v20 = Vertice("(2, 0)")
        v21 = Vertice("(2, 1)")
        random.seed(seed)

        edge1 = Edge(v00, v01, random.randint(random_min, random_max))
        Edge(v10, v11, random.randint(random_min, random_max))
        edge3 = Edge(v20, v21, random.randint(random_min, random_max))
        edge4 = Edge(v00, v10, random.randint(random_min, random_max))
        edge5 = Edge(v01, v11, random.randint(random_min, random_max))
        Edge(v10, v20, random.randint(random_min, random_max))
        edge7 = Edge(v11, v21, random.randint(random_min, random_max))

        test_edges = sorted([edge1, edge3, edge4, edge5, edge7],
                            key=lambda x: x.weight())

        for index in range(len(kruskal_edges)):
            self.assertEqual(
                "({0}, {1})".format(
                    test_edges[index].from_vertice().name(),
                    test_edges[index].to_vertice().name()),
                "({0}, {1})".format(
                    kruskal_edges[index].from_vertice().name(),
                    kruskal_edges[index].to_vertice().name())
            )

    def test_three_by_two_graph(self):
        width = 3
        height = 2
        seed = 1
        g = Graph(width, height, seed)
        random_min = 0
        random_max = 10000

        kruskal_edges = kruskal(g)
        self.assertEqual(5, len(kruskal_edges))
        # o - o   o
        # |       |
        # o - o - o

        v00 = Vertice("(0, 0)")
        v01 = Vertice("(0, 1)")
        v02 = Vertice("(0, 2)")
        v10 = Vertice("(1, 0)")
        v11 = Vertice("(1, 1)")
        v12 = Vertice("(1, 2)")

        random.seed(seed)
        edge1 = Edge(v00, v01, random.randint(random_min, random_max))
        Edge(v01, v02, random.randint(random_min, random_max))
        edge3 = Edge(v10, v11, random.randint(random_min, random_max))
        edge4 = Edge(v11, v12, random.randint(random_min, random_max))
        edge5 = Edge(v00, v10, random.randint(random_min, random_max))
        Edge(v01, v11, random.randint(random_min, random_max))
        edge7 = Edge(v02, v12, random.randint(random_min, random_max))

        test_edges = sorted([edge1, edge3, edge4, edge5, edge7],
                            key=lambda x: x.weight())

        for index in range(len(kruskal_edges)):
            self.assertEqual(
                "({0}, {1})".format(
                    test_edges[index].from_vertice().name(),
                    test_edges[index].to_vertice().name()),
                "({0}, {1})".format(
                    kruskal_edges[index].from_vertice().name(),
                    kruskal_edges[index].to_vertice().name())
            )


    def test_two_by_two_graph(self):
        width = 2
        height = 2
        seed = 1
        g = Graph(width, height, seed)
        random_min = 0
        random_max = 10000

        kruskal_edges = kruskal(g)
        self.assertEqual(3, len(kruskal_edges))

        # o - o
        #     |
        # o - o

        #v(row)(col)
        v00 = Vertice("(0, 0)")
        v01 = Vertice("(0, 1)")
        v10 = Vertice("(1, 0)")
        v11 = Vertice("(1, 1)")

        random.seed(1)
        edge1 = Edge(v00, v01, random.randint(random_min, random_max))
        Edge(v10, v11, random.randint(random_min, random_max)) # Edge not needed
        edge3 = Edge(v00, v10, random.randint(random_min, random_max))
        edge4 = Edge(v01, v11, random.randint(random_min, random_max))
        test_edges = [edge3, edge1, edge4]

        for index in range(len(kruskal_edges)):
            self.assertEqual(
                "({0}, {1})".format(
                    test_edges[index].from_vertice().name(),
                    test_edges[index].to_vertice().name()),
                "({0}, {1})".format(
                    kruskal_edges[index].from_vertice().name(),
                    kruskal_edges[index].to_vertice().name())
            )

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
