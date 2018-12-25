from unittest import TestCase

from model.data_structures.Queue import Queue


class TestQueue(TestCase):

    def test_push_pop_changes_size(self):
        q = Queue()

        self.assertEqual(0, len(q))

        q.enqueue(1)
        self.assertEqual(1, len(q))

        q.enqueue(2)
        self.assertEqual(2, len(q))

        q.dequeue()
        self.assertEqual(1, len(q))

        q.dequeue()
        self.assertEqual(0, len(q))

    def test_push_peek_pop_ordering(self):
        q = Queue()

        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)

        self.assertEqual(1, q.peek())
        self.assertEqual(1, q.dequeue())
        self.assertEqual(2, q.peek())
        self.assertEqual(2, q.dequeue())
        self.assertEqual(3, q.peek())
        self.assertEqual(3, q.dequeue())

    def test_peek_checks_first_entry(self):
        q = Queue()

        q.enqueue(1)
        q.enqueue(2)

        self.assertEqual(1, q.peek())

    def test_push_peek(self):
        q = Queue()

        q.enqueue(10)
        self.assertEqual(1, len(q))
        self.assertEqual(10, q.peek())

    def test_peek_empty_queue(self):
        q = Queue()

        try:
            q.peek()
            self.fail("Should not be able to peek empty queue")
        except IndexError as e:
            self.assertEqual("Queue is empty", str(e))

    def test_pop_empty_queue(self):
        q = Queue()

        try:
            q.dequeue()
            self.fail("Should not be able to dequeue empty queue")
        except IndexError as e:
            self.assertEqual("Queue is empty", str(e))

    def test_empty_queue_length_and_bool(self):
        q = Queue()

        self.assertEqual(0, len(q))
        self.assertFalse(q)
