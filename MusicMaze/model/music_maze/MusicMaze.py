class MusicMaze:
    """This class represents an instance of a music maze game. The class itself
    is responsible for constructing a graph such that the graph now depicts
    the path that a user can walk through. In this maze, each of the entries
    in the maze is considered a cell, and those cells are really just vertices
    with additional information about the vertice.

    A player in the maze must walk from whatever is considered the "starting"
    cell until they reach the "end" cell. As they traverse through the maze,
    if they happen to walk along the wrong path, the player will be given a
    distance from how far off they were from the "correct" path.

    This implementation represents a 2D n * m grid maze, where n represents
    height and m represents width. We define the maze ending location, but
    not necessarily the starting location. The end of the maze will always
    be located at the bottom right of the maze, whereas the starting location
    is highly variable, but the starting location will definitely bring a player
    to the right path if followed correctly."""

    def __init__(self):
        pass

    def __construct_maze(self, length=8, extra_width=0, extra_height=0):
        """Given a length on which to construct the length of the solution to
        the maze, constructs a maze with hints towards the size of the maze.
        By the constraints of our maze, the bare minimum dimensions of this
        maze must necessarily be (width + height) >= length - 1 to find a
        path such that a path of the appropriate length can be found.

        Args:
            length(int): the length of the path.
            extra_width(int): any additional width requested from the maze
            extra_height(int): any additional height requested from the maze
        Raises:
            ValueError: if length, extra_width, or extra_height is not positive
            """
        if length <= 0 or extra_width <= 0 or extra_height <= 0:
            raise ValueError("Given negative dimension parameter")
        # build the maze of vertices
        # connect all of the vertices together
        # apply kruskal's to find something from the graph
        # sever any edges not in kruskals
        # BFS to find an appropriate starting location (since top-left is just a
        # lower bound guarentee)

    def distance_from_path(self, row, col):
        """Given a row and column of a cell, determines the distance that cell
        is from the correct path.

        Args:
            row(int): the row of the cell
            col(int): the column of the cell
        Returns:
            int: the distance that cell is away from the solution path"""
        pass

    def solution_path(self):
        """Returns the path that represents the "correct" steps needed to move
        from the start to the end of the maze.

        Returns:
            list(str): A list of edges in string format that represent the
                correct path from start to finish"""
        pass

    def move_player(self, row, col):
        """Moves the player to the expected row and column if possible.

        Args:
            row(int): the row to move to
            col(int): the column to move to
        Raises:
            ValueError: if the player cannot move to that location.
            ValueError: if the player tries to move to the same location they
                are located at"""
        pass

    def get_player_position(self):
        """Returns a tuple representing the (row, col) of the player's current
            position.

        Returns:
            tuple(int, int): the (row, col) of the player's current location"""
        pass

    def game_over(self):
        """Determines if the game is over. The game is considered "over" when
        the player reaches the "end" cell.

        Returns:
            bool: if the player has reached the end cell"""
        pass
