from model.music_maze.MusicMaze import MusicMaze


class MazeState:
    """This class acts as the package of information that is sent to the view.
    In essence, the class functions as a view model wrapper around the
    Music Maze and provides an interface for the view to more easily
    receive information and parse the information for viewing."""

    def __init__(self, music_maze):
        """Constructs a music maze to be used to parse for this maze state.

        Args:
            music_maze(MusicMaze): a maze to diagnose statistics from"""
        self.__music_maze = music_maze

    def get_cells(self):
        """Returns a list of the cells in this maze. In this particular
        implementation, cells are interpreted as a pair of numbers and not as
        a name, which is different from the interpretation that the original
        model implements it as.

        Returns:
            list(tuple(int, int)): a list of (row, col) tuples denoting
                where a cell is located at within the maze."""
        result = []
        for cell in self.__music_maze.get_cells():
            # cells initially have names like (row, col)
            row, col = self.__cell_split(cell)
            result.append((row, col))
        return result

    def get_player_position(self):
        """Returns the player position as a (row, col) tuple.

        Returns:
            tuple(int, int): a (row, col) tuple indicating the row and column
                where the player is located at."""
        return self.__music_maze.get_player_position()

    def get_solution_path(self):
        """Returns the path of the solution, where each of the cells are
        interpreted as (row, col) pairs.

        Returns:
            list(tuple(int, int)): the solution path"""
        cells_str = self.__music_maze.solution_path()
        result = []

        for cell in cells_str:
            row, col = self.__cell_split(cell)
            result.append((row, col))
        return result

    def get_closest_cell_for_player(self):
        """Returns the cell closest to the player on the solution path.

        Returns:
            tuple(int, int): the cell closest to the player. If the player
                is on the solution path, just return that cell."""

        player_row, player_col = self.get_player_position()

        closest_cell_str = self.__music_maze.closest_cell_from_path(player_row,
                                                                    player_col)
        cell_row, cell_col = self.__cell_split(closest_cell_str)
        return cell_row, cell_col

    def get_closest_cell_distance_for_player(self):
        """Returns the distance of the cell closest to the player on the
        solution path.

        Returns:
            int: the distance of the cell closest to the player. If the player
                is on the solution path, just return that cell."""
        player_row, player_col = self.get_player_position()
        return self.__music_maze.distance_from_path(player_row, player_col)

    def game_over(self):
        """Returns whether or not the game has been completed.

        Returns:
            bool: whether or not the game has been completed"""
        return self.__music_maze.game_over()

    @staticmethod
    def __cell_split(cell):
        """Splits a cell apart from its string form and returns it as a
        row, col pair.

        Args:
            cell(str): the cell in a (row, col) format
        Returns:
            tuple(int, int): the cell in a (row, col) tuple"""
        cell = cell[1:-1].split(",")
        row = int(cell[0])
        col = int(cell[1])
        return row, col
