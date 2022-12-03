from os import path
from networkx import Graph
fileName = '12_advent.txt'
G = Graph()

def readFile():
    global G

    lines = open(fileName, 'r')
    for line in lines:
        line = line.strip()
        G.add_edge(*line.split("-"))

    for n in G:
        G.nodes[n]["visited"] = 0

def dfs(G, node, can_twice):
    if node == "end":
        return 1

    G.nodes[node]["visited"] += 1
    total = 0

    for n in G.adj[node]:
        if n.isupper() or G.nodes[n]["visited"] == 0:
            total += dfs(G, n, can_twice)
        elif can_twice and n != "start" and G.nodes[n]["visited"] == 1:
            total += dfs(G, n, False)

    G.nodes[node]["visited"] -= 1
    return total


if __name__ == '__main__':
    readFile()
    print("Part 1:", dfs(G, "start", False))
    print("Part 2:", dfs(G, "start", True))
