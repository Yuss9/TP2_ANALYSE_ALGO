from readGraphFromFile import read_graph
import random


class Graph:
    def __init__(self, file):
        # Initialisation du graphe à partir d'un fichier
        self.edges = read_graph(file)
        self.vertex = {}
        self.colors = {}

        # Création des sommets et des arêtes
        self.create_vertices_and_edges()

    def create_vertices_and_edges(self):
        for edge in self.edges:
            source, target = edge
            self.add_vertex(source)
            self.add_vertex(target)
            self.add_edge(source, target)

    def random_colors(self):
        # Coloration aléatoire des sommets en rouge, bleu ou vert
        for v in self.vertex:
            self.color_vertex(v, random.choice(['Red', 'Blue', 'Green']))

    def get_vertex(self):
        # Obtenir la liste des sommets
        return self.vertex

    def get_colors(self):
        # Obtenir la coloration des sommets
        return self.colors

    def add_vertex(self, vertex):
        # Ajouter un sommet s'il n'existe pas déjà
        if vertex not in self.vertex:
            self.vertex[vertex] = []
            self.colors[vertex] = 'None'

    def add_edge(self, vertex1, vertex2):
        # Ajouter une arête entre deux sommets
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.vertex[vertex1].append(vertex2)
        self.vertex[vertex2].append(vertex1)

    def color_vertex(self, vertex, color):
        # Colorer un sommet avec une couleur donnée
        self.colors[vertex] = color

    def update_all_color(self, new_coloring):
        # Mettre à jour la coloration de tous les sommets
        for vertex, color in new_coloring.items():
            self.color_vertex(vertex, color)
