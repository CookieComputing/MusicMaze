from unittest import TestCase

from model.data_structures.Deque import Deque


class TestDeque(TestCase):
    """Test cases for the deque class that test for expected behavior of a
    deque, including both head and tail appends."""

    def test_empty_deque_length(self):
        d = Deque()
        self.assertEqual(0, len(d))

    def test_normal_push_head(self):
        d = Deque()
        d.push_head(2)

        self.assertEqual(2, d.peek_head())
        self.assertEqual(2, d.peek_tail())

    def test_normal_push_tail(self):
        d = Deque()
        d.push_tail(2)

        self.assertEqual(2, d.peek_head())
        self.assertEqual(2, d.peek_tail())

    def test_push_head_and_push_tail_different(self):
        d = Deque()
        d.push_head(1)
        d.push_tail(2)

        self.assertEqual(1, d.peek_head())
        self.assertEqual(2, d.peek_tail())

    def test_simple_pop_head(self):
        d = Deque()
        d.push_head(3)
        self.assertEqual(3, d.pop_head())

    def test_simple_pop_tail(self):
        d = Deque()
        d.push_tail(3)
        self.assertEqual(3, d.pop_tail())

    def test_push_and_pop_head(self):
        d = Deque()
        d.push_head(3)
        d.push_head(2)
        d.push_head(1)

        self.assertEqual(1, d.pop_head())
        self.assertEqual(2, d.pop_head())
        self.assertEqual(3, d.pop_head())

    def test_push_and_pop_tail(self):
        d = Deque()
        d.push_tail(1)
        d.push_tail(2)
        d.push_tail(3)

        self.assertEqual(3, d.pop_tail())
        self.assertEqual(2, d.pop_tail())
        self.assertEqual(1, d.pop_tail())

    def test_pop_and_peek_head(self):
        d = Deque()

        d.push_head(3)
        d.push_head(2)
        d.push_head(1)

        self.assertEqual(1, d.peek_head())
        self.assertEqual(1, d.pop_head())
        self.assertEqual(2, d.peek_head())
        self.assertEqual(2, d.pop_head())
        self.assertEqual(3, d.peek_head())
        self.assertEqual(3, d.pop_head())

    def test_length_changes_by_push_or_pop(self):
        d = Deque()

        self.assertEqual(0, len(d))

        d.push_head(1)
        self.assertEqual(1, len(d))

        d.push_tail(2)
        self.assertEqual(2, len(d))

        d.pop_head()
        self.assertEqual(1, len(d))

        d.pop_tail()
        self.assertEqual(0, len(d))
        self.assertFalse(d)

    def test_peek_does_not_change_length(self):
        d = Deque()

        d.push_tail(2)

        d.peek_head()
        self.assertEqual(1, len(d))

        d.peek_tail()
        self.assertEqual(1, len(d))

    def test_deque_non_trivial_push_pop(self):
        d = Deque()

        d.push_head(2)
        d.push_tail(3)
        d.push_head(1)
        d.push_tail(4)
        d.push_head(0)
        d.push_tail(5)
        d.push_tail(6)
        d.push_tail(7)

        self.assertEqual(8, len(d))
        self.assertEqual(0, d.peek_head())
        self.assertEqual(7, d.peek_tail())

        self.assertEqual(0, d.pop_head())
        self.assertEqual(1, d.peek_head())
        self.assertEqual(7, d.peek_tail())

        self.assertEqual(7, d.pop_tail())
        self.assertEqual(1, d.peek_head())
        self.assertEqual(6, d.peek_tail())

        self.assertEqual(6, len(d))

        # previously: 1 - 2 - 3 - 4 - 5 - 6
        d.pop_head()
        d.pop_head()
        d.pop_head()
        self.assertEqual(4, d.peek_head())
        self.assertEqual(6, d.peek_tail())

        d.pop_head()
        d.pop_head()

        self.assertEqual(6, d.peek_head())
        self.assertEqual(6, d.peek_tail())
        d.pop_head()

        self.assertFalse(d)
        self.assertEqual(0, len(d))

    def test_single_push_same_head_same_tail(self):
        d = Deque()

        d.push_head(2)
        self.assertEqual(2, d.peek_head())
        self.assertEqual(2, d.peek_tail())

    def test_non_empty_deque(self):
        d = Deque()

        self.assertFalse(d)
        d.push_head(32)
        self.assertTrue(d)

    def test_peek_head_empty_deque(self):
        d = Deque()

        try:
            d.peek_head()
            self.fail("Should not be able to peek head off empty deque")
        except IndexError as e:
            self.assertEqual("Deque is empty", str(e))

    def test_peek_tail_empty_deque(self):
        d = Deque()

        try:
            d.peek_tail()
            self.fail("Should not be able to peek tail off empty deque")
        except IndexError as e:
            self.assertEqual("Deque is empty", str(e))

    def test_pop_head_empty_deque(self):
        d = Deque()

        try:
            d.pop_head()
            self.fail("Should not be able to pop head off empty deque")
        except IndexError as e:
            self.assertEqual("Deque is empty", str(e))

    def test_pop_tail_empty_deque(self):
        d = Deque()

        try:
            d.pop_tail()
            self.fail("Should not be able to pop tail off empty deque")
        except IndexError as e:
            self.assertEqual("Deque is empty", str(e))
