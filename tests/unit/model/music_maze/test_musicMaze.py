from unittest import TestCase

from model.music_maze.MusicMaze import MusicMaze


class TestMusicMaze(TestCase):
    """This class represents test cases for the music maze. Most of the tests
    take advantage of the string representation of the maze to visually
    verify if a move has been appropriately made."""

    def test_negative_length_constructor(self):
        try:
            MusicMaze(-1, 2, 3)
            self.fail("Should not be able to give negative length")
        except ValueError as e:
            self.assertEqual("Given invalid maze dimension", str(e))

    def test_zero_length_constructor(self):
        try:
            MusicMaze(-1, 2, 3)
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
