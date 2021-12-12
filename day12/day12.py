graph = {}
with open("/home/roflzyo/aoc/2021/day12/input.txt") as f:
    for line in f.readlines():
        v, w = line.strip().split("-")
        if graph.get(v):
            graph[v] += [w]
        else:
            graph[v] = [w]
        if graph.get(w):
            graph[w] += [v]
        else:
            graph[w] = [v]

mini_data = {
    "start": ["A", "b"],
    "A": ["c", "b", "end"],
    "b": ["A", "d", "end"],
    "c": ["A"],
    "d": ["b"]
}


def make_paths(graph, start, end, path, paths, twice=False):
    if start.islower() and start in path:
        path.append(1)
    if start == end:
        return path + [start]
    for node in graph[start]:
        if twice and node in path and node.islower() and 1 in path:
            pass
        elif twice and node in path and node.islower() and path.count(node) > 1:
            path.append(1)
            pass
        elif node in path and node.islower() and not twice:
            pass
        elif node == "start":
            pass
        else:
            newpath = make_paths(graph, node, end, path + [start], paths,
                                 twice)
            if newpath:
                paths.append(newpath)


paths = []
# make_paths(mini_data, "start", "end", [], paths)
make_paths(graph, "start", "end", [], paths)
print(len(paths))

paths = []
# make_paths(mini_data, "start", "end", [], paths, twice=True)
make_paths(graph, "start", "end", [], paths, twice=True)
print(len(paths))


