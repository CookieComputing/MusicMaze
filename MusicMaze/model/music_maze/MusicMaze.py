import itertools
import random

from model.graph.Graph import Graph
from model.graph.GraphUtilities import nodes_at_level, shortest_path
from model.graph.kruskal import kruskal

cell_format = "({0}, {1})"


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

    def __init__(self, length, width, height, seed=0):
        """Initializes the maze with the following dimensions, as well as the
        bare minimum length of the maze. The provided widths and heights are
        expected to satisfy the equation (width + height) - 1 >= length to
        satisfy the requirements of the length

        Args:
            length(int): the length of the solution for the maze
            width(int): the hinted width of the maze
            height(int): the hinted height of the maze
            seed(int): a seed to generate a new maze. Should be left untouched
                for ordinary purposes.
        Raises:
            ValueError: If the length, width, or height <= 0"""
        if length <= 0 or width <= 0 or height <= 0:
            raise ValueError("Given invalid maze dimension")

        if not width + height - 1 >= length:
            raise ValueError("Given width and height cannot"
                             " guarantee path length")

        if seed:
            random.seed(seed)

        self.__height = height
        self.__width = width

        # initialized in construct_maze()
        self.__starting_pos = None
        self.__end_pos = (height - 1, width - 1)
        self.__graph = self.__construct_maze(width, height, length)
        self.__player_pos = self.__starting_pos

        self.__solution_path = []
        # the maze position is interpreted as (row, col)

    def __construct_maze(self, width, height, length):
        """Given a length on which to construct the length of the solution to
        the maze, constructs a maze with hints towards the size of the maze.
        By the constraints of our maze, the bare minimum dimensions of this
        maze must necessarily be (width + height) >= length - 1 to find a
        path such that a path of the appropriate length can be found.

        Args:
            width(int): the width of the maze.
            height(int): the height of the maze.
            length(int): the length of the maze.
        Returns:
            Graph: a resulting graph
            """
        weight_lower_bound = 0
        weight_upper_bound = 10000

        graph = Graph()

        def add_vertices():
            for row in range(height):
                for col in range(width):
                    graph.add_vertice(cell_format.format(row, col))

        def add_edges():
            # the edges are added in sequence of each row connected first,
            # then all rows are joined.

            # e. g. o - o - o

            # then o o o
            #      | | |
            #      o o o
            for row in range(height):
                for col in range(width-1):
                    graph.add_edge(cell_format.format(row, col),
                                   cell_format.format(row, col+1),
                                   random.randint(weight_lower_bound,
                                                  weight_upper_bound))

            for row in range(height - 1):
                for col in range(width):
                    graph.add_edge(cell_format.format(row, col),
                                   cell_format.format(row+1, col),
                                   random.randint(weight_lower_bound,
                                                  weight_upper_bound))

        def remove_non_mst_edges():
            kruskal_edges = set(kruskal(graph))
            for edge in graph.edges():
                if edge not in kruskal_edges:
                    graph.remove_edge(edge.from_vertice().name(),
                                      edge.to_vertice().name())

        def set_starting_position():
            # arbitrarily picks the first starting point
            # length - 1 because 0 denotes the starting position
            potential_starting_points = nodes_at_level(graph,
                                                       cell_format.format(
                                                           self.__end_pos[0],
                                                           self.__end_pos[1]),
                                                       length-1)

            # always works given that the width/height invariant is satisfied
            initial_starting_point_str = potential_starting_points[0]

            # Since the string is of the form (x, y)
            self.__starting_pos = tuple([int(x) for x in
                                         initial_starting_point_str[1:-1]
                                        .split(',')])

        add_vertices()
        add_edges()
        remove_non_mst_edges()
        set_starting_position()
        return graph

    def distance_from_path(self, row, col):
        """Given a row and column of a cell, determines the distance that cell
        is from the correct path.

        Args:
            row(int): the row of the cell
            col(int): the column of the cell
        Returns:
            int: the distance that cell is away from the solution path, -1 if
                somehow not found
        Raises:
            IndexError: if the (row, col) pos is not in the graph"""

        original_cell = cell_format.format(row, col)
        if not self.__graph.contains_vertice(original_cell):
            raise ValueError("Given invalid position")

        solution_mapping = set(self.solution_path())
        visited = set()

        work_list = [cell_format.format(row, col)]
        while work_list:
            current_vertice = work_list.pop(0)

            visited.add(current_vertice)
            if current_vertice in solution_mapping:
                distance_from_path = len(shortest_path(self.__graph,
                                         original_cell,
                                         current_vertice))
                if distance_from_path:
                    # removes the from node to prevent over counting
                    return distance_from_path - 1
                else:
                    return 0

            for neighbor in self.__graph.neighbors(current_vertice):
                if neighbor not in visited:
                    work_list.append(neighbor)

        return -1

    def solution_path(self):
        """Returns the path that represents the "correct" steps needed to move
        from the start to the end of the maze.

        Returns:
            list(str): A list of edges in string format that represent the
                correct path from start to finish"""
        return shortest_path(self.__graph,
                             str(self.__starting_pos),
                             str(self.__end_pos))

    def move_player(self, row, col):
        """Moves the player to the expected row and column if possible.

        Args:
            row(int): the row to move to
            col(int): the column to move to
        Raises:
            ValueError: if the player cannot move to that location.
            ValueError: if the player tries to move to the same location they
                are located at"""
        if not self.__graph.contains_edge(
                cell_format.format(
                    self.__player_pos[0],
                    self.__player_pos[1]),
                cell_format.format(row, col)):
            raise ValueError("Cannot move to given location")
        self.__player_pos = (row, col)

    def get_player_position(self):
        """Returns a tuple representing the (row, col) of the player's current
            position.

        Returns:
            tuple(int, int): the (row, col) of the player's current location"""
        return self.__player_pos

    def game_over(self):
        """Determines if the game is over. The game is considered "over" when
        the player reaches the "end" cell.

        Returns:
            bool: if the player has reached the end cell"""
        return self.__player_pos == self.__end_pos

    def __str__(self):
        """Represents a string representation of the maze. In this context,
        the maze looks like a series of Os representing the walls, spaces
        representing the lanes in between, and X denoting the player location.

        Returns:
            str: A string representation of the maze."""
        row_connections = []
        column_connections = []

        for row in range(self.__height):
            row_entry = []
            for col in range(self.__width):
                if str(self.__player_pos) == cell_format.format(row, col):
                    row_entry.append("X")
                else:
                    row_entry.append("O")

                # works for the edge case of the last node b/c
                # edges not in the graph return false
                if self.__graph.contains_edge(cell_format.format(row, col),
                                              cell_format.format(row, col+1)):
                    row_entry.append(" - ")
                elif col != self.__width - 1:
                    row_entry.append("   ")
            row_connections.append(''.join(row_entry))

        for row in range(self.__height - 1):
            col_entry = []
            for col in range(self.__width):
                if self.__graph.contains_edge(cell_format.format(row, col),
                                              cell_format.format(row + 1, col)):
                    col_entry.append("|")
                else:
                    col_entry.append(" ")
            column_connections.append("   ".join(col_entry))

        return '\n'.join([entry for entry in
                          itertools.chain(
                              *itertools.zip_longest(
                                  row_connections,
                                  column_connections))
                          if entry is not None])
