from unittest import TestCase

from model.graph.Edge import Edge
from model.graph.PriorityQueue import PriorityQueue
from model.graph.Vertice import Vertice


class TestPriorityQueue(TestCase):
    """Test cases for the priority queue testing to see that equal weight edges
    can be pushed onto the priority queue, and that the priority queue works
    as intended of a priority queue."""

    def test_push_same_edge(self):
        v1 = Vertice("one")
        v2 = Vertice("two")

        edge = Edge(v1, v2)
        p = PriorityQueue()

        p.push(edge)
        p.push(edge)
        p.push(edge)
        self.assertFalse(p.is_empty())
        self.assertEqual(3, len(p))

    def test_push_edges(self):
        v1 = Vertice("one")
        v2 = Vertice("two")

        edge1 = Edge(v1, v2)
        edge2 = Edge(v2, v1)

        p = PriorityQueue()
        self.assertTrue(p.is_empty())
        self.assertEqual(0, len(p))

        p.push(edge1)
        self.assertFalse(p.is_empty())
        self.assertEqual(1, len(p))

        p.push(edge2)
        self.assertEqual(2, len(p))

    def test_simple_extraction(self):
        """Extracting the min from two edges should result in the minimum
        of the two edges being extracted"""
        v1 = Vertice("one")
        v2 = Vertice("two")

        edge1 = Edge(v1, v2, 0)
        edge2 = Edge(v1, v2, 1)

        p = PriorityQueue()
        p.push(edge1)
        p.push(edge2)

        self.assertEqual(2, len(p))
        self.assertEqual(edge1, p.extract_min())
        self.assertEqual(1, len(p))

        self.assertEqual(edge2, p.extract_min())
        self.assertTrue(p.is_empty())

    def test_multi_extraction(self):
        v1 = Vertice("one")
        v2 = Vertice("two")

        edge1 = Edge(v1, v2, 0)
        edge2 = Edge(v1, v2, 0)
        edge3 = Edge(v1, v2, 1)
        edge4 = Edge(v1, v2, 1)

        p = PriorityQueue()
        p.push(edge1)
        p.push(edge2)
        p.push(edge3)
        p.push(edge4)

        # we are less interested in the exact edges themselves
        # but rather the weight to justify the priority queue
        self.assertEqual(0, p.extract_min().weight())
        self.assertEqual(0, p.extract_min().weight())
        self.assertEqual(1, p.extract_min().weight())
        self.assertEqual(1, p.extract_min().weight())

        self.assertTrue(p.is_empty())

    def test_default_empty(self):
        self.assertTrue(PriorityQueue().is_empty())

    def test_default_length(self):
        self.assertEqual(0, len(PriorityQueue()))

    def test_invalid_extract(self):
        try:
            PriorityQueue().extract_min()
            self.fail("Should not be able to extract from an empty pq")
        except ValueError as e:
            self.assertEqual("Priority queue is empty", str(e))
