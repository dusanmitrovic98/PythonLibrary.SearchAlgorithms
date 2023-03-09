import queue


def breadth_first_search(graph, start, end):
    if start is end:
        path = list()
        path.append(start)
        return path
    queue_nodes = queue.Queue(len(graph))
    visited = set()
    prev_nodes = dict()
    prev_nodes[start] = None
    visited.add(start)
    queue_nodes.put(start)
    found_dest = False
    while (not found_dest) and (not queue_nodes.empty()):
        node = queue_nodes.get()
        # process(node)
        for dest in graph[node]:
            if dest not in visited:
                prev_nodes[dest] = node
                if dest is end:
                    found_dest = True
                    break
                visited.add(dest)
                queue_nodes.put(dest)
    path = list()
    if found_dest:
        path.append(end)
        prev = prev_nodes[end]
        while prev is not None:
            path.append(prev)
            prev = prev_nodes[prev]
        path.reverse()
    return path
