from Graph import Graph
from itertools import combinations
from verificateur import is_valid_3_coloration


def is_safe(graph, vertex, color, solution):
    # Vérifie si la coloration d'un sommet est valide en examinant ses voisins
    for neighbor in graph[vertex]:
        if neighbor in solution and solution[neighbor] == color:
            return False
    return True


def solve_coloration(graph, vertex, solution):
    # Fonction récursive pour résoudre la coloration du graphe
    if vertex is None:
        return True  # Tous les sommets ont été coloriés

    for color in ['Red', 'Blue', 'Green']:
        if is_safe(graph, vertex, color, solution):
            solution[vertex] = color

            # Récursivement, essayer de colorier les sommets suivants
            if solve_coloration(graph, next_vertex_to_color(graph, solution), solution):
                return True

            # Si la coloration actuelle ne mène pas à une solution, backtrack
            solution[vertex] = 'None'
    return False


def next_vertex_to_color(graph, solution):
    # Trouve le prochain sommet à colorier
    for vertex in graph:
        if solution[vertex] == 'None':
            return vertex
    return None


def backtracking_solver(graph):
    # Initialise la solution avec 'None' pour chaque sommet
    solution = {vertex: 'None' for vertex in graph}

    # Lance le solveur de coloration
    if solve_coloration(graph, next_vertex_to_color(graph, solution), solution):
        return solution
    return None


if __name__ == "__main__":
    path_file = '../instances/3C_GOOD_1'
    g = Graph(path_file)
    print('Graph is :')
    print(g.get_vertex())
    print('\n-- Backtracking solver --')
    solution = backtracking_solver(g.get_vertex())
    if solution:
        g.update_all_color(solution)
        print(is_valid_3_coloration(g))
        print(g.get_colors())
        print(g.get_vertex())
    else:
        print('pas de 3C')
