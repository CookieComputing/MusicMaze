from unittest import TestCase

from model.music_maze.MusicMaze import MusicMaze


class TestMusicMaze(TestCase):
    """This class represents test cases for the music maze. Most of the tests
    take advantage of the string representation of the maze to visually
    verify if a move has been appropriately made."""

    def test_two_by_two_maze_state(self):
        """Kept at a bare minimum to avoid having to detect different starting
        positions"""
        m = MusicMaze(3, 2, 2, 1)

        m_str = "X - O\n" \
                "|   |\n" \
                "O   O"
        self.assertEqual(m_str, str(m))

    def test_three_by_three_maze_state(self):
        """Kept at a bare minimum to avoid having to detect different starting
        positions"""
        m = MusicMaze(5, 3, 3, 1)

        m_str = "X - O   O\n" \
                "|       |\n" \
                "O - O - O\n" \
                "    |   |\n" \
                "O - O   O"
        self.assertEqual(m_str, str(m))

    def test_four_by_four_maze_state(self):
        """Kept at a bare minimum to avoid having to detect different starting
        positions"""

        m = MusicMaze(7, 4, 4, 1)

        m_str = "X - O   O - O\n" \
                "|       |    \n" \
                "O - O - O   O\n" \
                "|       |   |\n" \
                "O   O   O - O\n" \
                "    |   |   |\n" \
                "O - O - O   O"
        self.assertEqual(m_str, str(m))

    def test_three_by_five_maze_state(self):
        """Kept at a bare minimum to avoid having to detect different starting
        positions"""

        m = MusicMaze(7, 5, 3, 1)

        m_str = "O - O   O - O - O\n" \
                "|       |       |\n" \
                "O - O   O - X   O\n" \
                "    |   |       |\n" \
                "O - O - O - O   O"
        self.assertEqual(m_str, str(m))

    def test_five_by_three_maze_state(self):
        """Kept at a bare minimum to avoid having to detect different starting
        positions"""

        m = MusicMaze(7, 3, 5, 1)

        m_str = "O - O   O\n" \
                "|       |\n" \
                "O - O - O\n" \
                "|        \n" \
                "O - O   O\n" \
                "|   |   |\n" \
                "O   X   O\n" \
                "|       |\n" \
                "O - O - O"
        self.assertEqual(m_str, str(m))

    def test_two_by_two_movement(self):
        m = MusicMaze(3, 2, 2, 1)

        m_str = "X - O\n" \
                "|   |\n" \
                "O   O"
        self.assertEqual(m_str, str(m))

        m.move_player(1, 0)
        m_str = "O - O\n" \
                "|   |\n" \
                "X   O"
        self.assertEqual(m_str, str(m))

        m.move_player(0, 0)
        m_str = "X - O\n" \
                "|   |\n" \
                "O   O"
        self.assertEqual(m_str, str(m))

        m.move_player(0, 1)
        m_str = "O - X\n" \
                "|   |\n" \
                "O   O"
        self.assertEqual(m_str, str(m))

        m.move_player(1, 1)
        m_str = "O - O\n" \
                "|   |\n" \
                "O   X"
        self.assertEqual(m_str, str(m))

    def test_four_by_four_movement(self):
        m = MusicMaze(7, 4, 4, 1)

        m_str = "X - O   O - O\n" \
                "|       |    \n" \
                "O - O - O   O\n" \
                "|       |   |\n" \
                "O   O   O - O\n" \
                "    |   |   |\n" \
                "O - O - O   O"
        self.assertEqual(m_str, str(m))

        m.move_player(0, 1)
        m_str = "O - X   O - O\n" \
                "|       |    \n" \
                "O - O - O   O\n" \
                "|       |   |\n" \
                "O   O   O - O\n" \
                "    |   |   |\n" \
                "O - O - O   O"
        self.assertEqual(m_str, str(m))

        m.move_player(0, 0)
        m_str = "X - O   O - O\n" \
                "|       |    \n" \
                "O - O - O   O\n" \
                "|       |   |\n" \
                "O   O   O - O\n" \
                "    |   |   |\n" \
                "O - O - O   O"
        self.assertEqual(m_str, str(m))

        m.move_player(1, 0)
        m_str = "O - O   O - O\n" \
                "|       |    \n" \
                "X - O - O   O\n" \
                "|       |   |\n" \
                "O   O   O - O\n" \
                "    |   |   |\n" \
                "O - O - O   O"
        self.assertEqual(m_str, str(m))

        m.move_player(2, 0)
        m_str = "O - O   O - O\n" \
                "|       |    \n" \
                "O - O - O   O\n" \
                "|       |   |\n" \
                "X   O   O - O\n" \
                "    |   |   |\n" \
                "O - O - O   O"
        self.assertEqual(m_str, str(m))

        # skipping to interesting points
        m.move_player(1, 0)
        m.move_player(1, 1)
        m.move_player(1, 2)
        m.move_player(0, 2)
        m.move_player(0, 3)

        m_str = "O - O   O - X\n" \
                "|       |    \n" \
                "O - O - O   O\n" \
                "|       |   |\n" \
                "O   O   O - O\n" \
                "    |   |   |\n" \
                "O - O - O   O"
        self.assertEqual(m_str, str(m))

        m.move_player(0, 2)
        m.move_player(1, 2)
        m.move_player(2, 2)
        m.move_player(2, 3)
        m.move_player(3, 3)

        m_str = "O - O   O - O\n" \
                "|       |    \n" \
                "O - O - O   O\n" \
                "|       |   |\n" \
                "O   O   O - O\n" \
                "    |   |   |\n" \
                "O - O - O   X"
        self.assertEqual(m_str, str(m))

        m.move_player(2, 3)
        m.move_player(2, 2)
        m.move_player(3, 2)
        m.move_player(3, 1)
        m.move_player(3, 0)

        m_str = "O - O   O - O\n" \
                "|       |    \n" \
                "O - O - O   O\n" \
                "|       |   |\n" \
                "O   O   O - O\n" \
                "    |   |   |\n" \
                "X - O - O   O"
        self.assertEqual(m_str, str(m))

    def test_three_by_five_movement(self):
        m = MusicMaze(7, 5, 3, 1)

        m_str = "O - O   O - O - O\n" \
                "|       |       |\n" \
                "O - O   O - X   O\n" \
                "    |   |       |\n" \
                "O - O - O - O   O"
        self.assertEqual(m_str, str(m))

        m.move_player(1, 2)
        m.move_player(2, 2)
        m.move_player(2, 1)
        m.move_player(2, 0)
        m_str = "O - O   O - O - O\n" \
                "|       |       |\n" \
                "O - O   O - O   O\n" \
                "    |   |       |\n" \
                "X - O - O - O   O"
        self.assertEqual(m_str, str(m))

        m.move_player(2, 1)
        m.move_player(1, 1)
        m.move_player(1, 0)
        m.move_player(0, 0)
        m.move_player(0, 1)

        m_str = "O - X   O - O - O\n" \
                "|       |       |\n" \
                "O - O   O - O   O\n" \
                "    |   |       |\n" \
                "O - O - O - O   O"
        self.assertEqual(m_str, str(m))

        m.move_player(0, 0)
        m.move_player(1, 0)
        m.move_player(1, 1)
        m.move_player(2, 1)
        m.move_player(2, 2)
        m.move_player(1, 2)
        m.move_player(0, 2)
        m.move_player(0, 3)
        m.move_player(0, 4)
        m.move_player(1, 4)
        m.move_player(2, 4)

        m_str = "O - O   O - O - O\n" \
                "|       |       |\n" \
                "O - O   O - O   O\n" \
                "    |   |       |\n" \
                "O - O - O - O   X"
        self.assertEqual(m_str, str(m))

    def test_five_by_three_movement(self):
        """Kept at a bare minimum to avoid having to detect different starting
        positions"""

        m = MusicMaze(7, 3, 5, 1)

        m_str = "O - O   O\n" \
                "|       |\n" \
                "O - O - O\n" \
                "|        \n" \
                "O - O   O\n" \
                "|   |   |\n" \
                "O   X   O\n" \
                "|       |\n" \
                "O - O - O"
        self.assertEqual(m_str, str(m))

        m.move_player(2, 1)
        m.move_player(2, 0)
        m.move_player(1, 0)
        m.move_player(0, 0)
        m.move_player(0, 1)

        m_str = "O - X   O\n" \
                "|       |\n" \
                "O - O - O\n" \
                "|        \n" \
                "O - O   O\n" \
                "|   |   |\n" \
                "O   O   O\n" \
                "|       |\n" \
                "O - O - O"
        self.assertEqual(m_str, str(m))

        m.move_player(0, 0)
        m.move_player(1, 0)
        m.move_player(1, 1)
        m.move_player(1, 2)
        m.move_player(0, 2)

        m_str = "O - O   X\n" \
                "|       |\n" \
                "O - O - O\n" \
                "|        \n" \
                "O - O   O\n" \
                "|   |   |\n" \
                "O   O   O\n" \
                "|       |\n" \
                "O - O - O"
        self.assertEqual(m_str, str(m))

        m.move_player(1, 2)
        m.move_player(1, 1)
        m.move_player(1, 0)
        m.move_player(2, 0)
        m.move_player(3, 0)
        m.move_player(4, 0)
        m.move_player(4, 1)
        m.move_player(4, 2)
        m.move_player(3, 2)
        m.move_player(2, 2)

        m_str = "O - O   O\n" \
                "|       |\n" \
                "O - O - O\n" \
                "|        \n" \
                "O - O   X\n" \
                "|   |   |\n" \
                "O   O   O\n" \
                "|       |\n" \
                "O - O - O"
        self.assertEqual(m_str, str(m))

    def test_negative_length_constructor(self):
        try:
            MusicMaze(-1, 2, 3)
            self.fail("Should not be able to give negative length")
        except ValueError as e:
            self.assertEqual("Given invalid maze dimension", str(e))

    def test_zero_length_constructor(self):
        try:
            MusicMaze(0, 2, 3)
            self.fail("Should not be able to given zero length")
        except ValueError as e:
            self.assertEqual("Given invalid maze dimension", str(e))

    def test_negative_width_constructor(self):
        try:
            MusicMaze(2, -1, 3)
            self.fail("Should not be able to give negative width")
        except ValueError as e:
            self.assertEqual("Given invalid maze dimension", str(e))

    def test_zero_width_constructor(self):
        try:
            MusicMaze(5, 0, 3)
            self.fail("Should not be able to given zero width")
        except ValueError as e:
            self.assertEqual("Given invalid maze dimension", str(e))

    def test_negative_height_constructor(self):
        try:
            MusicMaze(2, 3, -1)
            self.fail("Should not be able to give negative height")
        except ValueError as e:
            self.assertEqual("Given invalid maze dimension", str(e))

    def test_zero_height_constructor(self):
        try:
            MusicMaze(5, 5, 0)
            self.fail("Should not be able to given zero height")
        except ValueError as e:
            self.assertEqual("Given invalid maze dimension", str(e))

    def test_bad_maze_sizes(self):
        try:
            MusicMaze(8, 4, 3)
            self.fail("Should not be able to make a maze that fails to "
                      "satisfy the requirements")
        except ValueError as e:
            self.assertEqual("Given width and height cannot"
                             " guarantee path length", str(e))

    def test_illegal_move_out_of_bounds_left(self):
        m = MusicMaze(3, 2, 2, 1)

        m_str = "X - O\n" \
                "|   |\n" \
                "O   O"
        self.assertEqual(m_str, str(m))

        try:
            m.move_player(-1, 0)
            self.fail("Cannot move out of bounds left")
        except ValueError as e:
            self.assertEqual("Cannot move to given location", str(e))

    def test_illegal_move_out_of_bounds_up(self):
        m = MusicMaze(3, 2, 2, 1)

        m_str = "X - O\n" \
                "|   |\n" \
                "O   O"
        self.assertEqual(m_str, str(m))

        try:
            m.move_player(0, -1)
            self.fail("Cannot move out of bounds up")
        except ValueError as e:
            self.assertEqual("Cannot move to given location", str(e))

    def test_illegal_move_out_of_bounds_down(self):
        m = MusicMaze(3, 2, 2, 1)

        m_str = "X - O\n" \
                "|   |\n" \
                "O   O"
        self.assertEqual(m_str, str(m))

        m.move_player(1, 0)

        try:
            m.move_player(2, 0)
            self.fail("cannot move out of bounds down")
        except ValueError as e:
            self.assertEqual("Cannot move to given location", str(e))

    def test_illegal_move_out_of_bounds_right(self):
        m = MusicMaze(3, 2, 2, 1)

        m_str = "X - O\n" \
                "|   |\n" \
                "O   O"
        self.assertEqual(m_str, str(m))

        m.move_player(1, 0)

        try:
            m.move_player(0, 2)
            self.fail("cannot move out of bounds down")
        except ValueError as e:
            self.assertEqual("Cannot move to given location", str(e))

    def test_illegal_move_cannot_jump_across_gap(self):
        m = MusicMaze(3, 2, 2, 1)

        m_str = "X - O\n" \
                "|   |\n" \
                "O   O"
        self.assertEqual(m_str, str(m))

        m.move_player(1, 0)

        try:
            m.move_player(1, 1)
            self.fail("Cannot jump across gap")
        except ValueError as e:
            self.assertEqual("Cannot move to given location", str(e))

    def test_illegal_move_cannot_jump_past_other_nodes(self):
        m = MusicMaze(7, 4, 4, 1)

        m_str = "X - O   O - O\n" \
                "|       |    \n" \
                "O - O - O   O\n" \
                "|       |   |\n" \
                "O   O   O - O\n" \
                "    |   |   |\n" \
                "O - O - O   O"
        self.assertEqual(m_str, str(m))

        try:
            m.move_player(2, 0)
            self.fail("Cannot jump past other nodes")
        except ValueError as e:
            self.assertEqual("Cannot move to given location", str(e))

    def test_illegal_move_cannot_teleport_to_end(self):
        m = MusicMaze(7, 4, 4, 1)

        m_str = "X - O   O - O\n" \
                "|       |    \n" \
                "O - O - O   O\n" \
                "|       |   |\n" \
                "O   O   O - O\n" \
                "    |   |   |\n" \
                "O - O - O   O"
        self.assertEqual(m_str, str(m))

        try:
            m.move_player(3, 3)
            self.fail("Cannot teleport to the end")
        except ValueError as e:
            self.assertEqual("Cannot move to given location", str(e))
