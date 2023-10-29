from readGraphFromFile import read_graph
import random


class Graph:
    def __init__(self, file):
        # Initialisation du graphe à partir d'un fichier
        if file:
            self.edges = read_graph(file)
        else:
            self.edges = []

        self.vertex = {}
        self.colors = {}

        # Création des sommets et des arêtes
        self.create_vertices_and_edges()

        for v in self.vertex:
            self.colors[v] = 'None'

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

    def add_edge_complement(self, vertex1, vertex2):
        self.vertex[vertex1].append(vertex2)

    def color_vertex(self, vertex, color):
        # Colorer un sommet avec une couleur donnée
        self.colors[vertex] = color

    def update_all_color(self, new_coloring):
        # Mettre à jour la coloration de tous les sommets
        for vertex, color in new_coloring.items():
            self.color_vertex(vertex, color)

    def assign_all_color_to_vertex(self, new_coloring):
        if len(new_coloring) != len(self.get_vertex()):
            raise ValueError("Les tableaux n'ont pas la même taille")

        for i, color in enumerate(new_coloring):
            self.color_vertex(i, color)

    def invert_graph(self):
        inverted_edges = set()

        # Parcours de toutes les arêtes existantes
        for edge in self.edges:
            source, target = edge

            # Si l'arête existe, la supprimer
            if (source, target) in inverted_edges or (target, source) in inverted_edges:
                inverted_edges.discard((source, target))
                inverted_edges.discard((target, source))
            else:
                # Sinon, ajouter l'arête inversée
                inverted_edges.add((target, source))

        # Mettre à jour les arêtes du graphe
        self.edges = list(inverted_edges)

        # Mettre à jour les sommets voisins
        self.vertex = {}
        for edge in self.edges:
            source, target = edge
            if source not in self.vertex:
                self.vertex[source] = []
            if target not in self.vertex:
                self.vertex[target] = []
            self.vertex[source].append(target)
            self.vertex[target].append(source)

    def complement_graph(self):
        # Créez un nouveau graphe pour le complémentaire
        # Vous pouvez initialiser avec None car le fichier n'est pas nécessaire
        complement = Graph(None)

        # Ajoutez tous les sommets au graphe complémentaire
        for vertex in self.get_vertex():
            complement.add_vertex(vertex)

        # Parcourez tous les paires de sommets
        for vertex1 in self.get_vertex():
            for vertex2 in self.get_vertex():
                if vertex1 != vertex2:
                    # Vérifiez si une arête relie ces sommets dans le graphe d'origine
                    if vertex2 not in self.get_vertex()[vertex1]:
                        # Si l'arête n'existe pas, ajoutez-la au graphe complémentaire
                        complement.add_edge_complement(vertex1, vertex2)

        return complement
