class TreeNode:
    """
    A class representing a node in a directory tree.
    """
    def __init__(self, name, node_type, path, parent=None, id=None):
        self.name = name
        self.node_type = node_type  
        self.path = path
        self.parent = parent
        self.children = []
        self.id = id
        self.imports = []  

    def add_child(self, child_node):
        self.children.append(child_node)

    def traverse(self):
        """
        Generator for traversing the tree.
        """
        yield self
        for child in self.children:
            yield from child.traverse()

    def __repr__(self):
        return f"TreeNode(name={self.name}, type={self.node_type}, id={self.id})"
