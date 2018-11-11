"""This file represents an implementation of Kruskal's Algorithm, which
is an algorithm used to find the minimum spanning tree of a given graph
and it's provided edges. The minimum spanning tree returned from the graph
will then be considered as the "solution" path that a user can follow."""
from model.graph.PriorityQueue import PriorityQueue


def kruskal(graph):
    """Takes the edges from a graph and produces the set of edges such that
    the edges form a minimum spanning tree for the graph.

    Args:
        graph(Graph): the graph object used to find edges from
    Returns:
        list(Edge): a list of edges from the graph forming the MST
    """
    def union(tree_one, tree_two):
        """Union the two trees if they are from separate trees. We make the
        arbitrary decision to merge the second to the first."""
        union_find[find(tree_two)] = find(tree_one)

    def find(vertice_name):
        """Finds the root of this vertice's tree."""
        if union_find[vertice_name] == vertice_name:
            return vertice_name
        return find(union_find[vertice_name])

    results = []
    pq = PriorityQueue()

    union_find = {}
    for vertice in graph.vertices():
            union_find[vertice.name()] = vertice.name()

    for edge in graph.edges():
        pq.push(edge)

    while not pq.is_empty():
        min_edge = pq.extract_min()

        vertice_one = min_edge.from_vertice().name()
        vertice_two = min_edge.to_vertice().name()

        if find(vertice_one) != find(vertice_two):
            union(vertice_one, vertice_two)
            results.append(min_edge)

    return results
