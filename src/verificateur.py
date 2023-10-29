from Graph import Graph
from itertools import combinations

import random


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


if __name__ == "__main__":
    path_file = '../instances/coloredTestGraph'

    # Créez un objet de la classe Graph en utilisant le fichier spécifié
    g = Graph(path_file)

    print('Graph is :')
    print(g.get_vertex())

    # Coloration manuelle de certains sommets
    g.color_vertex(0, 'Red')
    g.color_vertex(1, 'Blue')
    g.color_vertex(2, 'Green')

    print(g.get_colors())

    print('\n-- VERIFICATION --')
    # Vérification de la 3-coloration
    result = is_valid_3_coloration(g)
    print(result)
