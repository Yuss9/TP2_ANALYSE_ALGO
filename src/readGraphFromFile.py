def read_graph(file_path):
    with open(file_path, 'r') as file:
        lignes = file.readlines()

    edges = []
    for ligne in lignes:
        if ligne.startswith('e'):
            source, cible = ligne.split()[1:]
            edges.append((int(source), int(cible)))

    return edges