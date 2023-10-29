from Graph import Graph
from itertools import combinations
from verificateur import is_valid_3_coloration
import random

from itertools import combinations


def is_independent_set(graph, node1, node2):
    # Vérifie si les nœuds node1 et node2 forment un ensemble indépendant dans le graphe.
    return node2 not in graph[node1]


def is_bipartite(graph, node_set):
    # Vérifie si le sous-graphe formé en retirant node_set est biparti.
    visited = {}
    color = {}
    for node in graph:
        visited[node] = False
        color[node] = -1

    for start_node in node_set:
        if not visited[start_node]:
            stack = [start_node]
            color[start_node] = 0

            while stack:
                current_node = stack.pop()
                visited[current_node] = True

                for neighbor in graph[current_node]:
                    if not visited[neighbor]:
                        stack.append(neighbor)
                        color[neighbor] = 1 - color[current_node]
                    elif color[neighbor] == color[current_node]:
                        return False  # Le graphe n'est pas biparti.

    return True


def lawler_solver(graph):
    nodes = list(graph.keys())
    for size in range(2, len(graph) + 1):
        for node1, node2 in combinations(nodes, size):
            if is_independent_set(graph, node1, node2):
                complement_set = set(nodes) - {node1, node2}
                if is_bipartite(graph, complement_set):
                    solution = {}
                    for node in complement_set:
                        solution[node] = 'Red'
                    solution[node1] = 'Blue'
                    solution[node2] = 'Blue'
                    return solution
    return None


if __name__ == "__main__":
    path_file = '../instances/3C_GOOD_1'
    g = Graph(path_file)
    print('Graph is :')
    print('\n-- Lawler solver --')
    solution = lawler_solver(g.get_vertex())
    print('solution :')
    print(solution)
    print('fin solution')
    if solution:
        g.update_all_color(solution)
        print(is_valid_3_coloration(g))
        print(g.get_colors())
        print(g.get_vertex())
    else:
        print('pas de 3C')
