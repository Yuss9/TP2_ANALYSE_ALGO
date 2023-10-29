# coding=utf-8

import sys
from pycosat import solve as solveSAT
from pysat.card import *
from Graph import Graph


def solveClique(g, size, verbose):
    """
    Résout le problème Clique
    :param g: graphe G
    :param size: taille de la clique recherchée
    :return: cherche s'il existe une clique de taille
    `size' dans G.
    """

    # La suite est à compléter/modifier
    # (décommentez petit à petit les lignes commençant par #)

    """
    Si c'est possible pour votre structure de données, vous pouvez afficher le graphe
    """
    # if verbose:
    #    print("Graphe d'entrée")
    #    print(g)

    """
    Mettre dans n le nombre de sommets du graphe
    """
    # n = ???
    """
    Supprimer la ligne suivante :
    elle sert juste à ce que ça compile tant que la ligne d'avant n'est pas traitée
    """
    n = len(g.get_vertex())

    """
    Nos variables seront X1,...,Xn
    On voudrait que Xi soit vraie si la clique contient le sommet (i-1)
    """

    """
    On veut que la clique soit de taille `size'.
    Donc parmi les n variables X1,...,Xn, exactement `size' doivent
    être vraies.
    Déjà n variables sont utilisées, donc les nouvelles variables
    commenceront à n+1.
    """
    cnf = CardEnc.equals([i for i in range(1, n + 1)],
                         bound=size, top_id=n, encoding=EncType.seqcounter)

    """
    Pour chaque paire de sommets (u,v), si (u,v) n'est pas une arête,
    on rajoute la contrainte qu'une des extrémités ne doit pas appartenir
    à la clique.
    """

    for u in range(1, n+1):
        for v in range(1, u):
            if v not in g.vertex[u]:
                # Implement is_edge(u, v) to check if u and v form an edge in the graph.
                cnf.append([-u, -v])
                # Add a constraint that one of the endpoints should not belong to the clique.

    if verbose:
        print("Entrée pour le SAT solveur")
        print(cnf)

    solutionSAT = solveSAT(cnf)
    if verbose:
        print("Solution pour SAT")
        print(solutionSAT)

    """
    Si le SAT-solver n'a pas trouvé de solution, il renvoit "UNSAT".
    Sinon, il renvoit une liste d'entiers [l1, l2, l3, ...]
    Si l1 = 1 alors X1 est True
    Si l1 = -1 alors X1 est False
    Les variables l(n+1), l(n+2), ... ont été créées pour la contrainte de
    cardinalité et ne nous intéressent pas.
    En conclusion, le noeud i-1 est dans la clique si i est dans solutionSAT
    """
    if solutionSAT != "UNSAT":
        solution = [i - 1 for i in solutionSAT[:n] if i > 0]
    else:
        solution = []
    return solution

#########################################################################


def solve_3_coloration(graph, is_verbose=False):
    """
    Résout le problème de la 3-Coloration pour un graphe donné.

    :param graph: Graphe d'entrée
    :param is_verbose: Afficher les détails du processus si True
    :return: Une liste de couleurs attribuées aux sommets ou une liste vide si impossible
    """
    n = len(graph.vertex)

    # Affiche le graphe d'entrée si is_verbose est True
    if is_verbose:
        print("Graphe d'entrée")
        print(graph)

    # Crée une liste de clauses pour le problème SAT
    cnf = CardEnc.equals([i for i in range(1, 3 * n + 1)],
                         bound=n, top_id=n, encoding=EncType.seqcounter)

    # Ajoute des contraintes pour chaque sommet
    for i in range(1, n + 1):
        cnf.append([-i, -(i + n)])
        cnf.append([-i, -(i + 2 * n)])
        cnf.append([-(i + n), -(i + 2 * n)])

    # Ajoute des contraintes pour chaque paire de sommets reliés par une arête
    for u in range(len(graph.vertex)):
        for v in graph.vertex[u]:
            cnf.append([-(u + 1), -(v + 1)])
            cnf.append([-((u + 1) + n), -((v + 1) + n)])
            cnf.append([-((u + 1) + 2 * n), -((v + 1) + 2 * n)])

    # Affiche l'entrée pour le solveur SAT si is_verbose est True
    if is_verbose:
        print("Entrée pour le solveur SAT")

    # Résout le problème SAT
    solution_sat = solveSAT(cnf)

    # Affiche la solution si is_verbose est True
    if is_verbose:
        print("Solution pour SAT")
        print(solution_sat)

    # Retourne une liste de couleurs attribuées aux sommets ou une liste vide si impossible
    return [] if solution_sat == "UNSAT" else translate_solution(solution_sat, n)


def translate_solution(sol, n):
    # Traduit la solution SAT en une liste de couleurs pour les sommets
    colors = [-1] * n
    for v in sol:
        if v > 0:
            colors[(v - 1) % n] = (v - 1) // n
    return colors


def is_valid_3_coloration(graph):
    # Obtenir la liste des sommets du graphe et leur coloration actuelle
    vertices = graph.get_vertex()
    colors = graph.get_colors()

    # Parcourir tous les sommets du graphe
    for vertex in vertices:
        # Obtenir la couleur du sommet en cours d'examen
        vertex_color = colors[vertex]

        # Si le sommet n'est pas encore coloré, la 3-coloration n'est pas valide
        if vertex_color == "None":
            return "3C NOT GOOD"

        # Obtenir la liste des voisins du sommet en cours
        neighbors = vertices[vertex]

        # Parcourir les voisins du sommet
        for neighbor in neighbors:
            # Obtenir la couleur du voisin
            neighbor_color = colors[neighbor]

            # Si le voisin a la même couleur que le sommet en cours, la 3-coloration n'est pas valide
            if neighbor_color == vertex_color:
                return "3C NOT GOOD"

    # Si toutes les vérifications sont passées, la 3-coloration est valide
    return "3C GOOD"


def get_independent_set(graph, size, is_verbose):
    """
    Trouve un ensemble indépendant de taille donnée dans un graphe.

    :param graph: Le graphe G
    :param size: La taille de l'ensemble indépendant recherché
    :param is_verbose: Afficher les informations de débogage si True
    :return: Un ensemble indépendant de taille donnée ou une liste vide
    """

    n = len(graph.get_vertex())

    # Création d'une liste de variables pour chaque sommet
    cnf = CardEnc.equals([i for i in range(1, n + 1)],
                         bound=size, top_id=n, encoding=EncType.seqcounter)

    # Contraintes : les sommets voisins ne peuvent pas être dans l'ensemble indépendant
    for u in range(len(graph.vertex)):
        for v in graph.vertex[u]:
            cnf.append([-(u + 1), -(v + 1)])

    if is_verbose:
        print("Entrée pour le SAT solveur")
        print(cnf)

    solution_sat = solveSAT(cnf)

    if is_verbose:
        print("Solution pour SAT")
        print(solution_sat)

    if solution_sat != "UNSAT":
        solution = [i - 1 for i in solution_sat[:n] if i > 0]
        for i in range(len(solution)):
            solution[i] += 1
    else:
        solution = []

    return solution


#########################################################################
# first main

""" if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("usage : python3 solveClique.py <filename> <size_clique> [-v]")
        exit(1)
    filename = sys.argv[1]
    try:
        size = int(sys.argv[2])
    except:
        print("Le deuxième argument <size_clique> doit être un entier.")
        exit(1)
    if len(sys.argv) > 3 and (sys.argv[3] == "-v"
                              or sys.argv[3] == "--verbose"):
        verbose = True
    else:
        verbose = False

    # Récupérer le graphe stocké dans le fichier <filename>

    g = []
    g = Graph(filename)
    #     solution = solveClique(g, size, verbose)

    solution = solve_3_coloration(g, size, verbose)
    print("Solution pour le problème Clique")
    if solution != []:
        print(solution)
    else:
        print("Pas de clique de taille " + str(size) + ".")
"""

###########################################################################
# second main

if len(sys.argv) < 2:
    print("usage : python3 solveClique.py <filename> [-v]")
    exit(1)
filename = sys.argv[1]
if len(sys.argv) > 2 and sys.argv[2] in ["-v", "--verbose"]:
    verbose = True
else:
    verbose = False


# Récupérer le graphe stocké dans le fichier <filename>

g = Graph(filename)
solution = solve_3_coloration(g, verbose)

print("Solution pour le problème 3-Coloration :")
if solution:
    color = translate_solution(solution, len(g.vertex))
    print(g.vertex)
    print(color)
    print("UPDATING COLOR ......")
    g.assign_all_color_to_vertex(color)
    print("######################################################")
    print(g.get_colors())
    print("######################################################")
    print(is_valid_3_coloration(g))
else:
    print("Pas de coloration.")
