from unittest import TestCase

from model.data_structures.Stack import Stack


class TestStack(TestCase):

    def test_push_pop_ordering(self):
        s = Stack()

        s.push(3)
        s.push(2)
        s.push(1)

        self.assertEqual(1, s.peek())
        self.assertEqual(1, s.pop())
        self.assertEqual(2, s.peek())
        self.assertEqual(2, s.pop())
        self.assertEqual(3, s.peek())
        self.assertEqual(3, s.pop())

    def test_peek_checks_last_pushed(self):
        s = Stack()

        s.push(1)
        s.push(2)
        s.push(3)

        self.assertEqual(3, s.peek())

    def test_push_pop_changes_size(self):
        s = Stack()

        self.assertEqual(0, len(s))
        s.push(1)
        self.assertEqual(1, len(s))
        s.push(2)
        self.assertEqual(2, len(s))

        s.pop()
        self.assertEqual(1, len(s))

        s.pop()
        self.assertEqual(0, len(s))

    def test_pop_empty_stack(self):
        s = Stack()

        try:
            s.pop()
            self.fail("Should not be able to pop empty stack")
        except IndexError as e:
            self.assertEqual("Stack is empty", str(e))

    def test_peek_empty_stack(self):
        s = Stack()

        try:
            s.peek()
            self.fail("Should not be able to peek empty stack")
        except IndexError as e:
            self.assertEqual("Stack is empty", str(e))

    def test_empty_stack_len_bool(self):
        s = Stack()

        self.assertEqual(0, len(s))
        self.assertFalse(s)
