from unittest import TestCase

from model.music_maze.MazeState import MazeState
from model.music_maze.MusicMaze import MusicMaze


class TestMazeState(TestCase):

    def test_two_by_two_get_cell(self):
        m = MazeState(MusicMaze(3, 2, 2))

        self.assertCountEqual([(0, 0), (0, 1),
                               (1, 0), (1, 1)],
                              m.get_cells())

    def test_three_by_three_get_cell(self):
        m = MazeState(MusicMaze(5, 3, 3))
        self.assertCountEqual([(0, 0), (0, 1), (0, 2),
                               (1, 0), (1, 1), (1, 2),
                               (2, 0), (2, 1), (2, 2)],
                              m.get_cells())

    def test_three_by_five_get_cell(self):
        m = MazeState(MusicMaze(7, 5, 3))

        self.assertCountEqual([(0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
                               (1, 0), (1, 1), (1, 2), (1, 3), (1, 4),
                               (2, 0), (2, 1), (2, 2), (2, 3), (2, 4)],
                              m.get_cells())

    def test_five_by_three_get_cell(self):
        m = MazeState(MusicMaze(7, 3, 5))

        self.assertCountEqual([(0, 0), (0, 1), (0, 2),
                               (1, 0), (1, 1), (1, 2),
                               (2, 0), (2, 1), (2, 2),
                               (3, 0), (3, 1), (3, 2),
                               (4, 0), (4, 1), (4, 2)],
                              m.get_cells())

    def test_two_by_two_player_position(self):
        m = MazeState(MusicMaze(3, 2, 2))

        self.assertEqual((0, 0), m.get_player_position())

    def test_three_by_three_player_position(self):
        model_maze = MusicMaze(5, 3, 3, 1)

        m_str = "X - O   O\n" \
                "|       |\n" \
                "O - O - O\n" \
                "    |   |\n" \
                "O - O   O"
        self.assertEqual(m_str, str(model_maze))
        m = MazeState(model_maze)

        model_maze.move_player(1, 0)
        self.assertEqual((1, 0), m.get_player_position())

        model_maze.move_player(1, 1)
        self.assertEqual((1, 1), m.get_player_position())

        model_maze.move_player(1, 2)
        self.assertEqual((1, 2), m.get_player_position())

        model_maze.move_player(1, 1)
        model_maze.move_player(1, 0)
        model_maze.move_player(0, 0)

        self.assertEqual((0, 0), m.get_player_position())

    def test_two_by_two_solution_path(self):
        model_maze = MusicMaze(3, 2, 2, 1)
        m = MazeState(model_maze)

        m_str = "X - O\n" \
                "|   |\n" \
                "O   O"
        self.assertEqual(m_str, str(model_maze))

        self.assertEqual([(0, 0), (0, 1), (1, 1)], m.get_solution_path())

    def test_three_by_three_solution_path(self):
        model_maze = MusicMaze(5, 3, 3, 1)
        m = MazeState(model_maze)

        m_str = "X - O   O\n" \
                "|       |\n" \
                "O - O - O\n" \
                "    |   |\n" \
                "O - O   O"
        self.assertEqual(m_str, str(model_maze))

        self.assertEqual([(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)],
                         m.get_solution_path())

    def test_three_by_five_solution_path(self):
        model_maze = MusicMaze(7, 5, 3, 1)
        m = MazeState(model_maze)

        m_str = "O - O   O - O - O\n" \
                "|       |       |\n" \
                "O - O   O - X   O\n" \
                "    |   |       |\n" \
                "O - O - O - O   O"
        self.assertEqual(m_str, str(model_maze))

        self.assertEqual([(1, 3), (1, 2), (0, 2), (0, 3),
                          (0, 4), (1, 4), (2, 4)],
                         m.get_solution_path())

    def test_five_by_three_solution_path(self):
        model_maze = MusicMaze(7, 3, 5, 1)
        m = MazeState(model_maze)

        m_str = "O - O   O\n" \
                "|       |\n" \
                "O - O - O\n" \
                "|        \n" \
                "O - O   O\n" \
                "|   |   |\n" \
                "O   X   O\n" \
                "|       |\n" \
                "O - O - O"
        self.assertEqual(m_str, str(model_maze))

        self.assertEqual([(3, 1), (2, 1), (2, 0), (3, 0),
                          (4, 0), (4, 1), (4, 2)],
                         m.get_solution_path())

    def test_three_by_three_game_over(self):
        model_maze = MusicMaze(5, 3, 3, 1)

        m_str = "X - O   O\n" \
                "|       |\n" \
                "O - O - O\n" \
                "    |   |\n" \
                "O - O   O"
        self.assertEqual(m_str, str(model_maze))

        m = MazeState(model_maze)

        self.assertFalse(m.game_over())
        model_maze.move_player(1, 0)
        self.assertFalse(m.game_over())
        model_maze.move_player(1, 1)
        self.assertFalse(m.game_over())
        model_maze.move_player(1, 2)
        self.assertFalse(m.game_over())
        model_maze.move_player(2, 2)
        self.assertTrue(m.game_over())

    def test_two_by_two_closest_cell(self):
        model_maze = MusicMaze(3, 2, 2, 1)

        m_str = "X - O\n" \
                "|   |\n" \
                "O   O"
        self.assertEqual(m_str, str(model_maze))
        m = MazeState(model_maze)

        self.assertEqual((0, 0), m.get_closest_cell_for_player())
        model_maze.move_player(1, 0)
        self.assertEqual((0, 0), m.get_closest_cell_for_player())

        model_maze.move_player(0, 0)
        model_maze.move_player(0, 1)
        self.assertEqual((0, 1), m.get_closest_cell_for_player())

        model_maze.move_player(1, 1)
        self.assertEqual((1, 1), m.get_closest_cell_for_player())

    def test_three_by_three_closest_cell_and_distance(self):

        model_maze = MusicMaze(5, 3, 3, 1)

        m_str = "X - O   O\n" \
                "|       |\n" \
                "O - O - O\n" \
                "    |   |\n" \
                "O - O   O"
        self.assertEqual(m_str, str(model_maze))
        m = MazeState(model_maze)

        self.assertEqual((0, 0), m.get_closest_cell_for_player())
        self.assertEqual(0, m.get_closest_cell_distance_for_player())

        model_maze.move_player(0, 1)
        self.assertEqual((0, 0), m.get_closest_cell_for_player())
        self.assertEqual(1, m.get_closest_cell_distance_for_player())
        model_maze.move_player(0, 0)

        model_maze.move_player(1, 0)
        self.assertEqual((1, 0), m.get_closest_cell_for_player())
        self.assertEqual(0, m.get_closest_cell_distance_for_player())

        model_maze.move_player(1, 1)
        self.assertEqual((1, 1), m.get_closest_cell_for_player())
        self.assertEqual(0, m.get_closest_cell_distance_for_player())

        model_maze.move_player(2, 1)
        self.assertEqual((1, 1), m.get_closest_cell_for_player())
        self.assertEqual(1, m.get_closest_cell_distance_for_player())

        model_maze.move_player(2, 0)
        self.assertEqual((1, 1), m.get_closest_cell_for_player())
        self.assertEqual(2, m.get_closest_cell_distance_for_player())

        model_maze.move_player(2, 1)
        model_maze.move_player(1, 1)
        model_maze.move_player(1, 2)
        self.assertEqual((1, 2), m.get_closest_cell_for_player())
        self.assertEqual(0, m.get_closest_cell_distance_for_player())

        model_maze.move_player(0, 2)
        self.assertEqual((1, 2), m.get_closest_cell_for_player())
        self.assertEqual(1, m.get_closest_cell_distance_for_player())

        model_maze.move_player(1, 2)
        model_maze.move_player(2, 2)
        self.assertEqual((2, 2), m.get_closest_cell_for_player())
        self.assertEqual(0, m.get_closest_cell_distance_for_player())

    def test_three_by_five_closest_distance_and_cell(self):
        model_maze = MusicMaze(7, 5, 3, 1)
        m = MazeState(model_maze)

        m_str = "O - O   O - O - O\n" \
                "|       |       |\n" \
                "O - O   O - X   O\n" \
                "    |   |       |\n" \
                "O - O - O - O   O"
        self.assertEqual(m_str, str(model_maze))

        self.assertEqual((1, 3), m.get_closest_cell_for_player())
        self.assertEqual(0, m.get_closest_cell_distance_for_player())

        model_maze.move_player(1, 2)
        self.assertEqual((1, 2), m.get_closest_cell_for_player())
        self.assertEqual(0, m.get_closest_cell_distance_for_player())

        model_maze.move_player(2, 2)
        self.assertEqual((1, 2), m.get_closest_cell_for_player())
        self.assertEqual(1, m.get_closest_cell_distance_for_player())

        model_maze.move_player(2, 3)
        self.assertEqual((1, 2), m.get_closest_cell_for_player())
        self.assertEqual(2, m.get_closest_cell_distance_for_player())

        model_maze.move_player(2, 2)
        model_maze.move_player(2, 1)
        self.assertEqual((1, 2), m.get_closest_cell_for_player())
        self.assertEqual(2, m.get_closest_cell_distance_for_player())

        model_maze.move_player(2, 0)
        self.assertEqual((1, 2), m.get_closest_cell_for_player())
        self.assertEqual(3, m.get_closest_cell_distance_for_player())

        model_maze.move_player(2, 1)
        model_maze.move_player(1, 1)
        self.assertEqual((1, 2), m.get_closest_cell_for_player())
        self.assertEqual(3, m.get_closest_cell_distance_for_player())

        model_maze.move_player(1, 0)
        self.assertEqual((1, 2), m.get_closest_cell_for_player())
        self.assertEqual(4, m.get_closest_cell_distance_for_player())

        model_maze.move_player(0, 0)
        self.assertEqual((1, 2), m.get_closest_cell_for_player())
        self.assertEqual(5, m.get_closest_cell_distance_for_player())

        model_maze.move_player(0, 1)
        self.assertEqual((1, 2), m.get_closest_cell_for_player())
        self.assertEqual(6, m.get_closest_cell_distance_for_player())

    def test_five_by_three_closest_distance_and_cell(self):
        model_maze = MusicMaze(7, 3, 5, 1)
        m = MazeState(model_maze)

        m_str = "O - O   O\n" \
                "|       |\n" \
                "O - O - O\n" \
                "|        \n" \
                "O - O   O\n" \
                "|   |   |\n" \
                "O   X   O\n" \
                "|       |\n" \
                "O - O - O"
        self.assertEqual(m_str, str(model_maze))

        self.assertEqual((3, 1), m.get_closest_cell_for_player())
        self.assertEqual(0, m.get_closest_cell_distance_for_player())

        model_maze.move_player(2, 1)
        self.assertEqual((2, 1), m.get_closest_cell_for_player())
        self.assertEqual(0, m.get_closest_cell_distance_for_player())

        model_maze.move_player(2, 0)
        self.assertEqual((2, 0), m.get_closest_cell_for_player())
        self.assertEqual(0, m.get_closest_cell_distance_for_player())

        model_maze.move_player(1, 0)
        self.assertEqual((2, 0), m.get_closest_cell_for_player())
        self.assertEqual(1, m.get_closest_cell_distance_for_player())

        model_maze.move_player(0, 0)
        self.assertEqual((2, 0), m.get_closest_cell_for_player())
        self.assertEqual(2, m.get_closest_cell_distance_for_player())

        model_maze.move_player(0, 1)
        self.assertEqual((2, 0), m.get_closest_cell_for_player())
        self.assertEqual(3, m.get_closest_cell_distance_for_player())

        model_maze.move_player(0, 0)
        model_maze.move_player(1, 0)

        model_maze.move_player(1, 1)
        self.assertEqual((2, 0), m.get_closest_cell_for_player())
        self.assertEqual(2, m.get_closest_cell_distance_for_player())

        model_maze.move_player(1, 2)
        self.assertEqual((2, 0), m.get_closest_cell_for_player())
        self.assertEqual(3, m.get_closest_cell_distance_for_player())

        model_maze.move_player(0, 2)
        self.assertEqual((2, 0), m.get_closest_cell_for_player())
        self.assertEqual(4, m.get_closest_cell_distance_for_player())

    def test_get_neighbors_two_by_two(self):
        model_maze = MusicMaze(3, 2, 2, 1)

        m_str = "X - O\n" \
                "|   |\n" \
                "O   O"
        self.assertEqual(m_str, str(model_maze))

        m = MazeState(model_maze)

        self.assertCountEqual([(1, 0), (0, 1)],
                              m.get_connected_neighbors(0, 0))

        self.assertCountEqual([(0, 0)], m.get_connected_neighbors(1, 0))
        self.assertCountEqual([(0, 0), (1, 1)],
                              m.get_connected_neighbors(0, 1))
        self.assertCountEqual([(0, 1)], m.get_connected_neighbors(1, 1))

    def test_get_neighbors_three_by_five(self):
        model_maze = MusicMaze(7, 5, 3, 1)

        m_str = "O - O   O - O - O\n" \
                "|       |       |\n" \
                "O - O   O - X   O\n" \
                "    |   |       |\n" \
                "O - O - O - O   O"
        self.assertEqual(m_str, str(model_maze))

        m = MazeState(model_maze)

        self.assertCountEqual([(0, 1), (1, 0)],
                              m.get_connected_neighbors(0, 0))
        self.assertCountEqual([(2, 1)], m.get_connected_neighbors(2, 0))
        self.assertCountEqual([(2, 0), (1, 1), (2, 2)],
                              m.get_connected_neighbors(2, 1))
        self.assertCountEqual([(0, 2), (1, 3), (2, 2)],
                              m.get_connected_neighbors(1, 2))
        self.assertCountEqual([(0, 3), (1, 4)],
                              m.get_connected_neighbors(0, 4))
        self.assertCountEqual([(1, 4)], m.get_connected_neighbors(2, 4))

    def test_illegal_value_for_maze_neighbors(self):
        model_maze = MusicMaze(3, 2, 2)
        m = MazeState(model_maze)

        try:
            m.get_connected_neighbors(-1, 0)
            self.fail("Should not be able to get connected components")
        except IndexError as e:
            self.assertEqual("Maze does not contain vertice", str(e))