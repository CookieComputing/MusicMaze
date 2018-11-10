from unittest import TestCase

from model.graph.Vertice import Vertice


class TestVertice(TestCase):
    """This class represents examples and test cases for a vertice in a graph"""

    def test_adding_neighbors_to_vertice(self):
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
        self.assertEqual(2, len(vertice1.neighbors()))
        self.assertTrue(vertice2 in vertice1.neighbors())
        self.assertTrue(vertice3 in vertice1.neighbors())
        self.assertEqual([], vertice2.neighbors())
        self.assertEqual([], vertice3.neighbors())

        vertice2.add_neighbor(vertice1)
        self.assertEqual(2, len(vertice1.neighbors()))
        self.assertTrue(vertice2 in vertice1.neighbors())
        self.assertTrue(vertice3 in vertice1.neighbors())
        self.assertEqual(1, len(vertice2.neighbors()))
        self.assertTrue(vertice1 in vertice2.neighbors())
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

    def test_remove_single_neighbor_single_direction(self):
        vertice1 = Vertice("one")
        vertice2 = Vertice("two")

        vertice1.add_neighbor(vertice2)
        vertice2.add_neighbor(vertice1)

        self.assertTrue(vertice1.is_neighbor(vertice2))
        self.assertTrue(vertice2.is_neighbor(vertice1))

        vertice1.remove_neighbor(vertice2)
        self.assertFalse(vertice1.is_neighbor(vertice2))
        self.assertTrue(vertice2.is_neighbor(vertice1))

    def test_remove_single_neighbor_one_direction(self):
        vertice1 = Vertice("one")
        vertice2 = Vertice("two")

        vertice1.add_neighbor(vertice2)

        self.assertTrue(vertice1.is_neighbor(vertice2))
        self.assertFalse(vertice2.is_neighbor(vertice1))

        vertice1.remove_neighbor(vertice2)
        self.assertFalse(vertice1.is_neighbor(vertice2))
        self.assertFalse(vertice2.is_neighbor(vertice1))

    def test_remove_single_neighbor_multiple_neighbors(self):
        vertice1 = Vertice("one")
        vertice2 = Vertice("two")
        vertice3 = Vertice("three")

        vertice1.add_neighbor(vertice2)
        vertice1.add_neighbor(vertice3)

        self.assertTrue(vertice1.is_neighbor(vertice2))
        self.assertTrue(vertice1.is_neighbor(vertice3))
        vertice1.remove_neighbor(vertice2)
        self.assertFalse(vertice1.is_neighbor(vertice2))
        self.assertTrue(vertice1.is_neighbor(vertice3))

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

    def test_remove_non_existent_neighbor(self):
        vertice = Vertice("one")
        try:
            vertice.remove_neighbor(Vertice("non existent"))
            self.fail("Should not be able to remove a non existent vertice")
        except ValueError as e:
            self.assertEqual("Neighbor does not exist to remove", str(e))

    def test_remove_vertice_with_same_name_as_neighbor(self):
        vertice1 = Vertice("one")
        vertice2 = Vertice("two")

        vertice1.add_neighbor(vertice2)
        try:
            vertice1.remove_neighbor(Vertice("two"))
            self.fail("A vertice with the same name does not "
                      "count as the same neighbor")
        except ValueError as e:
            self.assertEqual("Given vertice "
                             "is not the actual vertice neighbor", str(e))
