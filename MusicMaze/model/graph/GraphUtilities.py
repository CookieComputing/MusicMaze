"""This file represents various useful operations that can be applied on a
graph and is separated from the graph object itself in the interest of
separation of concerns."""


def nodes_at_level(graph, root, depth):
    """Returns the name of all vertices that are at the specified level.
    If no such nodes exist, return an empty list.

    Args:
        graph(Graph): the graph to extract nodes from
        root(str): the name of the root node to start from
        depth(int): the depth away from the root node
    Returns:
        list(str): a list of the names of all vertices reachable at depth
    Raises:
        ValueError: if the depth is negative
        ValueError: if root does not exist in the graph"""
    if not graph.contains_vertice(root):
        raise ValueError("Root not found in graph")

    if depth < 0:
        raise ValueError("Given invalid depth")

    result = []

    work_list = [(root, 0)]
    discovered = set()
    while work_list:
        current_vertice, current_level = work_list.pop(0)

        if current_vertice in discovered:
            continue

        discovered.add(current_vertice)
        if current_level < depth:
            for neighbor in graph.neighbors(current_vertice):
                work_list.append((neighbor, current_level + 1))
        elif current_level == depth:
            result.append(current_vertice)
            # neighbors at this point are discarded if level >= depth
    return result


def shortest_path(graph, from_vertice, to_vertice):
    """Given two vertices, find a path from the from_vertice leading up to
    the to_vertice that is the shortest possible. If no such path exists,
    return an empty list.

    Args:
        graph(Graph): the graph to look for a path in
        from_vertice(str): the source vertice
        to_vertice(str): the destination vertice
    Returns:
        list(str): the list containing the path of the vertice
    Raises:
        ValueError: If either from or to vertices are not in the graph"""
    if not (graph.contains_vertice(from_vertice)
            and graph.contains_vertice(to_vertice)):
        raise ValueError("Vertice not found in graph")

    parent = {}

    def visit_nodes():
        work_list = [from_vertice]
        visited = set()

        while work_list:
            current_vertice = work_list.pop(0)

            if current_vertice == to_vertice:
                break
            visited.add(current_vertice)

            for neighbor in graph.neighbors(current_vertice):
                if neighbor not in visited:
                    work_list.append(neighbor)
                    parent[neighbor] = current_vertice

    def backtrack():
        result = []

        current_vertice = to_vertice
        while current_vertice in parent:
            result.append(current_vertice)
            current_vertice = parent[current_vertice]
        if result:
            result.append(from_vertice)
        return result

    visit_nodes()
    return list(reversed(backtrack()))
