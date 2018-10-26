from unittest import TestCase

from maze_generator.Vertice import Vertice


class TestVertice(TestCase):
    """This class represents examples and test cases for a vertice in a graph"""

    def test_adding_neigbhors_to_vertice(self):
        """Adding neighbors should be directional, only."""

        vertice1 = Vertice("one")
        vertice2 = Vertice("two")
        vertice3 = Vertice("three")

        self.assertEqual([], vertice1.neighbors())
        self.assertEqual([], vertice2.neighbors())
        self.assertEqual([], vertice3.neighbors())

        # should be directional
        vertice1.add_neighbor(vertice2)
        self.assertEqual([vertice2], vertice1.neighbors())
        self.assertEqual([], vertice2.neighbors())

        # other vertices should also not experience side effects
        vertice1.add_neighbor(vertice3)
        self.assertEqual([vertice2, vertice3], vertice1.neighbors())
        self.assertEqual([], vertice2.neighbors())
        self.assertEqual([], vertice3.neighbors())

        vertice2.add_neighbor(vertice1)
        self.assertEqual([vertice2, vertice3], vertice1.neighbors())
        self.assertEqual([vertice1], vertice2.neighbors())
        self.assertEqual([], vertice3.neighbors())

    def test_is_neighbor(self):
        """Testing directional behavior of vertices."""

        vertice1 = Vertice("one")
        vertice2 = Vertice("two")

        self.assertFalse(vertice1.is_neighbor(vertice2))
        self.assertFalse(vertice2.is_neighbor(vertice1))

        vertice1.add_neighbor(vertice2)
        self.assertTrue(vertice1.is_neighbor(vertice2))
        self.assertFalse(vertice2.is_neighbor(vertice1))

    def test_name(self):
        vertice1 = Vertice("one")
        vertice2 = Vertice("two")

        self.assertEqual("one", vertice1.name())
        self.assertEqual("two", vertice2.name())

    def test_vertice_with_null_name(self):
        try:
            Vertice("")
            self.fail("Vertice constructor should fail with null string")
        except ValueError as e:
            self.assertEqual("Given null name in vertice", str(e))

    def test_vertice_given_bad_neighbor(self):
        try:
            v = Vertice("some node")
            v.add_neighbor(None)
            self.fail("Should fail if the given neighbor is empty")
        except ValueError as e:
            self.assertEqual("Given invalid neighbor", str(e))

    def test_vertice_given_self_neighbor(self):
        """We define giving oneself as a neighbor as a potential cycle and
        remove it, enforcing a simple graph in our maze instead."""

        try:
            v = Vertice("self referential")
            v.add_neighbor(v)
            self.fail("Should not allow self referential neighboring")
        except ValueError as e:
            self.assertEqual("Vertice cannot become it's own neighbor", str(e))

    def test_vertice_given_duplicate(self):
        """Duplicate neighbors are considered illegal behavior"""
        vertice1 = Vertice("one")
        vertice2 = Vertice("two")

        vertice1.add_neighbor(vertice2)
        try:
            vertice1.add_neighbor(vertice2)
            self.fail("Should not be able to add a duplicate neighbor")
        except ValueError as e:
            self.assertEqual("Attempting to add duplicate neighbor", str(e))