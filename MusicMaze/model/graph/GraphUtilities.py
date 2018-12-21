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
