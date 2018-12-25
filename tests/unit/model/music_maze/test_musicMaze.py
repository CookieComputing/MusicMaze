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

    def test_game_over(self):
        m = MusicMaze(7, 5, 3, 1)

        m_str = "O - O   O - O - O\n" \
                "|       |       |\n" \
                "O - O   O - X   O\n" \
                "    |   |       |\n" \
                "O - O - O - O   O"
        self.assertEqual(m_str, str(m))

        self.assertFalse(m.game_over())
        m.move_player(1, 2)
        self.assertFalse(m.game_over())
        m.move_player(0, 2)
        self.assertFalse(m.game_over())
        m.move_player(0, 3)
        self.assertFalse(m.game_over())
        m.move_player(0, 4)
        self.assertFalse(m.game_over())
        m.move_player(1, 4)
        self.assertFalse(m.game_over())
        m.move_player(2, 4)
        self.assertTrue(m.game_over())

        m.move_player(1, 4)
        self.assertFalse(m.game_over())

    def test_solution_path_two_by_two(self):
        m = MusicMaze(3, 2, 2, 1)

        m_str = "X - O\n" \
                "|   |\n" \
                "O   O"
        self.assertEqual(m_str, str(m))

        self.assertEqual(["(0, 0)", "(0, 1)", "(1, 1)"], m.solution_path())

    def test_solution_path_three_by_three(self):
        m = MusicMaze(5, 3, 3, 1)

        m_str = "X - O   O\n" \
                "|       |\n" \
                "O - O - O\n" \
                "    |   |\n" \
                "O - O   O"
        self.assertEqual(m_str, str(m))

        self.assertEqual(["(0, 0)", "(1, 0)", "(1, 1)", "(1, 2)", "(2, 2)"],
                         m.solution_path())

    def test_solution_path_four_by_four(self):
        m = MusicMaze(7, 4, 4, 1)

        m_str = "X - O   O - O\n" \
                "|       |    \n" \
                "O - O - O   O\n" \
                "|       |   |\n" \
                "O   O   O - O\n" \
                "    |   |   |\n" \
                "O - O - O   O"
        self.assertEqual(m_str, str(m))

        self.assertEqual(["(0, 0)", "(1, 0)", "(1, 1)", "(1, 2)",
                          "(2, 2)", "(2, 3)", "(3, 3)"],
                         m.solution_path())

    def test_solution_path_three_by_five(self):
        m = MusicMaze(7, 5, 3, 1)

        m_str = "O - O   O - O - O\n" \
                "|       |       |\n" \
                "O - O   O - X   O\n" \
                "    |   |       |\n" \
                "O - O - O - O   O"
        self.assertEqual(m_str, str(m))

        self.assertEqual(["(1, 3)", "(1, 2)", "(0, 2)",
                          "(0, 3)", "(0, 4)", "(1, 4)", "(2, 4)"],
                         m.solution_path())

    def test_solution_path_five_by_three(self):
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

        self.assertEqual(["(3, 1)", "(2, 1)", "(2, 0)", "(3, 0)",
                          "(4, 0)", "(4, 1)", "(4, 2)"],
                         m.solution_path())

    def test_get_player_pos(self):
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

        self.assertEqual("(3, 1)", str(m.get_player_position()))
        m.move_player(2, 1)
        self.assertEqual("(2, 1)", str(m.get_player_position()))
        m.move_player(2, 0)
        self.assertEqual("(2, 0)", str(m.get_player_position()))
        m.move_player(2, 1)
        self.assertEqual("(2, 1)", str(m.get_player_position()))
        m.move_player(3, 1)
        self.assertEqual("(3, 1)", str(m.get_player_position()))

    def test_random_distance_positions_four_by_four(self):
        m = MusicMaze(7, 4, 4, 1)

        m_str = "X - O   O - O\n" \
                "|       |    \n" \
                "O - O - O   O\n" \
                "|       |   |\n" \
                "O   O   O - O\n" \
                "    |   |   |\n" \
                "O - O - O   O"
        self.assertEqual(m_str, str(m))

        # solution path should all be zero
        self.assertEqual(0, m.distance_from_path(0, 0))
        self.assertEqual(0, m.distance_from_path(1, 0))
        self.assertEqual(0, m.distance_from_path(1, 1))
        self.assertEqual(0, m.distance_from_path(1, 2))
        self.assertEqual(0, m.distance_from_path(2, 2))
        self.assertEqual(0, m.distance_from_path(2, 3))
        self.assertEqual(0, m.distance_from_path(3, 3))

        self.assertEqual(1, m.distance_from_path(0, 1))
        self.assertEqual(1, m.distance_from_path(2, 0))
        self.assertEqual(1, m.distance_from_path(0, 2))
        self.assertEqual(1, m.distance_from_path(3, 2))
        self.assertEqual(1, m.distance_from_path(1, 3))

        self.assertEqual(2, m.distance_from_path(0, 3))
        self.assertEqual(2, m.distance_from_path(3, 1))

        self.assertEqual(3, m.distance_from_path(3, 0))
        self.assertEqual(3, m.distance_from_path(2, 1))

    def test_random_distance_positions_three_by_five(self):
        m = MusicMaze(7, 5, 3, 1)

        m_str = "O - O   O - O - O\n" \
                "|       |       |\n" \
                "O - O   O - X   O\n" \
                "    |   |       |\n" \
                "O - O - O - O   O"
        self.assertEqual(m_str, str(m))

        # solution path should all be zero
        self.assertEqual(0, m.distance_from_path(1, 3))
        self.assertEqual(0, m.distance_from_path(1, 2))
        self.assertEqual(0, m.distance_from_path(0, 2))
        self.assertEqual(0, m.distance_from_path(0, 3))
        self.assertEqual(0, m.distance_from_path(0, 4))
        self.assertEqual(0, m.distance_from_path(1, 4))
        self.assertEqual(0, m.distance_from_path(2, 4))

        self.assertEqual(1, m.distance_from_path(2, 2))

        self.assertEqual(2, m.distance_from_path(2, 3))
        self.assertEqual(2, m.distance_from_path(2, 1))

        self.assertEqual(3, m.distance_from_path(2, 0))
        self.assertEqual(3, m.distance_from_path(1, 1))

        self.assertEqual(4, m.distance_from_path(1, 0))

        self.assertEqual(5, m.distance_from_path(0, 0))

        self.assertEqual(6, m.distance_from_path(0, 1))

    def test_random_distance_positions_five_by_three(self):
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

        # solution path should all be zero
        self.assertEqual(0, m.distance_from_path(3, 1))
        self.assertEqual(0, m.distance_from_path(2, 1))
        self.assertEqual(0, m.distance_from_path(2, 0))
        self.assertEqual(0, m.distance_from_path(3, 0))
        self.assertEqual(0, m.distance_from_path(4, 0))
        self.assertEqual(0, m.distance_from_path(4, 1))
        self.assertEqual(0, m.distance_from_path(4, 2))

        self.assertEqual(1, m.distance_from_path(1, 0))
        self.assertEqual(1, m.distance_from_path(3, 2))

        self.assertEqual(2, m.distance_from_path(0, 0))
        self.assertEqual(2, m.distance_from_path(1, 1))

        self.assertEqual(3, m.distance_from_path(0, 1))
        self.assertEqual(3, m.distance_from_path(1, 2))

        self.assertEqual(4, m.distance_from_path(0, 2))

    def test_cells_two_by_two(self):
        m = MusicMaze(3, 2, 2)

        self.assertCountEqual(["(0, 0)", "(0, 1)", "(1, 0)", "(1, 1)"],
                              m.get_cells())

    def test_cells_three_by_three(self):
        m = MusicMaze(5, 3, 3)

        self.assertCountEqual(["(0, 0)", "(0, 1)", "(0, 2)",
                               "(1, 0)", "(1, 1)", "(1, 2)",
                               "(2, 0)", "(2, 1)", "(2, 2)"],
                              m.get_cells())

    def test_cells_five_by_three(self):
        m = MusicMaze(7, 3, 5)

        self.assertCountEqual(["(0, 0)", "(0, 1)", "(0, 2)",
                               "(1, 0)", "(1, 1)", "(1, 2)",
                               "(2, 0)", "(2, 1)", "(2, 2)",
                               "(3, 0)", "(3, 1)", "(3, 2)",
                               "(4, 0)", "(4, 1)", "(4, 2)"],
                              m.get_cells())

    def test_cells_three_by_five(self):
        m = MusicMaze(7, 5, 3)

        self.assertCountEqual(["(0, 0)", "(0, 1)", "(0, 2)", "(0, 3)", "(0, 4)",
                               "(1, 0)", "(1, 1)", "(1, 2)", "(1, 3)", "(1, 4)",
                               "(2, 0)", "(2, 1)", "(2, 2)", "(2, 3)", "(2, 4)"]
                              , m.get_cells())

    def test_get_neighbors_two_by_two(self):
        m = MusicMaze(3, 2, 2, 1)

        m_str = "X - O\n" \
                "|   |\n" \
                "O   O"
        self.assertEqual(m_str, str(m))

        self.assertCountEqual(["(1, 0)", "(0, 1)"],
                              m.get_connected_neighbors(0, 0))

        self.assertCountEqual(["(0, 0)"], m.get_connected_neighbors(1, 0))
        self.assertCountEqual(["(0, 0)", "(1, 1)"],
                              m.get_connected_neighbors(0, 1))
        self.assertCountEqual(["(0, 1)"], m.get_connected_neighbors(1, 1))

    def test_get_neighbors_three_by_five(self):
        m = MusicMaze(7, 5, 3, 1)

        m_str = "O - O   O - O - O\n" \
                "|       |       |\n" \
                "O - O   O - X   O\n" \
                "    |   |       |\n" \
                "O - O - O - O   O"
        self.assertEqual(m_str, str(m))

        self.assertCountEqual(["(0, 1)", "(1, 0)"],
                              m.get_connected_neighbors(0, 0))
        self.assertCountEqual(["(2, 1)"], m.get_connected_neighbors(2, 0))
        self.assertCountEqual(["(2, 0)", "(1, 1)", "(2, 2)"],
                              m.get_connected_neighbors(2, 1))
        self.assertCountEqual(["(0, 2)", "(1, 3)", "(2, 2)"],
                              m.get_connected_neighbors(1, 2))
        self.assertCountEqual(["(0, 3)", "(1, 4)"],
                              m.get_connected_neighbors(0, 4))
        self.assertCountEqual(["(1, 4)"], m.get_connected_neighbors(2, 4))

    def test_restart_three_by_five(self):
        m = MusicMaze(7, 5, 3, 1)

        m_str = "O - O   O - O - O\n" \
                "|       |       |\n" \
                "O - O   O - X   O\n" \
                "    |   |       |\n" \
                "O - O - O - O   O"
        self.assertEqual(m_str, str(m))

        m.restart()
        self.assertEqual(m_str, str(m))

        m.move_player(1, 2)
        m.move_player(2, 2)
        m.move_player(2, 1)
        m.move_player(2, 0)
        m_str_four_move = "O - O   O - O - O\n" \
                          "|       |       |\n" \
                          "O - O   O - O   O\n" \
                          "    |   |       |\n" \
                          "X - O - O - O   O"
        self.assertEqual(m_str_four_move, str(m))

        m.restart()
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

    def test_negative_row_distance_check(self):
        m = MusicMaze(3, 2, 2)

        try:
            m.distance_from_path(-1, 0)
            self.fail("Should not be able to check negative distances")
        except ValueError as e:
            self.assertEqual("Given invalid position", str(e))

    def test_negative_col_distance_check(self):
        m = MusicMaze(3, 2, 2)

        try:
            m.distance_from_path(0, -1)
            self.fail("Should not be able to check negative distances")
        except ValueError as e:
            self.assertEqual("Given invalid position", str(e))

    def test_out_of_bounds_row_distance_check(self):
        m = MusicMaze(7, 3, 5)

        try:
            m.distance_from_path(6,0)
            self.fail("Should not be able to check out of bounds distances")
        except ValueError as e:
            self.assertEqual("Given invalid position", str(e))

    def test_out_of_bounds_col_distance_check(self):
        m = MusicMaze(7, 5, 3)

        try:
            m.distance_from_path(0, 6)
            self.fail("Should not be able to check out of bounds distances")
        except ValueError as e:
            self.assertEqual("Given invalid position", str(e))

    def test_illegal_value_for_maze_neighbors(self):
        model_maze = MusicMaze(3, 2, 2)

        try:
            model_maze.get_connected_neighbors(-1, 0)
            self.fail("Should not be able to get connected components")
        except IndexError as e:
            self.assertEqual("Maze does not contain vertice", str(e))
