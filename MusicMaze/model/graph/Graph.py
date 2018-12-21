from model.graph.Edge import Edge
from model.graph.Vertice import Vertice


class Graph:
    """This class represents an implementation of a graph. The graph is a
    set of vertices and edges, and is interpreted using an adjacency list
    for the ease of connecting vertices with their neighbors. The graph itself
    is not a maze, but rather an interpretation of a connected tree of nodes.
    The class is an undirected simple graph, and as such will have unique
    edges that are bidirectional.

    This Graph class should be the main point of contact between the graph
    and any operations involving the vertices and edges of this graph,
    operating as the primary interface of the graph and its associated classes.
  """

    def __init__(self):
        """Initializes the graph as an initially empty graph. All vertices
        and edges must subsequently be added to the graph.
        """
        self.__vertices = dict()

        # Edges are represented in the form
        #  "{a} - {b}".format(a.name(), b.name))
        self.__edges = dict()
        self.__edge_key = "{0} - {1}"

    def add_vertice(self, vertice_name):
        """Adds a given vertice into the graph. The vertice must be a new
        object and should also have a unique name identifying the vertice.

        Args:
            vertice_name(str): the name of the new vertice to add
        Raises:
            ValueError: if another vertice exists in the graph with the same
                name as the given vertice"""
        if self.contains_vertice(vertice_name):
            raise ValueError("Vertice already in the graph")
        self.__vertices[vertice_name] = Vertice(vertice_name)

    def contains_vertice(self, vertice_name):
        """Determines if a specific vertice exists in the graph. The vertice
        should be a physical object in the graph if it is contained.

        Args:
            vertice_name(str): the given vertice to check
        Returns:
            boolean: Whether or not the vertice in question is in the graph"""
        return vertice_name in self.__vertices

    def add_edge(self, v1, v2, weight=0):
        """Adds an edge to this graph only if that edge does not already
        exist. In our interpretation of the program, this means an undirected
        edge. Furthermore, only edges containing vertices that actually
        exist in the graph are acceptable.

        Note that since this is an undirected graph, adding an edge with
        either vertice as v1 or v2 will be the same edge. Adding an edge is
        also idempotent, and will also connect the vertices.

        Args:
            v1(str): The name of one of the vertices in the edge
            v2(str): The name of the other vertice in the edge.
            weight(int): the weight of the graph, which is non-negative
        Raises:
            ValueError: if the edge in question contains vertices that do
                not exist in the graph
            ValueError: if the weight is negative"""
        if v1 not in self.__vertices or v2 not in self.__vertices:
            raise ValueError("Vertice contained in edge not in graph")
        vertice_one = self.__vertices[v1]
        vertice_two = self.__vertices[v2]
        edge = Edge(vertice_one, vertice_two, weight)
        edge.connect_vertices()
        self.__edges[self.__edge_key.format(v1, v2)] = edge

    def remove_edge(self, v1, v2):
        """Removes the given edge from the graph. Removing the edge will
        cause the graph to disconnect the vertices from each other.

        Removing an edge is idempotent, and will not raise exceptions if no
        such edge exists

        Args:
            v1(str): the name of the first vertice in the edge
            v2(str): the name of the second vertice in the edge"""
        if self.__edge_key.format(v1, v2) in self.__edges:
            formatted_edge_key = self.__edge_key.format(v1, v2)
            edge = self.__edges[formatted_edge_key]
            edge.disconnect_vertices()
            del self.__edges[formatted_edge_key]
        if self.__edge_key.format(v2, v1) in self.__edges:
            formatted_edge_key = self.__edge_key.format(v2, v1)
            edge = self.__edges[formatted_edge_key]
            edge.disconnect_vertices()
            del self.__edges[formatted_edge_key]

    def contains_edge(self, v1, v2):
        """Determines whether or not this graph contains a given edge. An edge
        is considered in the graph if the graph contains some edge such that
        the vertices of that edge match the vertices of the given edge.

        Args:
            v1(str): the name of one of the vertices in the edge
            v2(str): the name of the other vertice in the edge
        Returns:
            boolean: Whether or not the edge is in the graph."""
        return self.__edge_key.format(v1, v2) in self.__edges or \
            self.__edge_key.format(v2, v1) in self.__edges

    def vertices(self):
        """Returns the set of vertices contained in this graph.

        Returns:
            set(Vertice): A set of copies of vertices in this graph
        """
        return set(self.__vertices.values())

    def edges(self):
        """Returns the set of edges contained in this graph.

        Returns:
            set(Edge): A set of copies of edges in this graph
        """
        return set(self.__edges.values())

    def neighbors(self, vertice):
        """Returns a list of the names of the neighbors of the given vertice
         in the graph.

        Args:
            vertice(str): the name of the vertice
        Returns:
            list(str): a list of the name of the neighbors
        Raises:
            ValueError: If the vertice does not exist in the graph
            """
        if not self.contains_vertice(vertice):
            raise ValueError("Vertice not in graph")

        node = self.__vertices[vertice]
        return [neighbor_vertice.name()
                for neighbor_vertice in node.neighbors()]
