from Graph import Graph
from itertools import combinations
from verificateur import is_valid_3_coloration
import random


def is_valid_coloring(graph, coloring):
    """
    Vérifie si une coloration est valide en parcourant les arêtes du graphe.

    :param graph: Le graphe
    :param coloring: La coloration à vérifier
    :return: True si la coloration est valide, False sinon
    """
    for vertex in graph:
        for neighbor in graph[vertex]:
            if coloring[vertex] == coloring[neighbor]:
                return False
    return True


def random_coloring(graph):
    """
    Crée une coloration aléatoire pour les sommets du graphe.

    :param graph: Le graphe
    :return: Une coloration aléatoire
    """
    coloring = {}
    for vertex in graph:
        coloring[vertex] = random.choice(['Red', 'Blue', 'Green'])
    return coloring


def find_problematic_edges(graph, coloring):
    """
    Trouve les arêtes problématiques dans une coloration en parcourant le graphe.

    :param graph: Le graphe
    :param coloring: La coloration à vérifier
    :return: Une liste d'arêtes problématiques
    """
    problematic_edges = []
    for vertex in graph:
        for neighbor in graph[vertex]:
            if coloring[vertex] == coloring[neighbor]:
                problematic_edges.append((vertex, neighbor))
    return problematic_edges


def random_coloring_solver(graph, max_iterations=1000):
    """
    Résout le problème de la coloration du graphe en modifiant la coloration de manière aléatoire.

    :param graph: Le graphe
    :param max_iterations: Nombre maximum d'itérations
    :return: Une coloration valide ou None si aucune solution n'a été trouvée
    """
    current_coloring = random_coloring(graph)

    for _ in range(max_iterations):
        problematic_edges = find_problematic_edges(graph, current_coloring)

        if not problematic_edges:
            return current_coloring

        random_edge = random.choice(problematic_edges)
        random_vertex = random.choice(random_edge)
        available_colors = ['Red', 'Blue', 'Green']
        available_colors.remove(current_coloring[random_vertex])
        new_color = random.choice(available_colors)

        current_coloring[random_vertex] = new_color

    return None


if __name__ == "__main__":
    path_file = '../instances/3C_GOOD_1'
    g = Graph(path_file)
    print('Graph is :')
    print(g.get_vertex())
    print('\n-- Random coloring solver --')
    solution = random_coloring_solver(g.get_vertex())
    if solution:
        g.update_all_color(solution)
        print(is_valid_3_coloration(g))
        print(g.get_colors())
        print(g.get_vertex())
    else:
        print('pas de 3C')
