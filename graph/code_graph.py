import networkx as nx

def build_graph(tree):
    """
    Builds a directed graph from the tree structure.
    """
    graph = nx.DiGraph()

    for node in tree.traverse():
        graph.add_node(node.id, name=node.name, type=node.node_type, path=node.path)

        if node.parent:
            graph.add_edge(node.parent.id, node.id)

        for imp in node.imports:
            graph.add_edge(node.id, imp)  #TODO: Import resolution has to be implemented
    return graph
